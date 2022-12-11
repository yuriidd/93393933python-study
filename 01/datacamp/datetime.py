# -*- coding: utf-8 -*-
"""Created on Tue Nov  8 21:06:18 2022@author: xiaom"""

from datetime import datetime

from pytz import timezone


###############                         DATETIME - TIMEZONE


#       basic
local_dt = datetime.now()
print(local_dt)

date_str = '06/08/2010'
date_dt = datetime.strptime(date_str, '%m/%d/%Y')
print(date_dt)
date_dt # datetime.datetime(2010, 6, 8, 0, 0)

date_str_again = date_dt.strftime('%m/%d/%Y')
date_str_again2 = date_dt.strftime('%Y/%m/%d')
print(date_str_again, date_str_again2)
print(date_dt.isoformat())

####################     TIMEZONE
print(date_dt)
ny_tz = timezone('US/Eastern')
la_tz = timezone('US/Pacific')
ny_dt = date_dt.replace(tzinfo = ny_tz)
la_dt = ny_dt.astimezone(la_tz)
print(ny_dt)
print(la_dt)

##




