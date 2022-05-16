#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ad_user_match.py
#
### Heavily based on: https://pbpython.com/record-linking.html

import requests
import json
import os 
import pandas as pd
from pathlib import Path
import fuzzymatcher
import numpy as np
from dotenv import load_dotenv

from pprint import pprint


# Load environment variables from `.env` file.
#
# Have a .env file in the directory of this script, containing:
"""
# .env 

# csv dump files of active directories
AD_DUMP_FILE_1=<your file with path here>
AD_DUMP_FILE_2=<your file with path here>
OUT_FILE=<your file with path here>

#
# End of .env
"""

load_dotenv()
# Your values are now stored in `os.environ`


### Variables
ad_file_1 = os.environ.get('AD_DUMP_FILE_1', '')
ad_file_2 = os.environ.get('AD_DUMP_FILE_2', '')
out_file = os.environ.get('OUT_FILE', '')


### Read csv files
ad_dump_1 = pd.read_csv(ad_file_1)
ad_dump_1['one_num'] = np.arange(len(ad_dump_1))

ad_dump_2 = pd.read_csv(ad_file_2, sep=';')
ad_dump_2['two_num'] = np.arange(len(ad_dump_2))

print(ad_dump_1.head())
print(ad_dump_2.head())

### Define columns to use in fuzzy search

left_on = ["Display name", "User logon name", "E-mail"]
right_on = ["cnName", "ADUserName", "Mailaccount"]


matched_results = fuzzymatcher.fuzzy_left_join(ad_dump_1,
                                               ad_dump_2,
                                               left_on,
                                               right_on,
                                               left_id_col='one_num',
                                               right_id_col='two_num')

print(matched_results.head())

# Reorder the columns to make viewing easier
cols = [
    "best_match_score", "one_num", "two_num",
    "User logon name", "ADUserName",
    "Display name", "cnName",
    "E-mail", "Mailaccount"
    ]
 

print(matched_results[cols].sort_values(by=['best_match_score'], ascending=False).head(5))

matched_results[cols].sort_values(by=['best_match_score'], ascending=False).to_csv(out_file)