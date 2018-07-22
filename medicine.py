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
def medicine():
    print ("I'm in the medicine  method")
    res = {
        "speech": "Explore the world of medicine & get the best knowledge from edX",
        "displayText": "Explore the world of medicine & get the best knowledge from edX",
        "data" : {
        "facebook" : [
               {
                "text": "Explore the world of medicine & get the best knowledge from edX"
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
                                   "title" : "Medicine in the Digital Age",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/course_tn-378x225.jpg",
                                   "subtitle" : "Future of healthcare is connected, patient-centered & social",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/faf09f27",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Improving Global Health",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/2f5692de-8f38-466c-b4fa-3e8fe42df639-52fe23944f8d.small.jpg",
                                   "subtitle" : "A course by Harvard on a very televant topic",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/750b0d82",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Health Coaching for Patient Care",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/4b6dff6a-1c49-4763-a711-4cf48e0ef418-d53d19821271.small.jpg",
                                   "subtitle" : "Learn essential coaching techniques to assist patients",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8d7a0eb3",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Chronic Disease Treatment",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/28d102b4-52f7-438f-8579-be6acd2bb13a-774465513560.small.jpg",
                                   "subtitle" : "Learn specific lifestyle medicine treatment protocols",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/17b12924",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Managing Addiction",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/addictionx-managing_addiction-378x225.jpg",
                                   "subtitle" : "Understand how to recognize addiction",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/1a092eb8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Cellular Brain Mechanism",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/cellular-mechanisms-of-brain-function_378x225.jpg",
                                   "subtitle" : "A mechanistic description of mammalian brain function",
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
                                   "title" : "Life with Diabetes",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/a68e19c6-7557-425b-b14e-7e3bd0a7b5c5-1a208b1830ef.small.png",
                                   "subtitle" : "Learn how to confidently manage your diabetes",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/cf0996b0",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Human Anatomy",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/861d399c-f33a-461b-88e6-f03b20553dee-400ae8a57fe2.small.jpg",
                                   "subtitle" : "The first MOOC to teach Human Anatomy",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/feae0a73",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Applied Biostatistics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/med101x-course_card_image-378x225.jpg",
                                   "subtitle" : "Learn data analysis for medical research",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/abbaee5a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Fundamentals of Clinical Trials",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/hms214x_378x225.jpg",
                                   "subtitle" : "Harvard teaches about clinical trials",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8644e45e",
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