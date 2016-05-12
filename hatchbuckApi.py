# encoding:utf-8
from __future__ import unicode_literals

import json
import urllib
import requests

from . import settings

class HatchbuckApi(object):
    """
    This class is meant to provide a python interface for interactions with the Hatchbuck API
    """
    BASE_URL = "https://api.hatchbuck.com/api/" #v1/contact?api_key=
    def __init__(self):
        self.api_key = settings.API_KEY

    def _build_query(self, routes, query_params=None, version='v1'):
        if query_params is None:
            query_params = {}
        base_url = self.BASE_URL + "{version}/{routes}?{params}"
        query_params['api_key'] = self.api_key
        return base_url.format(version=version, routes="/".join(routes), params=urllib.urlencode(query_params, True))

    def _add_new_contact(self, email, data):
        """
        This method adds a new contact to Hatchbuck, with the provided email address. Contact status and email type are taken from the module settings.py file.
        Params:
            email: Is the email address of the new contact
            data: All other contact data that will be added to the final request
        """
        if data is None:
            data = {}
        contact = {
            'emails': [{
                'address':email,
                'typeid':settings.NEW_CONTACT_EMAIL_TYPE,
                }],
            'status':{
                #'name':'Lead'
                'id':settings.NEW_CONTACT_STATUS,
                },
            }
        contact.update(data)
        query = self._build_query(['contact'])
        return requests.post(query, json=contact)

    def add_interaction(self, email, interaction, data, subtype=None):
        """
        This method adds a new interaction to Hatchbuck, with the proper information and tags. It receives the same parameters as the internal _add_contact method. If the contact doesn't exist it will create it; if it does, it updates it with the appropriate tag, which can be found in the settings file.
        Params:
            email, data: Same as self._add_new_contact
            interaction: The interaction type, as found in the settings file. Those not there are not supported
        """
        response = self._add_new_contact(email, data)
        if response.status_code == 200 or response.status_code == 400:
            query = self._build_query(['contact', email,'Tags'])
            if subtype:
                interaction_tag = settings.INTERACTION_TAGS[interaction][subtype]
            else:
                interaction_tag = settings.INTERACTION_TAGS[interaction]
            tags = [{
                'id':interaction_tag
                }]
            return requests.post(query, json=tags)
        else:
            print response.json()
            raise Exception("Unkwnown status code: %d" % response.status_code)

    
