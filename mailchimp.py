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

    # list_id = 'f802ccd729'
    # list_id = 'fb92bf4a53'
    list_id = '88eb930db5'

    member = {'email_address': 'victor.muia@storyful.com', 'status': 'subscribed'}

    # campaign_id = 'a20f061e15'
    campaign_id = '6c25ca5140'

    campaign = {
            'recipients': {
                'list_id': list_id
            },
            'type':'regular',
            'settings': {
                'subject_line':'Thank you',
                'reply_to':'vyncem@gmail.com',
                'from_name':'Isha'
            }
    }

    content = { 'html': '<p>Missed you</p>'}

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
    # pertty_print(client.lists.create(data=mailchimp.list))

    ## campaings
    # pertty_print(client.campaigns.all(get_all=False))
    # pertty_print(client.campaign_folders.all(get_all=False))
    # pertty_print(client.campaigns.create(data=mailchimp.campaign))
    # pertty_print(client.campaigns.get(campaign_id=mailchimp.campaign_id))
    # pertty_print(client.campaigns.delete(campaign_id=mailchimp.campaign_id))

    ## content
    # pertty_print(client.campaigns.content.update(campaign_id=mailchimp.campaign_id, data=mailchimp.content))
    # pertty_print(client.campaigns.content.get(campaign_id=mailchimp.campaign_id))


    ## send
    # pertty_print(client.campaigns.actions.send(campaign_id=mailchimp.campaign_id))


    ## Create a lists
    # pertty_print(client.lists.create(data=mailchimp.list))
    pertty_print(client.lists.get(list_id=mailchimp.list_id))

    ## Add list members
    # pertty_print(client.lists.members.create(list_id=mailchimp.list_id, data=mailchimp.member))
    pertty_print(client.lists.members.all(list_id=mailchimp.list_id, get_all=False))

    ## Replicate a campaign and Update recepients list or Create campaign and content
    # pertty_print(client.campaigns.create(data=mailchimp.campaign))
    pertty_print(client.campaigns.all(get_all=False))
    # pertty_print(client.campaigns.content.update(campaign_id=mailchimp.campaign_id, data=mailchimp.content))
    pertty_print(client.campaigns.content.get(campaign_id=mailchimp.campaign_id))

    ## Send campaign
    # pertty_print(client.campaigns.actions.send(campaign_id=mailchimp.campaign_id))

    ## Report
    pertty_print(client.reports.get(campaign_id=mailchimp.campaign_id))
