#!/usr/bin/env python3

import csv

f = open('csv_users.txt', 'r')
i = 0

for x in csv.reader(f):
    i = i + 1
    filename = 'admin.rc%d'%(i,)
    rcfile = open(filename, 'w')
    print('export OS_AUTH_URL=' + x[0], file=rcfile)
    print('export OS_IDENTITY_API_VERSION=3', file=rcfile)
    print('export OS_PROJECT_NAME=' + x[1], file=rcfile)
    print('export OS_PROJECT_DOMAIN_NAME=' + x[2], file=rcfile)
    print('export OS_USERNAME=' + x[3], file=rcfile)
    print('export OS_USER_DOMAIN_NAME=' + x[4], file=rcfile)
    print('export OS_PASSWORD=' + x[5], file=rcfile)
    rcfile.close()