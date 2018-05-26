#!/usr/bin/env python

from __future__ import print_function
from future import standard_library
import requests
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import json
import os
import sys
#import urlparse
from urllib.parse import urljoin
import emoji
import pprint

from flask import Flask
from flask import request, render_template
from flask import make_response
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Flask should start in global layout
context = Flask(__name__)
# Facbook Access Token
ACCESS_TOKEN = "EAADSsDjm6gIBANlzUbBmbFLGpNvZBhnZCEw71BSMvwQZCK8n9KjaY5Pf8P5ZAZBlt9mKcLHe2AmU5hgq7XZAc4vedP5ISpyuRIBKuWMvYx6YI6976r5qpZBsI8vSoU4pmqvVqffjNVJuvCttk7EykTb9tUfHWCnjfivwKUZAA1S4WQZDZD"
# Google Sheet Credentials
#CLIENT_ID = "107898040430223609451"
#LIENT_SECRET = '<Client secret from Google API Console>'
#************************************************************************************#
#                                                                                    #
#    All Webhook requests lands within the method --webhook                          #
#                                                                                    #
#************************************************************************************#
reqContext = None
# Webhook requests are coming to this method
@context.route('/webhook', methods=['POST'])
def webhook():
    global reqContext
    reqContext = request.get_json(silent=True, force=True)
    #print(json.dumps(reqContext, indent=4))
    print("webhook---->" + reqContext.get("result").get("action"))
    print ("webhook is been hit ONCE ONLY")
    if reqContext.get("result").get("action") == "input.welcome":
       return welcome()
    else:
       print("Good Bye")

 
#************************************************************************************#
#                                                                                    #
#   This method is to get the Facebook User Deatails via graph.facebook.com/v2.6     #
#                                                                                    #
#************************************************************************************#
nationality = "False"
destinationcountry = "False"
def welcome():
    data = request.json
    print (data)
    if data is None:
        return {}
    #entry = data.get('originalRequest')
    platform = data.get('originalRequest').get('source')
    print ("PLATFORM -->" + platform)

    if platform == "facebook":
       id = data.get('originalRequest').get('data').get('sender').get('id')
       print ("id :" + id)
       fb_info = "https://graph.facebook.com/v2.6/" + id + "?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=" + ACCESS_TOKEN
       print (fb_info)
       result = urllib.request.urlopen(fb_info).read()
       print (result)
       data = json.loads(result)
       first_name = data.get('first_name')
       print ("FACEBOOK: First Name -->" + first_name)

       #####################################################################
       # Opening Google Drive Excel to read and write userbase             #
       # https://www.youtube.com/watch?v=vISRn5qFrkM                       #
       #####################################################################

       scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
       creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
       client = gspread.authorize(creds)
       
       sheet = client.open("Visa CheckBot Global User Database").worksheet("user_table")
       user_table = sheet.get_all_records()
       pp = pprint.PrettyPrinter()
       #print (sheet.row_count)
       pp.pprint (user_table)

       # INSERT USER DETAILS FROM FACEBOOK API
       row = [str(data.get('first_name')), str(data.get('last_name')), str(data.get('gender')), str(data.get('id'))]
       print (row)
       
       # STOP DUPLICACY OF USER DATA
       if str(data.get('id')) in sheet.col_values(4):
          print ("Nothing to print")
       elif str(data.get('id')) not in sheet.col_values(4):
          sheet.insert_row(row)
       
    elif platform == "telegram":
       first_name = data.get('originalRequest').get('data').get('message').get('chat').get('first_name')
       print ("TELEGRAM: First Name -->" + first_name)
    elif platform == "skype":
       first_name = "to Visa CheckBot"
       print ("SKYPE: Within Python")
    elif platform == "slack":
       first_name = "to Visa CheckBot"
       print ("SKYPE: Within Python")
    elif platform == "kik":
       first_name = data.get('originalRequest').get('data').get('from')
       print ("KiK: Within Python")
       
    speech1 = "This is your one stop solution for visa related enquiry. "
    res = {
          "speech": speech1,
          "displayText": speech1,
           "data" : {
             "facebook" : [
                   {
                    "sender_action": "typing_on"
                  },
                  {
                 "attachment" : {
                   "type" : "template",
                     "payload" : {
                      "template_type" : "generic",
                       "elements" : [ 
                                 {
                                   "title" : "Welcome " + first_name + "! ",
                                   "image_url" : "http://gdurl.com/eDd3J",
                                 } 
                           ]
                       } 
                   }
                },
                 {
                    "sender_action": "typing_on"
                  },
                 {
                 "text": speech1
                  },
                 {
                  "text": "So, let's start. Shall we?",
                  "quick_replies": [
                 {
                  "content_type": "text",
                  "title": "Yeah Sure",
                  "payload": "Yeah Sure",
                  "image_url": "http://gdurl.com/eNYq"
                 },
                 {
                  "content_type": "text",
                  "title": "No Thanks",
                  "payload": "No Thanks",
                  "image_url": "http://gdurl.com/uViQ"
                   }
                  ]
                 }
                ],
            "telegram": {
                 "parse_mode": "markdown",
                 "text": "[​​​​​​​​​​​](https://goo.gl/eAfyr9) Welcome " + first_name + "! " + speech1 + "So let's start, shall we?",
                 "reply_markup": { 
                   "inline_keyboard": [ 
                        [{ "callback_data": "Yeah Sure", "text": "Yeah Sure" }], 
                        [{ "callback_data": "No Thanks", "text": "No Thanks" }] 
                       ] 
                   }
                },
           "slack": {
                 "text": speech1,
                 "attachments": [
                   {
                    "fallback": "You are unable to proceed",
                    "callback_id": "intro_block",
                    "color": "#3AA3E3",
                    "image_url": "https://goo.gl/eAfyr9",
                    "text": "So, let's start. Shall we?",
                    "attachment_type": "default",
                    "actions": [
                         {
                            "name": "Yeah Sure",
                            "text": "Yeah Sure",
                            "type": "button",
                            "value": "Yeah Sure"
                         },
                         {
                            "name": "No Thanks",
                            "text": "No Thanks",
                            "type": "button",
                            "value": "No Thanks"
                         }
                     ]
                  }
                ]
              },
           "kik": {
                 "type": "text",
                 "body": "Welcome " + first_name + "! " + speech1 + "So let's start, shall we?",
                 "keyboards": [
                        {
                    "type": "suggested",
                    "responses": [
                        {
                            "type": "text",
                            "body": "Yeah Sure"
                        },
                        {
                            "type": "text",
                            "body": "No Thanks"
                        }
                      ]
                    }
                 ]
              }
          },
        "messages": [
        {
          "type": 4,
          "platform": "skype",
          "payload": {
            "skype": {
              "type": "message",
              "text": "Hi",
              "attachments": [
                {
                  "contentType": "application/vnd.microsoft.card.hero",
                  "content": {
                    "title": "Welcome to Visa CheckBot",
                    "subtitle": "Your one stop solution for Visa check",
                    "images": [
                      {
                        "url": "https://goo.gl/eAfyr9"
                      }
                    ],
                   "buttons": [{
                            "type":"postBack",
                            "title": "Yeah Sure",
                            "value": "Yeah Sure"
                    },
                    {
                            "type":"postBack",
                            "title": "No Thanks",
                            "value": "No Thanks"
                    }]
                  }
                }
              ]
            }
          }
        }
       ],
     };
    print (res)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    print (r)
    return r

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    print ("Data.........")
    print (data)
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

#************************************************************************************#
#                                                                                    #
#   Tell USER about Visa Check Bot - ASK TWO QUESTIONS                               #
#                                                                                    #
#************************************************************************************#


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting APPLICATION on port %d" % port)
    context.run(debug=True, port=port, host='0.0.0.0')