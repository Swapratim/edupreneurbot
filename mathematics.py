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
def mathematics():
    print ("I'm in the mathematics  method")
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
                                   "title" : "Introduction to Probability",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8e8c954",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Relativity & Astrophysics",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/60b1bdd3",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Essential Mathematics for Artificial Intelligence",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/7fbf3fe4",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Linear Algebra - Foundations to Frontiers",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/3932b894",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "College Algebra and Problem Solving",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2b140932",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Graph Algorithms in Genome Sequencing",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/bc97ec81",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Mathematical Modelling Basics",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/729c86c6",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Paradox and infinity",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/9a40229d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Computational Neuroscience: Neuronal Dynamics of Cognition",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/383c4092",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Pre-University Calculus",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/57d30915",
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