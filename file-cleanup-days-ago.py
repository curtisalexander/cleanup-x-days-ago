#!/usr/bin/env python

import arrow
import datetime
import os
import re

# everything in US/Central
some_days_ago = arrow.now().floor('day').replace(days=-3)
date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')

for root, dirs, files in os.walk('/some/network/dir/backup'):
    for name in files:
        full_pathname = os.path.realpath(os.path.join(root, name))
        file_date_string = date_pattern.search(name).group(0)
        file_date = datetime.datetime.strptime(file_date_string,
                                               '%Y-%m-%d').date()
        file_date_floor = arrow.get(file_date, 'US/Central').floor('day')
        if file_date_floor <= some_days_ago:
            os.remove(full_pathname)
