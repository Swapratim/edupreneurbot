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
def computerscience():
    print ("I'm in the computerscience*************####&&&  method")
    res = {
        "speech": "Do you know that computer science & IT are hot career topics right now",
        "displayText": "Do you know that computer science & IT are hot career topics right now",
        "data" : {
        "facebook" : [
               {
                "text": "Do you know that computer science & IT are hot career topics right now"
               },
               {
                    "sender_action": "typing_on"
               },
               {
                "text": "Explore the most money making popular courses"
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
                                   "title" : "Robotics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/robo2x_378x225.jpg",
                                   "subtitle" : "Vision Intelligence & Machine Learning",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a06e249a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Computational Thinking",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/6.00.2x_computational_thinking_homepage378x225.jpg",
                                   "subtitle" : "Data Science course offered by MIT",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d10bf051",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "UX Design: From Concept to Wireframe",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/40ad6d8a-edb8-40d3-a695-71c82503368a-24dcc3f567df.small.jpg",
                                   "subtitle" : "University of Michigan offers UX design process course",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6317fe63",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Java Programming",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/java-course-378x225_0.jpg",
                                   "subtitle" : "Learn fundamental elements of Java programming ",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/15632da2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "AWS Developer: Deploying to AWS",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/6152449b-250c-45ee-8ed7-53d0670f33c6-5c9b91b62a9c.small.jpg",
                                   "subtitle" : "Learn about AWS development from AWS experts",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f8f99b57",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "IT Support: Cloud Fundamentals",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/774b88de-f0e7-4d48-9868-67d2a20bb699-c950f9e1c005.small.jpg",
                                   "subtitle" : "Learn about Cloud fundamentals from Microsoft",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/97b56c0c",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Principles of Machine Learning",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/af583b4b-d869-4abc-be94-44b4146edf94-6049ca23cee9.small.jpg",
                                   "subtitle" : "Get insights from machine learning models - Microsoft",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e285776c",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to OpenStack",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/cf35dad9-31cb-4786-a06a-2fa942d612bc-bb080939d70d.small.png",
                                   "subtitle" : "Get an in-depth primer on leading cloud computing platform",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e5399528",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Infrastruture As a Code",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/7ec0b9d3-2f29-4c50-a611-5e16de0f4b1c-5f66edab5699.small.png",
                                   "subtitle" : "Learn skills for automating infrastructure as a code",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ddc74bca",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "DevOps for Mobile Apps",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/82106a52-c72a-4693-9431-134ecc5994cd-054faeabe67e.small.png",
                                   "subtitle" : "How to build, test, and deploy mobile apps in a DevOps environment ",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/fc77e59",
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