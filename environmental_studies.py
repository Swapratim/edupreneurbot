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
def environmental_studies():
    print ("I'm in the environmental_studies  method")
    res = {
        "speech": "Know your environment and advance your career. Browse the best courses out there.",
        "displayText": "Know your environment and advance your career. Browse the best courses out there.",
        "data" : {
        "facebook" : [
               {
                "text": "Know your environment and advance your career. Browse the best courses out there."
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
                                   "title" : "The Climate Energy Challenge",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/9146946f-1859-481b-9552-3d1271146826-d6f69cd6b03d.small.jpg",
                                   "subtitle" : "Learn more about the science behind climate change",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/632abc41",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Introduction to Environmental Science",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/intro_to_environmental_science_378x225.jpg",
                                   "subtitle" : "A scientific study of the natural world",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8dfd1a8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Sustainable Energy Capstone",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/engycap-banner-378.jpg",
                                   "subtitle" : "Learn via Sustainable Energy MicroMasters program",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e1c050e4",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Low Emission Technologies and Supply",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/engy3x-banner-378.jpg",
                                   "subtitle" : "Analyse the role of current energy supply systems",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/22c451fa",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Flood Risk Management",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/frmx-378x225.jpg",
                                   "subtitle" : "Understand the fundamentals of flood risk management",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/cff9949a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Globalization and Sustainable Development",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/403142dc-dc49-41f9-a5e4-da355d2ede90-935038f40d06.small.png",
                                   "subtitle" : "Learn the nexus between globalisation & sustainable development",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c333f9d1",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Co-Creating Sustainable Cities",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/course_image_v20170607-378225.jpg",
                                   "subtitle" : "Learn how citizen’s co-creation can make world more sustainable",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f789c4eb",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Antarctica: From Geology to Human History",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ice101x_course_listing_thumbnail.jpg",
                                   "subtitle" : "Take a virtual field trip to Antarctica",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d2ba607",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Effects of Radiation",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/radio101x-378x225.jpg",
                                   "subtitle" : "Learn more about effects of Radiation",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/955cd640",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Natural Disasters",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/natural-disasters378x225.jpg",
                                   "subtitle" : "Learn the science behind different types of natural disasters",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c80efc22",
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