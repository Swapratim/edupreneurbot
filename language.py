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
def language():
    print ("I'm in the language  method")
    res = {
        "speech": "Learning a new language benefits cognitive abilities like intelligence and memory",
        "displayText": "Learning a new language benefits cognitive abilities like intelligence and memory",
        "data" : {
        "facebook" : [
               {
                "text": "Learning a new language benefits cognitive abilities like intelligence and memory"
               },
               {
                    "sender_action": "typing_on"
               },
               {
                "text": "But learning a new language can open up opportunity for earning money also!"
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
                                   "title" : "TOEFL Test Preparation",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/ee4f4f12-e6ec-45ac-94df-b90b4b022903-535df2dd3168.small.jpg",
                                   "subtitle" : "The Insider's Guide for guaranteed success",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/529472bb",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "IELTS Academic Test Preparation",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/d61d7a1f-3333-4169-a786-92e2bf690c6f-e5d57786f124.small.jpg",
                                   "subtitle" : "Prepare for the IELTS Academic tests",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/4a3a7e00",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Intermediate Chinese Grammar",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/20000001-378x225_0.png",
                                   "subtitle" : "Learn Chinese grammatical concepts to improve your Chinese",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f927460d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Basic Spanish 1: Getting Started",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/b05291d7-fbff-4520-8371-7ffdcda326c4-a5153fa821d0.small.jpg",
                                   "subtitle" : "Learn Spanish and explore Spanish culture",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8d5ea435",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Italian Language and Culture: Advanced",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/be8b88c1-7bc9-4711-95d4-e7150140c8a2-149660bd4b2f.small.jpg",
                                   "subtitle" : "Improve your language & knowledge of contemporary Italian culture",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a2091381",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Academic & Business Writing",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/ed682cf1-7c11-4417-ac78-e940843cfccc-a97efbb259eb.small.jpg",
                                   "subtitle" : "Barkeley presents an academic and business writing course",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/28907892",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Learn Japanese",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/d6a62265-20c6-47d4-afed-3b6ba2969548-a6964527eea3.small.jpg",
                                   "subtitle" : "Practice pronunciation and improve your spoken Japanese",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e19f06d1",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Sign Language Structure, Learning and Change",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/3be9efa9-3f4b-4c49-9c03-6ac5bff2b80f-c917dd191ad7.small.jpg",
                                   "subtitle" : "Join the history and evolution of American Sign Language",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/b723a869",
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