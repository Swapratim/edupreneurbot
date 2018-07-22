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
def communication():
    print ("I'm in the communication  method")
    res = {
        "speech": "Develop strong communication skills for a bright career in any field",
        "displayText": "Develop strong communication skills for a bright career in any field",
        "data" : {
        "facebook" : [
               {
                "text": "Develop strong communication skills for a bright career in any field"
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
                                   "title" : "Teamwork and Collaboration",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/b826a61b-6d2b-42a7-b757-cbcbe8b794c6-0427a4b6c700.small.jpg",
                                   "subtitle" : "Learn effective communication skills to lead, build and motivate your teams",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a854349f",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "English for Journalists",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/cdc1f3db-0242-403f-b338-50805cb8a03d-6b189d5c69a2.small.jpg",
                                   "subtitle" : "Improve your English grammar, vocabulary and writing skills - Berkeley University",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/fd716b04",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Leading with Effective Communication",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/2aaffce0-fa32-416c-a1f6-85ca4835ce65-464e09bba78b.small.jpg",
                                   "subtitle" : "Develop communication skills that bring out the best in you",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/bc82476e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Business Communications",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/business-communication-illustration_378x225.jpg",
                                   "subtitle" : "Learn how to communicate effectively in a business setting",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d9710ab8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Family Business",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/a6aed9da-5b57-4843-987b-ad451393dc7c.small.jpg",
                                   "subtitle" : "Learn how to manage the essential strategies of a family business",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/20739b94",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Digital Branding and Engagement",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/mkt1x-course_image-378x225_0.jpg",
                                   "subtitle" : "Increase brand engagement through creation and distribution of digital contents",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ba82d9d6",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Storytelling in the Workplace",
                                   "image_url" : "http://www.rit.edu/news/lib/filelib/201709/softskills.jpg",
                                   "subtitle" : "Learn how to craft messages and narratives to resonate with your target audience",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5e9f4daa",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Leading High-Performing Teams",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/buslead3-banner-large-378225.jpg",
                                   "subtitle" : "Learn to motivate, engage and empower people to build high performing teams",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/76e8736e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Public Speaking",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/public_speaking_copy-378225.jpg",
                                   "subtitle" : "Build confidence as a speaker by learning how to use simple tools and skills to prepare",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d754efc2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Online Marketing Strategies",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/mkt5x_courseabout_378x225.jpg",
                                   "subtitle" : "Learn about online marketing opportunities & use Internet, social media & digital analytics",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/71f813ff",
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