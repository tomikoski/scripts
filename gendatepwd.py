#!/usr/bin/python3
# coding: utf-8

import calendar
import locale

years = [2020,2019,2018,2017]
months = []

# if you want these in certain language...
locale.setlocale(locale.LC_ALL, 'fi_FI')

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

