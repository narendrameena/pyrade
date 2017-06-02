#author narumeena

#description reading csv data files and storing them using pandas package


import pandas as pd
#----------------------------------------------------------------------

def csv_reader(file_obj):
    """
    Read a CSV file using pandas
    """
    reader = pd.read_csv(file_obj, sep=',')
    print(reader)
