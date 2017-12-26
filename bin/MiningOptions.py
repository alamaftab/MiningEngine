import csv
import urllib
import requests
from bs4 import BeautifulSoup
import re
import datetime
import calendar
import time
import os
import shutil
import sys
import string
import re
from time import gmtime, strftime
from datetime import datetime

###Help sites and notes 
##https://www.crummy.com/software/BeautifulSoup/bs4/doc/

url = "C:/aftab/aftab_personal/python/misc/VIX.html"
##url ="http://www.marketwatch.com/investing/index/vix/options?countrycode=US&showAll=True"
#html = urllib.urlopen(url)
##html = urllib.urlopen(url).read()

soup = BeautifulSoup(open(url), "html.parser")
##soup = BeautifulSoup(response.content, "html.parser")
find1 = soup.findAll('body')
##print(find1)

