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
def architecture():
    print ("I'm in the architecture  method")
    res = {
        "speech": "Architecture courses help you to imagine, design and construct the streets and buildings of the future",
        "displayText": "Architecture courses help you to imagine, design and construct the streets and buildings of the future",
        "data" : {
        "facebook" : [
               {
                "text": "Architecture courses help you to imagine, design and construct the streets and buildings of the future"
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
                                   "title" : "The Architectural Imagination",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/8c411679-4105-4de9-8a4c-9c5b3f4a33a6-3b563779dd78.small.jpg",
                                   "subtitle" : "Learn fundamental principles of architecture from Harvard University",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/690eace",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Sustainability in Architecture",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/aaf55a03-04f1-40f9-bb56-e92a9d66f2df-4dee14c0a844.small.jpg",
                                   "subtitle" : "Interdisciplinary course to define sustainability practices in Architecture",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e4b32ba6",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Mechanics of Deformable Structures",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/2.02.1x-378225.jpg",
                                   "subtitle" : "MIT offers study of foundation of Strength of Materials",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2fdcb70",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "A Global History of Architecture",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/4065x_378x225_1.jpg",
                                   "subtitle" : "MIT presents humanity’s rich architectural history",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/9da9ceb7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Urban Design for the Public Good",
                                   "image_url" : "https://d2jzbjey2ol3gs.cloudfront.net/uploads/category/1/image3/normal_architektur_kurs_3.jpg",
                                   "subtitle" : "Dutch approach - how to design landscapes and cities",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/9ba9ad4e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Responsive Cities",
                                   "image_url" : "https://i.ytimg.com/vi/HFklKEffsv4/maxresdefault.jpg",
                                   "subtitle" : "Explore the future of urbanization responsive Cities",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/735db8f7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Ecodesign for Cities and Suburbs",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ecodesign_ubc_378x225.jpg",
                                   "subtitle" : "Learn how ecology can guide urban design to avert environmental disasters",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2e62663e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Modern Japanese Architecture",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/arch101x-course_image-378x225z_0.jpg",
                                   "subtitle" : "Tokyo Tech presents traditional Japanese architecture",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/70b64004",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Vernacular Architecture of Asia",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/the-search-for-vernacular-architecture-of-asia-part-1_378x225.jpg",
                                   "subtitle" : "Search for Vernacular Architecture of Asia by Hong Kong University",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/69d01348",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Smart Cities",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/smartcities_378x225.jpg",
                                   "subtitle" : "Learn how data and information impact the design & sustainability of future cities",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/7ce16bb5",
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
                  "payload": "BackToHomeArtCourses",
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