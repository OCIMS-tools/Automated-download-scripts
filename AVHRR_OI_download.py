# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:36:05 2019

@author: matth
"""

import sys, os
from math import floor,ceil
import numpy as np
from datetime import date
import datetime

#from pydap.client import open_url
#from netCDF4 import Dataset

#Using current date as reference
today = date.today()
#Account for latency of the SST product
yesterday = today - datetime.timedelta(days = 2)
n_day = yesterday.strftime("%d")
long_day = yesterday.strftime("%j")
n_month = yesterday.strftime("%m")
n_year = yesterday.strftime("%Y")
n_hour = '120000'

#Url of data storage website
url = 'https://opendap.jpl.nasa.gov/opendap/hyrax/OceanTemperature/ghrsst/data/GDS2/L4/GLOB/NCEI/AVHRR_OI/v2.1/'

#Building string for download
#The suffix of the file name to be saved (output)
sname = '-NCEI-L4_GHRSST-SSTblend-AVHRR_OI-GLOB-v02.0-fv02.1.nc'
filename = str(url) + str(n_year) + '/' + str(long_day) + '/' + str(n_year+n_month+n_day+n_hour)+ str(sname)
#Save path where file is to be stored 
path_fileout = '/home/ocims_platform/SST_auto/data/'
#Save name of file
filenameout = ('daily' + str(sname))


#Run command to start download
cmd=' wget "'  + filename +'"' + ' -O ' + path_fileout + filenameout
os.system( cmd )

