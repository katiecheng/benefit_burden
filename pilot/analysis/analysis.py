import os
import csv
from os import path
from factor import *

def get_data():
    """
    Takes user input for which data file to analyze, and returns (fn, data)
    where data is a list of response rows.
    """
    data_files = []
    for i, f in enumerate(os.listdir(data_path)):
        data_files.append(f)
        print i, ": ", f
    while True:
        try:
            index = int(raw_input("Type the index of the data file you'd like to analyze: "))
            fn_data = data_files[int(index)]
            break
        except ValueError:
            print("Not a valid index. Try again.")
        except IndexError:
            print("Not a valid index. Try again.")
    with open(data_path + fn_data) as infile:
        data = list(csv.DictReader(infile))
    return (fn_data, data)



here = path.dirname(path.realpath(__file__))
data_path = path.join(here, '..', 'data/')
fn, data = get_data()

print data