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
def engineering():
    print ("I'm in the engineering  method")
    res = {
        "speech": "Engineering is the base of any society. Advance your career with it today.",
        "displayText": "Engineering is the base of any society. Advance your career with it today.",
        "data" : {
        "facebook" : [
               {
                "text": "Engineering is the base of any society. Advance your career with it today."
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
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/robo3x_378x225.jpg",
                                   "subtitle" : "Learn how to design and engineer complex, dynamic robotic systems",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/871a03f9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Entrepreneurship for Engineers",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/d4f93be9-ad38-4137-b18c-ecb28ce60a17-e997fa02966b.small.jpg",
                                   "subtitle" : "A toolbox for building a technology startup from idea to execution",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/16674080",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Aeronautical Engineering",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/fd2b565f-8730-4264-957a-3fbfa1b649b0-b8bdbe7976ac.small.jpg",
                                   "subtitle" : "Learn about aeronautics, aerodynamics and flight mechanics",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d13e011f",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Electric Cars: Technology",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/ee11fadf-c75b-48ec-ae68-e40e44adef29-be1b444480d2.small.png",
                                   "subtitle" : "In-depth understanding of the technology behind electric cars",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/adf3b5a2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Solar Energy: Capstone Project",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/cd76ec33-e5aa-49fe-b7b8-169ced7fc85d-22b7b035a185.small.jpg",
                                   "subtitle" : "Solar Energy Engineering MicroMasters program",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5c51b475",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Supply Chain Management",
                                   "image_url" : "https://www.edx.org/sites/default/files/supply-chain-micromasters_378x.jpg",
                                   "subtitle" : "Earn aDiploma from MIT’s #1 ranked Program to advance your career",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/71460946",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Leadership for Engineers",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/lfe101x-new_course_card_image-378x225.jpg",
                                   "subtitle" : "Learn how to lead in a technology-driven world",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8e6ef128",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Nuclear Reactor Physics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/mephi005x-course-banner_378x225.jpg",
                                   "subtitle" : "Familiar with Nuclear Reactor Physics",
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
                                   "title" : "Quantum Cryptography",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/tnw_qucryptox_378x225.jpg",
                                   "subtitle" : "Learn how quantum communication provides security",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f987b528",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Industrial Biotechnology",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/bio_home_378x225.jpg",
                                   "subtitle" : "Basics of sustainable processing for biobased products",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/cba6755a",
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