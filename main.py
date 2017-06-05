#author narumeena
#description constaraint based modeling of antibiotic resistance.

import csv
#----------------------------------------------------------------------

from csvToPandasStorage import *
if __name__ == "__main__":
    gene_names_antibiotic()
    data_group_sample()
    normlized_sample_data()
