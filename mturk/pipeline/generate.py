import os
import re
import csv
import config
from helpers import *
from maps import *

NUM_ITEMS = 27
MAX_SCORE_PER_ITEM = 4

def get_raw_data():
    """
    Takes user input for which raw data file to import, and returns (fn, data)
    where data is a list of response rows.
    """
    data_files = []
    for i, f in enumerate(os.listdir(config.RAW_DATA_DIR)):
        data_files.append(f)
        print i, ": ", f
    while True:
        try:
            index = int(raw_input("Type the index of the data file you'd like to import: "))
            fn_raw_data = data_files[int(index)]
            break
        except ValueError:
            print("Not a valid index. Try again.")
        except IndexError:
            print("Not a valid index. Try again.")
    print "Importing %s..." % fn_raw_data
    with open(config.RAW_DATA_DIR + fn_raw_data) as infile:
        next(infile)
        raw_data = list(csv.DictReader(infile))
    return (fn_raw_data, raw_data)

def wrangle(raw_data):
    data = raw_data
    
    with open(config.RAW_DATA_DIR + 'keys.csv', 'rU') as infile:
        keys = list(csv.DictReader(infile))

    #TO DO, calculate scores for overal ben and burd, as well as ben/burd subscales
    curBenSocial = [k['new_header'] for k in keys if re.search("curr.ben.social", k['new_header'])]

fn, raw_data = get_raw_data()
data = wrangle(raw_data)
