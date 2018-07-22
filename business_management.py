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
def business_management():
    print ("I'm in the business_management  method")
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
                                   "title" : "Becoming an Entrepreneur",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/launch.x-64f89aa9bf42-378225.jpg",
                                   "subtitle" : "Learn the business skills and startup mindset from MIT",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e8282a10",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Critical Thinking & Problem Solving",
                                   "image_url" : "https://campustechnology.com/~/media/EDU/CampusTechnology/Images/2017/09/20170914softskills.jpg",
                                   "subtitle" : "Be the most successful professional",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/3a40aa3a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Reputation Management in Digital World",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/mkt2_378x225.jpg",
                                   "subtitle" : "How to build organizations' reputation via social media",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/686afdc8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Project Management for Development",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/17e30556-8e90-4005-b59b-0de1a07a1ab4-808ba0342a90.small.png",
                                   "subtitle" : "Learn best practices to manage government projects",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6a10ccc0",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Networking & Interview Skills",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/52cbad0b-c721-4e3d-babd-e63201fd6a57-691ddc941576.small.jpg",
                                   "subtitle" : "Get the job you want with compelling skillsets",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8e634870",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Business & Data Analysis Skills",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/ff6654bb-100f-4c22-8d79-4314ddb4f8fe-5417c04b68dc.small.jpg",
                                   "subtitle" : "Learn key business management skills to grow faster",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ecfb591a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Strategic Management",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/st101x_bannerimage_resize.jpg",
                                   "subtitle" : "Learn how a manager or CEO develops a business strategy - IIMB",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8433b992",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Blockchain for Business",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/95c27f23-9062-4959-9673-de788e07873d-735dd82878e5.small.png",
                                   "subtitle" : "An Introduction to Hyperledger Technologies",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/901b43bb",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Financial Analysis for Decision Making",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/courseimages_0002_finance_378x225.jpg",
                                   "subtitle" : "Learn how to analyze business opportunities for their financial viability",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f262d14e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Project Management Success",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/best_practice_378x225.jpg",
                                   "subtitle" : "Learn how to create an organizational environment ",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e946742",
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