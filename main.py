#author narumeena
#description constaraint based modeling of antibiotic resistance.


#----------------------------------------------------------------------

import csv
from   csvToPandasStorage  import csv_reader
if __name__ == "__main__":
    csv_path = "/Users/naru/Documents/GitHub/pyrade/data/slectedGenes.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)
