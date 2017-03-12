# -*- coding: utf-8 -*-
# -- ---------------------------------------------------------------------------
# --
# -- Title:        run.py
# -- License:      Apache License Version 2.0
# -- Author:       Ethan Dunford
# -- Version:      1
# -- Date:        11/03/17
# --
# -- ---------------------------------------------------------------------------
from lib.time_stamp import date_time_stamp
import os
import os.path
import csv
import time


# -- Check data location
# -- ---------------------------------------------------------------------------


def check_data(dir_path, data_folder, data_file):
    full_path = file_path = dir_path + '/' + data_folder + '/' + data_file
    if os.path.exists(full_path):
        print date_time_stamp('Data found: ' + data_file)
        return full_path
    else:
        print date_time_stamp('Data not found: ' + data_file)
        return False

# -- Read csv
# -- ---------------------------------------------------------------------------


def read_csv_data(data_file, new_headers):
    if data_file is not False:
        new_data_list     = []
        with open(data_file) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                    _new_data         = {}
                    for key, value in row.iteritems():
                        if key in new_headers.keys():
                            key = new_headers[key]
                            _new_data[key] = value
                    new_data_list.append(_new_data)
        return new_data_list



dir_path     = os.path.dirname(os.path.abspath(__file__))
data_folder  = 'data'
data_file    = 'result.csv'
new_headers  = {
    'data__001': 'name',
    'data__002': 'email',
    'data__003': 'dob',
    'data__004': 'country',
    'data__005': 'postcode'
}

print date_time_stamp('Hello world')
data_file = check_data(dir_path, data_folder, data_file)

print date_time_stamp('Processing Data')
csv_data  = read_csv_data(data_file, new_headers)

print date_time_stamp('New data ready.')

#
# for data in csv_data:
#     print data
