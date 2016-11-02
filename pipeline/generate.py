import os
import re
import csv
import config
from helpers import *
from maps import *


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
        next(infile)
        raw_data = list(csv.DictReader(infile))
    return (fn_raw_data, raw_data)


def wrangle(raw_data):
    data = raw_data
    for response in data:
        for q, a in response.items():
            if q == 'gender':
                response[q + '_num'] = mapGender.get(a)
            elif q == 'age':
                if isInt(a):
                    response[q + '_num'] = int(a)
                else:
                    response[q + '_num'] = None
            elif q == 'educ':
                response[q + '_num'] = mapEduc.get(a)
            elif q == 'current' or q == 'abandoned':
                response[q + '_category'] = mapApp.get(a)
            elif re.match('current_', q) or re.match('abandoned_', q):
                response[q + '_num'] = mapLikert.get(a)

    return data


def write_data(filename, data):
    with open(config.DATA_DIR + filename, 'w') as outfile:
        fieldnames = data[0].keys()
        fieldnames.sort()
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for response in data:
            writer.writerow(response)


fn, raw_data = get_raw_data()
data = wrangle(raw_data)
write_data(fn, data)
