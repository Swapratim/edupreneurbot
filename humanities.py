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
def humanities():
    print ("I'm in the humanities  method")
    res = {
        "speech": "If you are an empathetic person and want to build your career upon that this is the right place",
        "displayText": "If you are an empathetic person and want to build your career upon that this is the right place",
        "data" : {
        "facebook" : [
               {
                "text": "If you are an empathetic person and want to build your career upon that this is the right place"
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
                                   "title" : "Introduction to Bioethics",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/11593f6c-042c-42a1-b2aa-c337ceb6f74e-c01f93e11647.small.jpg",
                                   "subtitle" : "Bioethics explores some of the most difficult & fascinating moral challenges",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ca50a2b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Human Rights Defenders",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/c981f823-ae43-4432-8ab7-b919fd318cfd-65990e6653a5.small.jpg",
                                   "subtitle" : "Learn how Amnesty International stands up against injustice",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/fd5e92b7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Global Media, War and Technology",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/11748849-1cf7-44fb-9d08-6ca7bf8f6c72-3b03d98a2046.small.jpg",
                                   "subtitle" : "Explore the intersection of IT, violent conflict, and resistance",
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
                                   "title" : "Leaders in Global Development",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/0c6102e9-b2d7-420d-8f42-a74f9868b70f-92af6e7dff60.small.jpg",
                                   "subtitle" : "Learn key leadership skills, concepts and theories",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/7672de16",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Unlocking Your Employability",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/employ101x-course_card_image11192015-378x225.jpg",
                                   "subtitle" : "Learn how to market your skills to potential employers",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/4b029445",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Working in Teams",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/teams101x-banner.jpg",
                                   "subtitle" : "Learn how to build effective teams",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/939ce348",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Writing for Social Media",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/course3_writing_for_social_media-378225_0.jpg",
                                   "subtitle" : "Learn how to write for social media - Berkeley",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/97e6dcfa",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Effective Business Writing",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/course2_effective_business_writing_-_378225_0.jpg",
                                   "subtitle" : "Learn effective business writing by Berkeley",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/54be9bdf",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Terrorism and Counterterrorism",
                                   "image_url" : "https://d3q6qq2zt8nhwv.cloudfront.net/course/2e31de4294a74730953628a21bcc695a.jpg",
                                   "subtitle" : "The danger of terrorism & how to counter it",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/562de61",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Trends in e-Psychology",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/trends_in_e-psychology-378x225.jpg",
                                   "subtitle" : "E-based promotion of physical, mental and social health",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/3febacd1",
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