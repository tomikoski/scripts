#!/usr/bin/python3

import calendar
import locale
import argparse

years = [2017,2018,2019,2020]
months = []

parser = argparse.ArgumentParser(description="Generate fancy passwords using dates!")
parser.add_argument('locale', nargs='+', help="Locale such as: fi_FI or en_US or en_DK.UTF-8...")
args = parser.parse_args()

for l in args.locale:
  try:
    locale.setlocale(locale.LC_ALL, l)
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

  except:
   print("error: probably incorrect locale?")

