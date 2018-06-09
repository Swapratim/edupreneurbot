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
def physics():
    print ("I'm in the physics  method")
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
                                   "title" : "Astrophysics: Exploring Exoplanets",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e303a440",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Plasma physics: Introduction",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d895f2aa",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Mechanics",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/df0854b2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Effective Field Theory",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f2acc268",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Quantum Mechanics and Quantum Computation",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ab8cccfa",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Space Mission Design and operation",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c399a4f2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Nuclear Reactor Physics Basics",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a835cf30",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Atomic and Optical Physics",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/bf266be3",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Flight Vehicle Aerodynamics",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5a01c29d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Flight Vehicle Aerodynamics",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5a01c29d",
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