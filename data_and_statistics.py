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
def data_and_statistics():
    print ("I'm in the data_and_statistics  method")
    res = {
        "speech": "Data scientists are one the highest paid people in the world. Why not you?",
        "displayText": "Data scientists are one the highest paid people in the world. Why not you?",
        "data" : {
        "facebook" : [
               {
                "text": "Data scientists are one the highest paid people in the world. Why not you?"
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
                                   "title" : "Math for Machine Learning",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/fcaea676-0280-4af8-a913-7192af58c643-a4aa14027c75.small.png",
                                   "subtitle" : "Learn essential math for Machine Learning & AI",
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
                                   "title" : "Multi-Object Tracking - Automobiles",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/1ddf76b7-93e0-4c7f-9ff6-75e99897159d-3a6cf5889b90.small.jpg",
                                   "subtitle" : "Learn how to localize and track autonomous vehicles",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/1ea1f5ae",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Data Science",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/c654bfe1-69ba-4a2b-8be1-9acb2e846855-2111845aec83.small.jpg",
                                   "subtitle" : "Harvard University offers best class Data Science course",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e16ad055",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Big Data Analytics Using Spark",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/bannerrevised_4_378x225.jpg",
                                   "subtitle" : "Learn how to analyze large datasets using Spark",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/9dd0eec6",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Mobile Application Experiences",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/building-mobile-experiences-378x225_0.jpg",
                                   "subtitle" : "MIT presents a complete life-cycle of Mobile Apps",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6f620491",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "IoT Programming and Big Data",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/f4ce8928-2ca9-47f0-bc53-804769ffe095-3eaeb6ffaaf4.small.jpg",
                                   "subtitle" : "How you need Big Data to your IoT designs",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/4ad28045",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Social Network Analysis",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/sna_378x225.jpg",
                                   "subtitle" : "Learn how to conduct a social network analysis",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c13b73af",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Predictive Analysis",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/featured-card/qm901x-about_page_image-318x210a.jpg",
                                   "subtitle" : "Master the tools of predictive analytics - IIMB",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a3038773",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Case Studies in Functional Genomics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/statistics-and-r-for-the-life-sciences_378x225.jpg",
                                   "subtitle" : "Explore data analysis of genomic info - Harvard",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2efa399a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Statistics and R",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/statistics-and-r-for-the-life-sciences_378x225.jpg",
                                   "subtitle" : "statistical concepts & R to analyze Life Science data - Harvard",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/3766444a",
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