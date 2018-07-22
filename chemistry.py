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
#   CHEMISTRY COURSE CATEGORY - SHOWS MAJOR CATEGORIES EACH WITH 10 ITEMS            #
#                                                                                    #
#************************************************************************************#
def chemistry():
    print ("I'm in the chemistry  method")
    res = {
        "speech": "Boost your career with the best courses & diploma on Chemistry",
        "displayText": "Boost your career with the best courses & diploma on Chemistry",
        "data" : {
        "facebook" : [
               {
                "text": "Boost your career with the best courses & diploma on Chemistry"
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
                                   "title" : "Medicinal Chemistry",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/babef812-bef4-4daf-96a9-226d044ebf3c-68c870bfc696.small.jpg",
                                   "subtitle" : "Gain a better understanding of the drug discovery process",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5a158c0d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Quantum Mechanics of Molecular Structures",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/quantum-mechanics-of-molecular-structures_378x225.jpg",
                                   "subtitle" : "Learn Molecular Structures and Quantum Mechanics",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5698c37b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Solid State Chemistry",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/3.091x-course_card_image-378x225.jpg",
                                   "subtitle" : "Learn chemical principles by examining materials",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/3cc8c20d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Industrial Biotechnology",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/bio_home_378x225.jpg",
                                   "subtitle" : "Learn the basics of sustainable processing",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/cba6755a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Preparing for CLEP Chemistry",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/apchem.1x_banner-378x225.jpg",
                                   "subtitle" : "CLEP Chemistry MOOC",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2044a4fb",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Principles of Biochemistry",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/896f6184-731a-4dae-9e53-ef7a83e5606d-d7284e36f4d8.small.jpg",
                                   "subtitle" : "Explores the molecules of life with Harvard Course",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ef1a4c4b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Metabolomics in Life Sciences",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/metab101x_378.jpg",
                                   "subtitle" : "Learn about metabolomics principles",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/60e9e7a7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Cement Chemistry",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/378x225_vignettecement.jpg",
                                   "subtitle" : "Learn the basics of cement chemistry",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e4f0a42e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Science in Art: The Chemistry of Art Materials",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/t001x-378x225.jpg",
                                   "subtitle" : "Learn the chemistry behind the visual arts - Triniy College",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/898203c0",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Global Warming Science",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/global_warming_378x225.jpg",
                                   "subtitle" : "Learn about earth’s climate system from MIT course",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/588ac61f",
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