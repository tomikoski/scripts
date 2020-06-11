#!/usr/bin/python3
# coding: utf-8

import calendar
import locale
import argparse

years = [2020,2019,2018,2017]
months = []

parser = argparse.ArgumentParser(description="Generate fancy password using dates and stuff")
parser.add_argument('locale', metavar='LOCALE', nargs='+',help="Locale such as: fi_FI or en_US...")
args = parser.parse_args()

# if you want these in certain language...
#locale.setlocale(locale.LC_ALL, 'fi_FI')

for l in args.locale:

  for i in range(1,13):
    months.append(calendar.month_abbr[i])
    months.append(calendar.month_abbr[i].lower())
    months.append(calendar.month_abbr[i].upper())
    months.append(calendar.month_name[i])
    months.append(calendar.month_name[i].lower())
    months.append(calendar.month_name[i].upper())


  for y in years:
    for m in months:
       print(f"{y}{m}")
       print(f"{m}{y}")

