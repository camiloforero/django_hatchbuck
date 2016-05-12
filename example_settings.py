# encoding:utf-8
from __future__ import unicode_literals

#The API key to be used with Hatchbuck
API_KEY = "LXJBY1F2NVRaaWZZLUZBRlk3SXFVZWJtNHF0aURta20tdTNDa0JHcEljRTE1"

#The following fields are taken from the Lookup Table Keys in https://app.hatchbuck.com/Account/WebAPI

#The contact status that new users will have
NEW_CONTACT_STATUS = "Q0F3dXo4LVZnbjVUZHhjTUxEb0pOM0l1NjhzWlRFXzk1bzhVbjZ3eFE4STE1" #Lead

#The default email type new users will have.
NEW_CONTACT_EMAIL_TYPE = "bU5PNVFaZTBJTGUtMUtjR2F4bFJWblhKU2Y4ZW1DVWFyTzBaTHQxTmpZVTE1" #Other


#THis is for only AIESEC: here are the different supported interaction types, and their associated tags
INTERACTION_TAGS = {
    'registered':'VXp1YTRrdy1hQkc5ZTMxQ2wyd0JldDVjOEEycWpBUXBmXzJKclVTbzRRdzE1',
    'contacted':'RGFMck40M0NvMURiY1FoRzlqT3dEWjdad1ZRdnJ3N0g2RERBYzVIa1UwdzE1',
    'applied':{
        'GCDP':'Y0tJVkxhY1JDY19jZ1RHejF0ejg5akliNVpyU19VcmNKd1dSWTJjb3NBODE1',
        'GIP':'dFJZWWwwVW1lYW1uLVNjSm5vMEpIaV9hUXJGeXJmQkl3b0dhOEZnTnBYbzE1',
        },
    'accepted':{
        'GCDP':'WVVoUzhEUGZYQkRqOGlVenlHN3pFWnVSWHc5OUlrU0R4eTZLZ2g3Y3ptRTE1',
        'GIP':'YUFUeGMzUUU3S3VjNjBFYkVjOFZ0TGRGTFBKTEdxbk5Ya2hwTGpqNHRZWTE1',
        },
    'an_signed':{
        'GCDP':'Rl84aUQ3YTZGZVpreFN3QXF3VU5vd2dWMGNVOEM2eldNRnMteVRwbFgxZzE1',
        'GIP':'Vy1RLUtFdEtHSnJkcm1PeXowS2xFQnRyN19BQnd1b3VXZmltakFNbXRIMDE1',
        },
    'approved':{
        'GCDP':'OFlkYVhzT0J0WUZXanRUblczWUNENDcxUTExT0RSWGRHUllFb0hyaWhJYzE1',
        'GIP':'VkRfUzJPVFlRaW9yMENubXVHc3pkcXFONnNNNW0zTHQyVmVFcUlfVjlqQTE1',
        },
    'realized':{
        'GCDP':'VHFRNlJPcWlCSmswNlM2d3VnR1ZOT1BWMHdCREtEb1ZXWGY4UmNnUTlwTTE1',
        'GIP':'VVV6TXdKdjYtdmwyejRjdFVkNnF2eGtncl85Q0F2andmNzNxWXV5WnhrazE1',
        },
    }

CUSTOM_FIELD_TAGS = {
    'EXPA_ID':'NHBOYlE2Y0FsUHVmdHQtalppanVvcW5idkViYnQzb3IwcU9qbFhOLTdIRTE1',
    'LC':'MnZGaURHNGpVZTFlV01Xblh2T0ZCN2NSU3BkVXN0Wmg3WExxUHl5T2dRRTE1',
}
