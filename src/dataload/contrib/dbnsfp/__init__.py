from .dbnsfp_parser import load_data as _load_data

DBNSFP_INPUT_FILE = '/opt/myvariant.info/load_archive/dbnsfp/dbNSFP3.0b2c_variant.chr*'

__METADATA__ = {
    "src_name": 'dbNSFP',
    "src_url": 'https://sites.google.com/site/jpopgen/dbNSFP',
    "version": '2.9',
    "field": 'dbnsfp'
}


def load_data():
    dbnsfp_data = _load_data(DBNSFP_INPUT_FILE)
    return dbnsfp_data


def get_mapping():
    mapping = {
        "dbnsfp": {
            "properties": {
                "rsid": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "chrom": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "hg18": {
                    "properties": {
                        "start": {
                            "type": "long"
                        },
                        "end": {
                            "type": "long"
                        }
                    }
                },
                "hg19": {
                    "properties": {
                        "start": {
                            "type": "long"
                        },
                        "end": {
                            "type": "long"
                        }
                    }
                },
                "hg38": {
                    "properties": {
                        "start": {
                            "type": "long"
                        },
                        "end": {
                            "type": "long"
                        }
                    }
                },
                "ref": {
                    "type": "string"
                },
                "alt": {
                    "type": "string"
                },
                "aa": {
                    "properties": {
                        "alt": {
                            "type": "string",
                            "analyzer": "string_lowercase"
                        },
                        "ref": {
                            "type": "string",
                            "analyzer": "string_lowercase"
                        },
                        "pos": {
                            "type": "integer"
                        },
                        "refcodon": {
                            "type": "string"
                        },
                        "codonpos": {
                            "type": "integer"
                        }
                    }
                },
                "genename": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "uniprot": {
                    "properties": {
                        "acc": {
                            "type": "string"
                        },
                        "pos": {
                            "type": "string"
                        }
                    }
                },
                "interpro_domain": {
                    "type": "string"
                },
                "cds_strand": {
                    "type": "string"
                },
                "ancestral_allele": {
                    "type": "string"
                },
                "ensembl": {
                    "properties": {
                        "transcriptid": {
                            "type": "string"
                        },
                        "geneid": {
                            "type": "string"
                        }
                    }
                },
                "sift": {
                    "properties": {
                        "converted_rankscore": {
                            "type": "float"
                        },
                        "pred": {
                            "type": "string"
                        },
                        "score": {
                            "type": "float"
                        }
                    }
                },
                "polyphen2": {
                    "properties": {
                        "hdiv": {
                            "properties": {
                                "pred": {
                                    "type": "string"
                                },
                                "score": {
                                    "type": "float"
                                },
                                "rankscore": {
                                    "type": "float"
                                }
                            }
                        },
                        "hvar": {
                            "properties": {
                                "pred": {
                                    "type": "string"
                                },
                                "score": {
                                    "type": "float"
                                },
                                "rankscore": {
                                    "type": "float"
                                }
                            }
                        }
                    }
                },
                "lrt": {
                    "properties": {
                        "converted_rankscore": {
                            "type": "float"
                        },
                        "pred": {
                            "type": "string"
                        },
                        "score": {
                            "type": "float"
                        },
                        "omega": {
                            "type": "float"
                        }
                    }
                },
                "mutationtaster": {
                    "properties": {
                        "converted_rankscore": {
                            "type": "float"
                        },
                        "pred": {
                            "type": "string"
                        },
                        "score": {
                            "type": "float"
                        },
                        "model": {
                            "type": "string",
                            "analyzer": "string_lowercase"
                        },
                        "AAE": {
                            "type": "string"
                        }
                    }
                },
                "mutationassessor": {
                    "properties": {
                        "pred": {
                            "type": "string"
                        },
                        "score": {
                            "type": "float"
                        },
                        "rankscore": {
                            "type": "float"
                        }
                    }
                },
                "fathmm": {
                    "properties": {
                        "pred": {
                            "type": "string"
                        },
                        "score": {
                            "type": "float"
                        },
                        "rankscore": {
                            "type": "float"
                        }
                    }
                },
                "provean": {
                    "properties": {
                        "score": {
                            "type": "float"
                        },
                        "rankscore": {
                            "type": "float"
                        },
                        "pred": {
                            "type": "string"
                        }
                    }
                },
                "metasvm": {
                    "properties": {
                        "score": {
                            "type": "float"
                        },
                        "rankscore": {
                            "type": "float"
                        },
                        "pred": {
                            "type": "string"
                        }
                    }
                },
                "lr": {
                    "properties": {
                        "pred": {
                            "type": "string"
                        },
                        "score": {
                            "type": "float"
                        },
                        "rankscore": {
                            "type": "float"
                        }
                    }
                },
                "reliability_index": {
                    "type": "integer"
                },
                "gerp++": {
                    "properties": {
                        "rs_rankscore": {
                            "type": "float"
                        },
                        "nr": {
                            "type": "float"
                        },
                        "rs": {
                            "type": "float"
                        }
                    }
                },
                "phylop_7way": {
                    "properties": {
                        "vertebrate": {
                            "type": "float"
                        },
                        "vertebrate_rankscore": {
                            "type": "float"
                        }
                    }
                },
                "phastcons_7way": {
                    "properties": {
                        "vertebrate": {
                            "type": "float"
                        },
                        "vertebrate_rankscore": {
                            "type": "float"
                        }
                    }
                },
                "siphy_29way": {
                    "properties": {
                        "pi": {
                            "properties": {
                                "a": {
                                    "type": "float",
                                },
                                "c": {
                                    "type": "float",
                                },
                                "t": {
                                    "type": "float",
                                },
                                "g": {
                                    "type": "float",
                                },
                            }
                        },
                        "logodds": {
                            "type": "float"
                        },
                        "logodds_rankscore": {
                            "type": "float"
                        }
                    }
                },
                "1000gp1": {
                    "properties": {
                        "ac": {
                            "type": "integer"
                        },
                        "af": {
                            "type": "float"
                        },
                        "afr_af": {
                            "type": "float"
                        },
                        "afr_ac": {
                            "type": "integer"
                        },
                        "eur_ac": {
                            "type": "integer"
                        },
                        "eur_af": {
                            "type": "float"
                        },
                        "amr_ac": {
                            "type": "integer"
                        },
                        "amr_af": {
                            "type": "float"
                        },
                        "eas_af": {
                            "type": "float"
                        },
                        "eas_ac": {
                            "type": "integer"
                        },
                        "sas_af": {
                            "type": "float"
                        },
                        "sas_ac": {
                            "type": "integer"
                        },
                    }
                },
                "twinsuk": {
                    "properties": {
                        "ac": {
                            "type": "integer"
                        },
                        "af": {
                            "type": "float"
                        }
                    }
                },
                "alspac": {
                    "properties": {
                        "ac": {
                            "type": "integer"
                        },
                        "af": {
                            "type": "float"
                        }
                    }
                },
                "esp6500": {
                    "properties": {
                        "ea_af": {
                            "type": "float"
                        },
                        "aa_af": {
                            "type": "float"
                        },
                        "ea_ac": {
                            "type": "integer"
                        },
                        "aa_ac": {
                            "type": "integer"
                        }
                    }
                },
                "exac": {
                    "properties": {
                        "ac": {
                            "type": "integer"
                        },
                        "af": {
                            "type": "float"
                        },
                        "adj_ac": {
                            "type": "integer"
                        },
                        "adj_af": {
                            "type": "float"
                        },
                        "afr_ac": {
                            "type": "integer"
                        },
                        "afr_af": {
                            "type": "float"
                        },
                        "amr_ac": {
                            "type": "integer"
                        },
                        "amr_af": {
                            "type": "float"
                        },
                        "eas_ac": {
                            "type": "integer"
                        },
                        "eas_af": {
                            "type": "float"
                        },
                        "fin_ac": {
                            "type": "integer"
                        },
                        "fin_af": {
                            "type": "float"
                        },
                        "nfe_ac": {
                            "type": "integer"
                        },
                        "nfe_af": {
                            "type": "float"
                        },
                        "sas_ac": {
                            "type": "integer"
                        },
                        "sas_af": {
                            "type": "float"
                        }
                    }
                },
                "clinvar": {
                    "properties": {
                        "rs": {
                            "type": "string"
                        },
                        # "clinsig": {
                        #     "type": "integer"     # can contain |, like 5|5, FIXME
                        # },
                        "trait": {
                            "type": "string"        # can contain |, FIXME
                        }
                    }
                }
            }
        }
    }
    return mapping
