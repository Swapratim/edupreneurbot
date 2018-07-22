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
def economics_and_finance():
    print ("I'm in the economics_and_finance  method")
    res = {
        "speech": "Transform your career by learning economics & finance edX courses",
        "displayText": "Transform your career by learning economics & finance edX courses",
        "data" : {
        "facebook" : [
               {
                "text": "Transform your career by learning economics & finance edX courses"
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
                                   "title" : "Entrepreneurship in Emerging Economics",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/387c5b5b-ef7f-43b9-b9b5-4163f3c74a49-aa50d2a80cbb.small.jpg",
                                   "subtitle" : "Masterpiece course by Harvard to tackle social problems",
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
                                   "title" : "Introduction to foreign Exchange(FX)",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/4f061507-8a82-407e-a83f-c72ae102b768-183ac67743e1.small.jpg",
                                   "subtitle" : "Introductory trading conventions of foreign exchange markets",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/13ab7176",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Brokerage Operations",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/bopc.pc1_.1x.jpg",
                                   "subtitle" : "Learn about brokerage operations",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/7d91f799",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "AP Microeconomics",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/a086516d-a287-4d49-8af7-b8b1ecb5dd33-61417e36506c.small.jpg",
                                   "subtitle" : "MIT presents introductory microeconomics",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/313ec547",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "AP Macroeconomics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ap_macro_378x225.jpg",
                                   "subtitle" : "Introduction to macroeconomics",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/87731878",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to FinTech",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/15923a19-7f31-4767-a7a0-73da8886f7b8-897ace251e72.small.jpg",
                                   "subtitle" : "Learn about innovations transforming finance",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/b0f59157",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Cybersecurity Fundamentals",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/cyber501x_image_378x225.jpg",
                                   "subtitle" : "Learn cybersecurity fundamentals",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/74975cbf",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Mortgage Backed Securities",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/mbs1.pc1x_378x225.jpg",
                                   "subtitle" : "Learn about mortgage-backed securities",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/52b459b3",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Risk Management Prof. Cert.",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/rmpc.pc6x_378x225.jpg",
                                   "subtitle" : "Learn Risk Management, critical for your career growth",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/1654c2e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Healthcare in India",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/c0d711dc-8926-4814-a8e2-f4a35aed9333-ce8d8af80cde.small.png",
                                   "subtitle" : "Learn about contradictions & challenges that define Indian healthcare",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/293711ca",
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