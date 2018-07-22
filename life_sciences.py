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
def life_sciences():
    print ("I'm in the life_sciences  method")
    res = {
        "speech": "Biology can be the most interesting & career upgrading subject in your life.",
        "displayText": "Biology can be the most interesting & career upgrading subject in your life.",
        "data" : {
        "facebook" : [
               {
                "text": "Biology can be the most interesting & career upgrading subject in your life."
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
                                   "title" : "Super-Earths And Life",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/2b375f3f-4498-4130-b7ec-1d6a1b03ffc5-9e24c9969708.small.jpg",
                                   "subtitle" : "Harvard presents how & where search for alien life",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2791beeb",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Principle of Biochemistry",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/896f6184-731a-4dae-9e53-ef7a83e5606d-d7284e36f4d8.small.jpg",
                                   "subtitle" : "In depth Biochemistry study by Harvard",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ef1a4c4b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Stat Analysis in Bioinformatics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/bioinformatics3image_378x225.jpg",
                                   "subtitle" : "Learn how to analyze biological big data to locate genes",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8a18190d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "DNA: The Genetic Code",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/f7b3a875-ac4b-499b-8a58-49826453cfc3-8fb3d986d9ad.small.jpg",
                                   "subtitle" : "Explore DNA structure",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6f2fbeaa",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Evolution of Human Sociality",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/000x-course_image-378x225a.jpg",
                                   "subtitle" : "Learn about the origins of human beings and primatology",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/938d6a5",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Cellular Mechanisms of Brain Function",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/cellular-mechanisms-of-brain-function_378x225.jpg",
                                   "subtitle" : "Learn mammalian brain function at the level of individual nerve cells",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2e3d16fc",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Biomedical Imaging",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/494a5714-605c-420a-bff0-a9550a6cdcbe-c41e30563c8c.small.jpg",
                                   "subtitle" : "Discover how medical imaging technologies are complementary",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/878412a6",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Big Bang and & Origin of Chemical Elements",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/123e28f1-5eae-4663-9198-769b98430c92-b40c2a0acefd.small.jpg",
                                   "subtitle" : "Explore the Big Bang through Nobel Lectures",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/81150de",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Neuronal Dynamics",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/907185f6-0f8e-4e58-9099-4521428a4712-de9bedd78ca8.small.jpg",
                                   "subtitle" : "Learn mathematical neuron models",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a8fdeb04",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Principles of Synthetic Biology",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/20.305x-course_image-378x225_0.jpg",
                                   "subtitle" : "Learn how to engineer biological systems and program organisms",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e63f2570",
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