from behave import *
import vcr
import urllib2
import eventbrite
import re
import logging
import json


@given('I\'m a moderator')
def step_impl(context):
    pass

def scrub_string():
    def before_record_response(response):
        response['headers']['x-rate-limit'] = \
            re.sub(r"token:[A-Z0-9]*", 'XXX', response['headers']['x-rate-limit'][0])
        return response
    return before_record_response

@when('I pull eventbrite stats')
@vcr.use_cassette(filter_headers=['Authorization'], before_record_response=scrub_string())
def step_impl(context):
    context.event = eventbrite.getEvents()[-1]
    context.attendees = eventbrite.getAttandeesEmailsForEvent(context.event)

@then('I get valid stats')
def step_impl(context):
    expected_event = '{"startDate": "2018-06-25T21:00:00Z", "endDate": "2018-06-25T22:30:00Z", "name": "Isha Offering (Free)", "id": "47440729499"}'
    attending = '{"status": "Attending", "id": "983076728", "cell_phone": null, "name": "Isha one", "email": "isha-1@mailinator.com"}'
    checked_in = '{"status": "Checked In", "id": "983077546", "cell_phone": null, "name": "Isha two", "email": "isha-2@mailinator.com"}'
    assert(str(context.event) == expected_event)
    assert((attending in str(context.attendees)) == True)
    assert((checked_in in str(context.attendees)) == True)
