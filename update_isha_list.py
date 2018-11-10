#!/usr/bin/env python

import mailchimp
import eventbrite
import sys
import logging
import securekeys
import os
from datetime import datetime, timedelta

if __name__ == '__main__':
    securekeys.load()
    logging.basicConfig(filename=os.environ['FREE_OFFERING_WORKSPACE']+'/events.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    logging.info('-----------------------------------------------------------------------------')
    if len(sys.argv) == 3:
        # get startdate and enddate from command line args
        startDate = sys.argv[1]
        endDate = sys.argv[2]
    else:
        # otherwise fetch events in following way
        #  if it is monday fetch for saturday, sunday, monday
        #  if it is wednesday fetch for tuesday, wenesday
        #  if it is friday fetch for thursday, friday
        today = datetime.today()
        if today.weekday() == 0:  # 0 means monday
            gap = 2  # saturday, sunday, monday
        else:
            gap = 1  # tuesday,wednesday/thursday,friday
        print(f'day : {today.weekday()} ,gap {gap}')
        startDate = (today - timedelta(days=gap)).strftime("%Y-%m-%d")
        endDate = today.strftime("%Y-%m-%d")
    logging.info('-----------Running scheduler for sessions from %s to %s-----------', startDate, endDate)
    orgId = securekeys.retrieve('EVENTBRITE_ORG_ID')

    client = mailchimp.MailChimpClient().client
    listId = securekeys.retrieve('MAILCHIMP_LIST_ID')

    events = eventbrite.getEvents(startDate, endDate, orgId)
    totalEmailScheduled = 0
    for event in events:
        try:
            print(f'name: {event.name}, date: {event.startDate}')
            ebAttandees = eventbrite.getAttandeesEmailsForEvent(event)
            successCount = 0
            if ebAttandees:
                for ebAttendee in ebAttandees:
                    {"merge_fields": { "FNAME": "" }, "email_address": "", "status": "subscribed"}
                    member = {"merge_fields": {"FNAME": ebAttendee.name},
                               "email_address": ebAttendee.email,
                               "status": "subscribed"}
                    try:
                        client.lists.members.create(list_id=listId, data=member)
                        successCount = successCount+1
                    except Exception as e:
                        print('=== Error:', e)
                        logging.error('Error while creating member in list for attendee: ' + str(e)+', attandee: '+str(ebAttendee));
            logging.info('Event: %s, total attendees: %s, email scheduled: %s', event.name, len(ebAttandees), successCount)
            totalEmailScheduled = totalEmailScheduled + successCount
        except Exception as e:
            print('Error: ' + str(e))
            logging.error('Error while getting attendee: '+ str(e)+', for event: '+str(event));
    logging.info('-----------Total emails scheduled for sessions from %s to %s are %s------------', startDate, endDate, totalEmailScheduled)
