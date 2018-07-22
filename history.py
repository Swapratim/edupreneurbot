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
def history():
    print ("I'm in the history method")
    res = {
        "speech": "History helps us understand change and how the society we live in came to be",
        "displayText": "History helps us understand change and how the society we live in came to be",
        "data" : {
        "facebook" : [
               {
                "text": "History helps us understand change and how the society we live in came to be"
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
                                   "title" : "Religion, Conflict and Peace",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/47faf271-5dce-455e-8308-9bb903f1d697-c80435496084.small.jpg",
                                   "subtitle" : "Explore the diverse and complex roles the religions play",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d222b1eb",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Discover Political Science",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/8203b2ca-f5db-4a16-ae2b-02ca1df8aa2a-61d2a64bd2e2.small.jpg",
                                   "subtitle" : "Understand current political stakes",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8ec807ad",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Ancient Egyptian Civilization",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/bax1_image_378x225.png",
                                   "subtitle" : "Learn about the history, women, and architecture of ancient Egypt",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5f62eabf",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Democracy and Development",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/17.571x_378x225.jpg",
                                   "subtitle" : "Learn about the drivers of democratic development in Africa",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c808d32a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Antarctica: From Geology to Human History",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ice101x_course_listing_thumbnail.jpg",
                                   "subtitle" : "Take a virtual field trip to Antarctica",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d2ba607",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Einstein Revolution",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/emc2x_thumbnail_378x225.jpg",
                                   "subtitle" : "Learn about Albert Einstein’s lifelong interests",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/3e96ecff",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Western Civilization: Ancient and Medieval Europe",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/hst102_banner_0.jpg",
                                   "subtitle" : "Learn about the origins and development of Western societies",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f1c672bc",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Science of Religion",
                                   "image_url" : "http://aboutislam.net/wp-content/uploads/2017/03/Similarities-Between-Scientific-and-Religious-Extremism.jpg",
                                   "subtitle" : "Explore the journey to the origins of religion and spirituality",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6682aabd",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Saving Schools: Reforming the U.S. Education System",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/education-course-378x225_0.png",
                                   "subtitle" : "An overview of past, present, and future of US education system",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/39ef89e7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Conquest of Space",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/af05174d-613f-4a54-9c6e-8298a26417e3-6100db4c3b78.small.jpg",
                                   "subtitle" : "Explore the history of space travel",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/b9803414",
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