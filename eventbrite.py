#!/usr/bin/env python

import os
import requests
import json

def executeGet(path):
    resp = requests.get("https://www.eventbriteapi.com/v3" + path,
                        headers={
                            "Authorization": "Bearer %s" % (os.environ['EVENTBRITE_TOKEN'],),
                        }, verify=True,  # Verify SSL certificate
                        )
    return resp


def getEvents():
    response = executeGet("/users/me/owned_events/")

    if response.json().get('status_code') != None:
        print response.json();
        return []

    events = response.json()['events']
    evs = []
    for event in events:
        ev = EBEvent(event)
        evs.append(ev)
    return evs


def getAttandeesEmailsForEvent(event):
    response = executeGet("/events/" + event.id + "/attendees/")
    attendees = response.json()['attendees']
    ebAttandees = []
    for attandee in attendees:
        ebAttandees.append(EBAttandee(attandee))
    return ebAttandees


class EBEvent(object):
    """__init__() functions as the class constructor"""

    def __init__(self, event=None):
        self.name = event['name']['text']
        self.id = event['id']
        self.startDate = event['start']['utc']
        self.endDate = event['end']['utc']

    def __repr__(self):
        return self.printEvent()

    def __str__(self):
        return self.printEvent()

    def printEvent(self):
        return json.dumps({'name': self.name, 'id': self.id, 'startDate': self.startDate, 'endDate': self.endDate})


class EBAttandee(object):
    """__init__() functions as the class constructor"""

    def __init__(self, attandee=None):
        profile = attandee.get('profile')
        self.name = profile.get('name')
        self.id = attandee.get('id')
        self.email = profile.get('email')
        self.cell_phone = profile.get('cell_phone')
        self.status = attandee.get('status')

    def __repr__(self):
        return self.printAttendee()

    def __str__(self):
        return self.printAttendee()

    def printAttendee(self):
        return json.dumps({'name': self.name, 'email': self.email, 'cell_phone': self.cell_phone, 'status': self.status, 'id': self.id})


if __name__ == "__main__":
    for event in getEvents():
        print(event)
        print(getAttandeesEmailsForEvent(event))
