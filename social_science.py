#!/usr/bin/env python

from __future__ import print_function
from future import standard_library
import requests
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import json
import os
import sys

from flask import Flask
from flask import request, render_template
from flask import make_response

#************************************************************************************#
#                                                                                    #
#   POPULAR COURSE CATEGORY - SHOWS MAJOR CATEGORIES EACH WITH 10 ITEMS              #
#                                                                                    #
#************************************************************************************#
def social_science():
    print ("I'm in the social_science  method")
    res = {
        "speech": "Social Science provides opportunity to make you grow a powerful career.",
        "displayText": "Social Science provides opportunity to make you grow a powerful career.",
        "data" : {
        "facebook" : [
               {
                "text": "Social Science provides opportunity to make you grow a powerful career. See the below courses."
               },
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
                                   "title" : "Global Media, War & Technology",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/11748849-1cf7-44fb-9d08-6ca7bf8f6c72-3b03d98a2046.small.jpg",
                                   "subtitle" : "Explore the intersection of IT, conflict & resistance",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/9dc70dd8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Psychology of Personal Growth",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/07d7ae26-cc26-43df-a427-40488e08abcb-10f16a091c54.small.jpg",
                                   "subtitle" : "Learn to understand personal growth",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/1d29bdb2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Adaptive Leadership in Development",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/aebacc3c-b6af-467c-996a-b3298b1f9dcc-2c9d2ec93416.small.jpg",
                                   "subtitle" : "Gain the skills to be an adaptive leader",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/47f0891f",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Psychology of Criminal Justice",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/479e2d74-9414-4939-9e52-937cf1685720-f12c0c17fccd.small.jpg",
                                   "subtitle" : "Learn how it can improve criminal justice system",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/4c89bd9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Science of Parenting",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/parenting_101x_378x225.jpg",
                                   "subtitle" : "Learn more about sensible parenting",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f513c6f8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Science of Everyday Thinking",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/01bf8f79-a1fc-4481-8a37-d313a781298b-b427e99b7993.small.jpg",
                                   "subtitle" : "Learn how to think, argue & choose better",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/29990dba",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Corporate Social responsibility(CSR)",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/f531e896-cbd8-4c7b-90e5-2ac9cb04bbf4-8b3623f12a50.small.png",
                                   "subtitle" : "A rich and exciting series of topics to learn",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/1989187",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Urban Infrastructure Management",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/urban_infrastructure_big-378225.jpg",
                                   "subtitle" : "Learn the principles of managing urban infrastructure systems",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2cf137d6",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Behavioral Economics in Action",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/e676bed5-ecd1-420b-81f7-606570ead24f-9c0be3b17d8e.small.jpg",
                                   "subtitle" : "Learn behavioural economics to change behaviours & improve welfare",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/61c0a9e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Comparative Political Systems",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/f1d975ef-6981-464e-9d29-52b2136e05a8-11c47205f149.small.jpg",
                                   "subtitle" : "Insights needed to understand Democracy today",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8ba81410",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }
                           ]
                       } 
                   }
                },
                {
                  "text": "Get me to previous step",
                  "quick_replies": [
                 {
                  "content_type": "text",
                  "title": "Back",
                  "payload": "BackToHome",
                  "image_url": "https://maxcdn.icons8.com/Share/icon/Arrows/reply_all_arrow_filled1600.png"
                  }
                  ]
                }
             ]
          } 
       };
    print (res)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r