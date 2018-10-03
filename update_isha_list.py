#!/usr/bin/env python

import mailchimp
import eventbrite
import os

if __name__ == '__main__':
    startDate = os.environ['EVENTBRITE_START']
    endDate = os.environ['EVENTBRITE_END']
    orgId = os.environ['EVENTBRITE_ORG_ID']

    client = mailchimp.MailChimpClient().client
    listId = os.environ['MAILCHIMP_LIST_ID']

    events = eventbrite.getEvents(startDate, endDate, orgId)
    for event in events:
        try:
            ebAttandees = eventbrite.getAttandeesEmailsForEvent(event)
            if ebAttandees:
                for ebAttendee in ebAttandees:
                    { "merge_fields": { "FNAME": "" }, "email_address": "", "status": "subscribed"}
                    member = { "merge_fields": { "FNAME": ebAttendee.name },
                               "email_address": ebAttendee.email,
                               "status": "subscribed" }
                    try:
                        client.lists.members.create(list_id=listId, data=member)
                    except Exception as e:
                        print '=== Error:', e
        except Exception as e:
            print 'Error: ' + str(e)
