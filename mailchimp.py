#!/usr/bin/env python

import os
from mailchimp3 import MailChimp
import json

class MailChimpClient:
    def __init__(self):
        self.client = MailChimp(mc_api = os.environ['MAILCHIMP_TOKEN'],
                                mc_user = 'vykta')

    # def create_list(self, data = list):
    #     client.lists.create(data = data)
    #
    # def create_member(self, id = list_id, data = member):
    #     client.lists.members.create(list_id = list_id, data = data)

    list = {
        'name': 'Test List',
        'contact': {
            'company': 'Isha',
            'address1': 'Coimbatoire',
            'address2': 'India',
            'city': 'India',
            'state': 'Coimbatoire',
            'zip': '30308',
            'country': 'India'
        },
        'permission_reminder': 'Do it',
        'campaign_defaults': {
            'from_name': 'Isha',
            'from_email':'Isha@isha.com',
            'subject':'',
            'language':'en'
        },
        'email_type_option': True
    }

    list_id = 'f802ccd729'

    member = {'email_address': 'vyncem@gmail.com', 'status': 'subscribed'}

    subscriber_hash = 'vyncem@gmail.com'

def pertty_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))

if __name__ == '__main__':
    mailchimp = MailChimpClient()
    client = mailchimp.client
    ## members
    # pertty_print(client.lists.members.delete(list_id=mailchimp.list_id,
    #     subscriber_hash=mailchimp.subscriber_hash))
    # pertty_print(client.lists.members.create(list_id=mailchimp.list_id, data=mailchimp.member))
    # pertty_print(client.lists.members.all(list_id=mailchimp.list_id, get_all=False))

    ## lists
    # pertty_print(client.lists.get(list_id=mailchimp.list_id))
    # pertty_print(client.lists.delete(list_id=mailchimp.list_id))
    # pertty_print(client.lists.all(get_all=True))
    # pertty_print(client.lists.create(data=mailchimp.list_id))

    ## campaings
    # pertty_print(client.campaigns.all(get_all=True))
    # pertty_print(client.campaign_folders.all(get_all=False))
