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
    expected_event = '(Isha Offering (Free) , #47440729499 , 2018-06-25 , 25443248)'
    attending = '(Isha one , isha-1@mailinator.com , Attending)'
    checked_in = '(Isha two , isha-2@mailinator.com , Checked In)'
    assert(str(context.event) == expected_event)
    assert((attending in str(context.attendees)) == True)
    assert((checked_in in str(context.attendees)) == True)
