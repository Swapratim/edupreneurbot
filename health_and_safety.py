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
def health_and_safety():
    print ("I'm in the health_and_safety method")
    res = {
        "speech": "Taking up popular courses is a quick way to accelerate your career",
        "displayText": "Taking up popular courses is a quick way to accelerate your career",
        "data" : {
        "facebook" : [
               {
                "text": "Taking up popular courses is a quick way to accelerate your career."
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
                                   "title" : "Injury Prevention for Children & Teens",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a771b080",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Health Coaching for Patient Care",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8d7a0eb3",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Social Welfare Policy and Service",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a656cc30",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Forensic Engineering: Learning from Failures",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5d765b61",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Entrepreneurship in Emerging Economies",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/870fc1db",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Nutrition and Health: Food Risks",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6c8a39a7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Social Work: Research",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a4e566fc",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Science and Practice of Yoga",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a32d00c9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Positive Behavior Support for Young Children",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/21376368",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "eHealth – Opportunities and Challenges",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c87cb06b",
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