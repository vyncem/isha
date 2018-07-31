#!/usr/bin/env python

import requests
import csv
import os
import pycountry
from datetime import datetime
from dateutil import tz


def writeCsv():
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'id', 'startDate', 'endDate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def executeGet(path):
    resp = requests.get("https://www.eventbriteapi.com/v3" + path,
                        headers={
                            "Authorization": "Bearer " + os.environ['EVENTBRITE_TOKEN'],
                        }, verify=True,  # Verify SSL certificate
                        )
    return resp

def getEvents(fromLocalDate, toLocalDate, organizerId):
    response = executeGet("/users/me/events");
    # response = executeGet("/events/search?start_date.range_start="
    #     +fromLocalDateTime+"&start_date.range_end="+toLocalDateTime+"&organizer.id="+organizerId+"&sort_by=date");
    if response.json().get('status_code') != None:
        print(response.json());
        return [];
    events = response.json()['events'];
    pageCount = response.json()['pagination']['page_count'];
    evs = [];
    i = 1;
    while i <= pageCount:
        print("page: "+str(i));
        nextResp = executeGet("/users/me/events?page="+str(i));
        events = nextResp.json()['events']
        for event in events:
            ev = EBEvent(event);
            fromDt = datetime.strptime(fromLocalDate,'%Y-%m-%d');
            toDt = datetime.strptime(toLocalDate,'%Y-%m-%d');
            dt = datetime.strptime(ev.utcDate,'%Y-%m-%dT%H:%M:%SZ');
            if fromDt < dt <= toDt:
                evs.append(ev);
        i += 1;
    return evs;

def getAttandeesEmailsForEvent(event):
    response = executeGet("/events/" + event.id + "/attendees/")
    attendees = response.json()['attendees']
    ebAttandees = []
    for attandee in attendees:
        attendeeObj = EBAttandee(attandee);
        if attendeeObj.status == 'Checked In':
            ebAttandees.append(attendeeObj);
    return ebAttandees;


def getEventCountry(event):
    response = executeGet("/venues/" + event.venueId)
    countryAlpha2 = response.json()['address']['country']
    if countryAlpha2 is not None:
        return pycountry.countries.get(alpha_2=countryAlpha2).name
    else:
        return 'None'


def getRegionDate(utcDateTime, regionTimeZone):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz(regionTimeZone)
    utc = datetime.strptime(utcDateTime, '%Y-%m-%dT%H:%M:%SZ')
    # Tell the datetime object that it's in UTC time zone since
    # datetime objects are 'naive' by default
    utc = utc.replace(tzinfo=from_zone)
    # Convert time zone
    regionDateTime = utc.astimezone(to_zone)
    return regionDateTime.date()


class EBEvent(object):
    """__init__() functions as the class constructor"""

    def __init__(self, event=None):
        self.name = event['name']['text'];
        self.id = event['id'];
        self.startDate = getRegionDate(event['start']['utc'], event['start']['timezone']);
        self.venueId = event['venue_id'];
        self.utcDate = event['start']['utc'];

    def __repr__(self):
        return '(' + self.name + ' , #' + self.id + ' , ' + str(self.startDate) + ' , ' + self.venueId + ')'

    def __str__(self):
        return '(' + self.name + ' , #' + self.id + ' , ' + str(self.startDate) + ' , ' + self.venueId + ')'


class EBAttandee(object):
    """__init__() functions as the class constructor"""

    def __init__(self, attandee=None):
        profile = attandee.get('profile')
        self.name = profile.get('name')
        self.id = attandee.get('id')
        self.email = profile.get('email')
        self.status = attandee.get('status')

    def __repr__(self):
        return '(' + self.name + ' , ' + self.email + ')'

    def __str__(self):
        return '(' + self.name + ' , ' + self.email + ')'



if __name__ == "__main__":
    with open(os.environ['DATA'] + '/events.csv', 'w') as csvfile:
        fieldnames = ['Event', 'Country', 'Date', 'Attendees']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        events = getEvents('2018-06-01','2018-07-21','14004606792');
        for event in events:
            try:
                ebAttandees = getAttandeesEmailsForEvent(event)
                if ebAttandees:
                    writer.writerow({'Event': event.name, 'Country': getEventCountry(
                    event), 'Date': event.startDate, 'Attendees': ebAttandees})
            except Exception as e:
                print(
                    'Error [' + str(e) + '] while fetching info for event : ' + str(event))
                writer.writerow({'Event': event.name, 'Country': 'error while getting country',
                                 'Date': event.startDate, 'Attendees': 'error while getting attandees'})
        csvfile.close()

    # print(response.json());
    #print(map(lambda ev: ev['name'], events))
