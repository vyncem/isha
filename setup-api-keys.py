#!/usr/bin/env python

import securekeys

securekeys.load()
# put original keys below
securekeys.store('EVENTBRITE_ORG_ID', 'somekey')
securekeys.store('MAILCHIMP_LIST_ID', 'somekey')
securekeys.store('EVENTBRITE_TOKEN', 'somekey')
securekeys.store('MAILCHIMP_TOKEN', 'somekey')
