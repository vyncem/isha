#!/usr/bin/env python

##
## Script pulls stats from eventbrite sessions
##

import httplib
import os
import urllib

if __name__ == "__main__":

    token = os.environ['EVENTBRITE_TOKEN']
    params = '?token=' + token
    url = 'www.eventbriteapi.com'
    service = '/v3/users/me/'

    conn = httplib.HTTPSConnection(url , httplib.HTTPS_PORT)
    conn.request("POST", service + params)
    response = conn.getresponse()
    print 'response', response.status, response.reason

    data = response.read()
    print 'data', data
    conn.close()
