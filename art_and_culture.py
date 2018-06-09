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
def art_and_culture():
    print ("I'm in the art_and_culture  method")
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
                                   "title" : "Grant Writing and Crowdfunding for Public Libraries",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/9e018f1b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Design Theory",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/dff6dea9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Poetry in America: Whitman",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6ea2b58d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The World History of Modern Wine",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a08ad6bd",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Hollywood; History, Industry, Art",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e875f5b8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Social Media: How Media got Social",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2198341a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Great War and Modern Philosophy",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ec3417fb",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Modern Masterpieces of World Literature",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/67b8ee77",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Inspiring and Motivating Arts and Culture Teams",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e6b4dc8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Pyramids of Giza",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/b7518b37",
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