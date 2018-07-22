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
        "speech": "Everyone needs some level of mathematics to progress better in any field",
        "displayText": "Everyone needs some level of mathematics to progress better in any field",
        "data" : {
        "facebook" : [
               {
                "text": "Everyone needs some level of mathematics to progress better in any field. You would lik the list for sure."
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
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/0876df69-2866-4428-9fc3-a97d8d0cf81e-50ac34f93c9c.small.jpg",
                                   "subtitle" : "Fundamental concepts of mathematical probability",
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
                                   "image_url" : "https://i.ytimg.com/vi/io8JSc5q3VA/maxresdefault.jpg",
                                   "subtitle" : "Explore astronomy and Einstein’s theory of relativity",
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
                                   "title" : "Essential Math for AI",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/fcaea676-0280-4af8-a913-7192af58c643-a4aa14027c75.small.png",
                                   "subtitle" : "Learn Machine Learning and AI from Microsoft",
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
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/16e7e19f-9036-4916-a1c8-2b799b502212-b6ccea6595b7.small.jpg",
                                   "subtitle" : "Learn linear algebra and link it to matrix software development",
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
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/mat117_banner.jpg",
                                   "subtitle" : "Credit-eligible college level math course from ASU",
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
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/206x_378x225.jpg",
                                   "subtitle" : "Learn graphs usage to assemble millions of pieces of DNA",
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
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/d65b671f-d3ff-444f-aa3c-41ded325e111-43dd55e266c1.small.jpg",
                                   "subtitle" : "Apply mathematics to solve real-life problems",
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
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/62467d39-05f3-4453-aee0-46cf5781c10d-a7ac373ab047.small.png",
                                   "subtitle" : "This is a class about awe-inspiring issues from MIT",
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
                                   "title" : "Computational Neuroscience",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/d9db31e0-a833-427b-b2f3-77b5b926cf13-b1200e143d1a.small.jpg",
                                   "subtitle" : "Explore theoretical neuroscience to analyze the collective dynamics",
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
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/41e295ce-a84b-4952-a9a7-fa613201d896-fd70d93486b2.small.jpg",
                                   "subtitle" : "Prepare for Introductory Calculus courses",
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