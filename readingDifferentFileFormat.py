#author: narumeena
#description: functions to reading different data formats files


#! /usr/bin/env python
#----------------------------------------------------------------------
import pandas as pd

def csv_reader(file_obj):
    """
        simple read function with default encoding
    """
    reader = pd.read_csv(file_obj ,low_memory=False)
    return reader
