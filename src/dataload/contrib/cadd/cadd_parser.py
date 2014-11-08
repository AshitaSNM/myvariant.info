# -*- coding: utf-8 -*-

import pysam
from itertools import groupby, imap
import pymongo
import time
#from utils.common import timesofar


VALID_COLUMN_NO = 90
DEPENDENCIES = ["pysam", "pymongo"]


# remove keys whos values are "."
# and remove empty dictionaries
def dict_sweep(d):
    for key, val in d.items():
        if val == "NA":
            del d[key]
        elif isinstance(val, dict):
            dict_sweep(val)
            if len(val) == 0:
                del d[key]
    return d


# convert string numbers into integers or floats
def value_convert(d):
    for key, val in d.items():
        try:
            d[key] = int(val)
        except (ValueError, TypeError):
            try:
                d[key] = float(val)
            except (ValueError, TypeError):
                pass
        if isinstance(val, dict):
            value_convert(val)
    return d


# if dict value is a list of length 1, unlist
def unlist(d):
    for key, val in d.items():
            if isinstance(val, list):
                if len(val) == 1:
                    d[key] = val[0]
            elif isinstance(val, dict):
                unlist(val)
    return d


# convert one snp to json
def _map_line_to_json(fields):
    if len(fields) == VALID_COLUMN_NO:
        chrom = fields[0]
        chromStart = fields[1]
        allele1 = fields[2]
        allele2 = fields[4]
        HGVS = "chr%s:g.%s%s>%s" % (chrom, chromStart, allele1, allele2)
    
        # load as json data
        if HGVS is None:
            return
    
        one_snp_json = {
    
                "_id": HGVS,
                "cadd":
                    {
                         'chrom': fields[0],
                         'pos': fields[1],
                         'ref': fields[2],
                         'anc': fields[3],
                         'alt': fields[4],
                         'type': fields[5],
                         'length': fields[6],
                         'istv': fields[7],
                         'isderived': fields[8],
                         'annotype': fields[9],
                         'consequence': fields[10],
                         'consscore': fields[11],
                         'consdetail': fields[12],
                         'gc': fields[13],
                         'cpg': fields[14],
                         'mapability':
                             {
                                 '20bp': fields[15],
                                 '35bp': fields[16]
                             },
                         'scoresegdup': fields[17],
                         'phast_cons':
                             {
                                 'primate': fields[18],
                                 'mammalian': fields[19],
                                 'vertebrate': fields[20]
                             },
                         'phylop':
                             {
                                 'primate': fields[21],
                                 'mammalian': fields[22],
                                 'vertebrate': fields[23]
                             },
                         'gerp':
                             {
                                 'n': fields[24],
                                 's': fields[25],
                                 'rs': fields[26],
                                 'rs_pval': fields[27]
                             },
                         'bstatistic': fields[28],
                         'encode':
                             {
                                 'exp': fields[29],
                                 'h3k27ac': fields[30],
                                 'h3k4me1': fields[31],
                                 'h3k4me3': fields[32],
                                 'nucleo': fields[33],
                                 'occ': fields[34],
                                 'p_val':
                                     {
                                         'comb': fields[35],
                                         'dnas': fields[36],
                                         'faire': fields[37],
                                         'polii': fields[38],
                                         'ctcf': fields[39],
                                         'mycp': fields[40]
                                     },
                                 'sig':
                                     {
                                         'dnase': fields[41],
                                         'faire': fields[42],
                                         'polii': fields[43],
                                         'ctcf': fields[44],
                                         'myc': fields[45]
                                     },
                             },
                         'segway': fields[46],
                         'motif':
                             {
                                 'toverlap': fields[47],
                                 'dist': fields[48],
                                 'ecount': fields[49],
                                 'ename': fields[50],
                                 'ehipos': fields[51],
                                 'escorechng': fields[52]
                             },
                         'tf':
                             {
                                 'bs': fields[53],
                                 'bs_peaks': fields[54],
                                 'bs_peaks_max': fields[55]
                             },
                         'isknownvariant': fields[56],
                         'esp':
                             {
                                 'af': fields[57],
                                 'afr': fields[58],
                                 'eur': fields[59]
                             },
                         '1000g':
                             {
                                 'af': fields[60],
                                 'asn': fields[61],
                                 'amr': fields[62],
                                 'afr': fields[63],
                                 'eur': fields[64]
                             },
                         'min_dist_tss': fields[65],
                         'min_dist_tse': fields[66],
                         'gene':
                             {
                                 'gene_id': fields[67],
                                 'feature_id': fields[68],
                                 'ccds_id': fields[69],
                                 'genename': fields[70],
                                 'cds':
                                     {
                                         'cdna_pos': fields[71],
                                         'rel_cdna_pos': fields[72],
                                         'cds_pos': fields[73],
                                         'rel_cds_pos': fields[74]
                                     },
                                 'prot':
                                     {
                                         'protpos': fields[75],
                                         'rel_prot_pos': fields[76],
                                         'oaa': fields[81],
                                         'naa': fields[82]
                                     },
                                 'dst_2_splice': fields[77],
                                 'dst_2_spltype': fields[78],
                                 'exon': fields[79],
                                 'intron': fields[80]
                             },
                         'grantham': fields[83],
                             'polyphen':
                             {
                                 'cat': fields[84],
                                 'val': fields[85]
                             },
                         'sift':
                             {
                                 'cat': fields[86],
                                 'val': fields[87]
                             },
                         'rawscore': fields[88],
                         'phred': fields[89]
                      }
                }
        return dict_sweep(unlist(value_convert(one_snp_json)))


def merge_duplicate_rows(rows):
    rows = list(rows)
    first_row = rows[0]
    other_rows = rows[1:]
    for row in other_rows:
        for i in first_row["cadd"]:
            if i in row["cadd"]:
                if row["cadd"][i] != first_row["cadd"][i]:
                    aa = first_row["cadd"][i]
                    if not isinstance(aa, list):
                        aa = [aa]
                    aa.append(row["cadd"][i])
                    first_row["cadd"][i] = aa             
    return first_row


# open file, parse, pass to json mapper
def data_generator(input_file):
        # All possible SNVs of GRCh37/hg19 incl. all annotations
        cadd = pysam.Tabixfile(input_file)
        for contig in cadd.contigs:
            if contig == 1:
                cadd = cadd.fetch(contig)
                cadd = imap(lambda x: x.split(), cadd)
                json_rows = imap(_map_line_to_json, cadd)
                row_groups = (it for (key, it) in groupby(json_rows, lambda row: row["_id"]))
                cnt = 0
                for one_snp_json in imap(merge_duplicate_rows, row_groups):
                    cnt += 1
                    yield one_snp_json
                    if cnt == 100:
                        break
                    

i = data_generator('http://krishna.gs.washington.edu/download/CADD/v1.0/whole_genome_SNVs_inclAnno.tsv.gz')
out=list(i)

# load collection into mongodb
def load_collection(database, cadd_url, collection_name):
    """
    : param database: mongodb url
    : param input_file_list: variant docs, path to file
    : param collection_name: annotation source name
    """
    conn = pymongo.MongoClient(database)
    db = conn.variantdoc
    posts = db[collection_name]
    t1 = time.time()
    cnt = 0
    for doc in data_generator(cadd_url):
        posts.insert(doc, manipulate=False, check_keys=False, w=0)
        cnt += 1
        if cnt % 100000 == 0:
            print cnt, timesofar(t1)
    print "successfully loaded %s into mongodb" % collection_name 