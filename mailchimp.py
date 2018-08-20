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
            'from_email':'mailme@kannanv.com',
            'subject':'',
            'language':'en'
        },
        'email_type_option': True
    }

    # list_id = 'f802ccd729'
    # list_id = 'fb92bf4a53'
    # list_id = '88eb930db5'
    list_id = '4c10b8599c'


    member = {'email_address': 'mailme@kannanv.com', 'status': 'subscribed'}
    # member = {'email_address': 'diva_kar@yahoo.com', 'status': 'subscribed'}
    # member = {'email_address': 'Slokendra@yahoo.com', 'status': 'subscribed'}

    # campaign_id = 'a20f061e15'
    # campaign_id = '6c25ca5140'
    # campaign_id = '2f774e1d1d'
    # campaign_id = '000c5b6ecc'
    # campaign_id = 'b7983b9f60'
    # campaign_id = 'a4a5026aec'
    # campaign_id = '105f831048'
    campaign_id = 'ccde2b5510'

    campaign = {
        "recipients": {
            'list_id': list_id,
            "segment_opts": {
                "conditions": [
                    {
                        "condition_type": "Date",
                        "field": "timestamp_opt",
                        "op": "greater",
                        "value": "last"
                    }
                ],
                "match": "any"
            },
            "segment_text": "new only"
        },
        'type':'regular',
        'settings': {
            "reply_to": "vyncem@gmail.com",
            "subject_line": "Join Isha's Events for World Environment Day, 2018",
            "from_name": "Isha Ireland"
        }
    }

    content = { 'html': '<p>Missed you</p>'}

    subscriber_hash = 'vyncem@gmail.com'

def pretty_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))

if __name__ == '__main__':
    mailchimp = MailChimpClient()
    client = mailchimp.client

    ## Create a lists
    print('### Create List ####')
    # pretty_print(client.lists.create(data=mailchimp.list))
    pretty_print(client.lists.get(list_id=mailchimp.list_id))

    ## Add list members
    print('### Add list members ####')
    # pretty_print(client.lists.members.create(list_id=mailchimp.list_id, data=mailchimp.member))
    pretty_print(client.lists.members.all(list_id=mailchimp.list_id, get_all=False))

    ## Replicate a campaign and Update recepients list or Create campaign and content
    print('### Relipcate campaign ####')
    # pretty_print(client.campaigns.actions.replicate(campaign_id=mailchimp.campaign_id))
    print('### Update recipients list ####')
    # pretty_print(client.campaigns.update(campaign_id=mailchimp.campaign_id, data=mailchimp.campaign))

    print('### Create campaign ####')
    # pretty_print(client.campaigns.create(data=mailchimp.campaign))
    pretty_print(client.campaigns.get(campaign_id=mailchimp.campaign_id))

    print('### Update content ####')
    # pretty_print(client.campaigns.content.update(campaign_id=mailchimp.campaign_id, data=mailchimp.content))
    pretty_print(client.campaigns.content.get(campaign_id=mailchimp.campaign_id))

    ## Send campaign
    print('### Send Campaign ####')
    pretty_print(client.campaigns.actions.send(campaign_id=mailchimp.campaign_id))

    ## Report
    print('### Report ####')
    pretty_print(client.reports.get(campaign_id=mailchimp.campaign_id))


    ## members
    print('### Members ####')
    # pretty_print(client.lists.members.delete(list_id=mailchimp.list_id, subscriber_hash=mailchimp.subscriber_hash))
    # pretty_print(client.lists.members.create(list_id=mailchimp.list_id, data=mailchimp.member))
    # pretty_print(client.lists.members.all(list_id=mailchimp.list_id, get_all=False))

    ## lists
    print('### Lists ####')
    # pretty_print(client.lists.get(list_id=mailchimp.list_id))
    # pretty_print(client.lists.delete(list_id=mailchimp.list_id))
    # pretty_print(client.lists.all(get_all=True))
    # pretty_print(client.lists.create(data=mailchimp.list))

    ## campaings
    print('### Campaigns ####')
    # pretty_print(client.campaigns.all(get_all=True, fields="campaigns.id,campaigns.campaign_defaults"))
    # pretty_print(client.campaigns.all(get_all=True))
    # pretty_print(client.campaign_folders.all(get_all=False))
    # pretty_print(client.campaigns.create(data=mailchimp.campaign))
    # pretty_print(client.campaigns.get(campaign_id=mailchimp.campaign_id))
    # pretty_print(client.campaigns.delete(campaign_id=mailchimp.campaign_id))

    ## content
    print('### Content ####')
    # pretty_print(client.campaigns.content.update(campaign_id=mailchimp.campaign_id, data=mailchimp.content))
    # pretty_print(client.campaigns.content.get(campaign_id=mailchimp.campaign_id))


    ## send
    print('### Send ####')
    # pretty_print(client.campaigns.actions.send(campaign_id=mailchimp.campaign_id))
