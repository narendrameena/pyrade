#author narumeena
#description reading csv data files and storing them using pandas package

import pandas as pd
from readingDiffrentFileFormats import csv_reader
#----------------------------------------------------------------------

def gene_names_antibiotic():
    """
        Read gene names list related to antibiotic using pandas from a CSV file
    """
    gene_names_antibiotic_file = "/Users/naru/Documents/GitHub/pyrade/data/slectedGenes.csv"
    with open(gene_names_antibiotic_file, "rb") as f_obj:
        csv_reader(f_obj)



def data_group_sample():
    """
        reading data or samples as they are for same condition
    """
    data_group_sample_file = "/Users/naru/Documents/GitHub/pyrade/data/dataGroupSamples.csv"
    with open(data_group_sample_file, "rb") as f_obj:
        csv_reader(f_obj)

def normlized_sample_data():
    """
        normlized exprassion data of all microarray samples data
    """
    normlized_exprassion_data_file = "/Users/naru/Documents/GitHub/pyrade/data/varAllData.csv"
    with open(normlized_exprassion_data_file,"rb") as f_obj:
        csv_reader(f_obj)
