#!/usr/bin/python2.6
'''
Script name:    engine_check.py

Description:    This script is for URL verification. It checkes if there are
                any issues with to many connection or timeouts.

Author:         run2cmd

Version:        1.0 - Initial version - by run2cmd
                '''

import pycurl
from StringIO import StringIO
import argparse

class CheckURL():

    def __init__(self):
        self.val = ''

    def c_url(self, my_url, time_out):
        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, my_url)
        c.setopt(c.WRITEFUNCTION, buffer.write)
        c.setopt(c.TIMEOUT, time_out)
        c.perform()
        c.close()
        body = buffer.getvalue()
        return body

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This is Icinga plugin for URL check.\nAuthor:\trun2cmd')
    parser.add_argument('-u', type=str, help='URL to check', required=True)
    args = parser.parse_args()

    cu = CheckURL()
    try:
        cu.c_url(args.u, 5)
        print 'OK: Access to site completed successfully'
    except (pycurl.error):
        print 'CRITICAL: Curl failed to retrive data from %s' % (args.u)
