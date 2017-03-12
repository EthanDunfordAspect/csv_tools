# -*- coding: utf-8 -*-
# -- ---------------------------------------------------------------------------
# --
# -- Title:        time_stamp
# -- License:      Apache License Version 2.0
# -- Author:       Ethan Dunford
# -- Version:      1
# -- Date:         02/09/2016
# --
# -- ---------------------------------------------------------------------------
import time
import datetime


def date_time_stamp_With_string(string_to_print):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%d-%m-%Y %H:%M:%S")
    print string_to_print + ' ' + st


def date_time_stamp(string):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%d-%m-%Y %H:%M:%S")
    t = '[' + str(st) + '] ' + str(string)
    return t


def date_stamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
    st = '_' + st
    return st


def time_stamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
    return st


def date_time_stamp_joined():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%d%m%Y-%H%M%S")
    t = str(st)
    return t
