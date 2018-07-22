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
def health_and_safety():
    print ("I'm in the health_and_safety method")
    res = {
        "speech": "Healthy habits & safety measures can boost your life. Learn the secrets behind them",
        "displayText": "Healthy habits & safety measures can boost your life. Learn the secrets behind them",
        "data" : {
        "facebook" : [
               {
                "text": "Healthy habits & safety measures can boost your life. Learn the secrets behind them"
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
                                   "title" : "Injury Prevention for Children & Teens",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/59b08778-66cc-4902-8b9c-3844fb04e01f-89045b78cf64.small.jpg",
                                   "subtitle" : "Learn how to avoid injury- #1 cause of death among children and teens",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a771b080",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Health Coaching for Patient Care",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/4b6dff6a-1c49-4763-a711-4cf48e0ef418-d53d19821271.small.jpg",
                                   "subtitle" : "Learn essential coaching techniques to assist patients with lifestyle modifications",
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
                                   "title" : "Social Welfare Policy and Service",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ssw_micromaster_530_socialwelfarepolicy_378x225.jpg",
                                   "subtitle" : "Learn about the history of social welfare policy, services & work profession",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a656cc30",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Forensic Engineering: Learning from Failures",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/forensic-engineering_378x225.jpg",
                                   "subtitle" : "Learn how failures can lead to social betterment",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5d765b61",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Entrepreneurship in Emerging Economies",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/387c5b5b-ef7f-43b9-b9b5-4163f3c74a49-ff159d73a091.small.jpg",
                                   "subtitle" : "Explore how entrepreneurship and innovation tackle complex social problems",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/870fc1db",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Nutrition and Health: Food Risks",
                                   "image_url" : "https://www.wur.nl/upload_mm/7/6/0/ccf6214a-278c-4fbb-ace7-a8f41570cd4b_54145643-4d1f-4c49-aa86-4acaf9af5caa_nutr103x_587px_9687d60f_490x330.jpg",
                                   "subtitle" : "Learn about bacteria, pesticides and health hazards present in food",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6c8a39a7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Social Work: Research",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ssw_micromaster_522_socialworkresearch_378x225.jpg",
                                   "subtitle" : "Learn about the importance of an evidence-based approach in social work",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a4e566fc",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Science and Practice of Yoga",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/yoga_378x225.jpg",
                                   "subtitle" : "Learn to practice yoga & bring mindfulness into your everyday life",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a32d00c9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Positive Behavior Support for Young Children",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/featured-card/positive-behavior-for-children-380x168.jpg",
                                   "subtitle" : "Learn to promote social-emotional development for young children",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/21376368",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "eHealth – Opportunities and Challenges",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ehealth-opportunities-and-challenges_378x225.jpg",
                                   "subtitle" : "An introduction to the eHealth field featuring practical examples",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c87cb06b",
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