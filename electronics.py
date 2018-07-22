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
def electronics():
    print ("I'm in the electronics  method")
    res = {
        "speech": "Learning electronics can empower your entrepreneurship opportunities. Have a look",
        "displayText": "Learning electronics can empower your entrepreneurship opportunities. Have a look",
        "data" : {
        "facebook" : [
               {
                "text": "Learning electronics can empower your entrepreneurship opportunities. Have a look"
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
                                   "title" : "Internet of Things (IoT)",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/51821230-63f3-49bb-86af-0d3073a28648-c1f54677af8b.small.jpg",
                                   "subtitle" : "Gain an understanding of what the IoT",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ed799833",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Solar Energy: Photovoltaic Energy Conversion",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ewi_pv1x_378x225.jpg",
                                   "subtitle" : "Understand how solar cells generate electricity",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/7d3026f8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Embedded Systems",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/785cf551-7f66-4350-b736-64a93427b4db-ca6e6a3af96b.small.jpg",
                                   "subtitle" : "Learn about embedded systems & microcontroller",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/3ca54369",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Arduino Programming",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/e391b4dd-ed7e-4aff-b349-7018280ec0f7-08912c1b5a3a.small.jpg",
                                   "subtitle" : "Learn to program an object using basic electronics and Arduino",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f17a7681",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Electric & Conventional Vehicles",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/1428ed1b-d1c4-4a23-9b8c-cb9b858bfecb-d5517cb52ed9.small.jpg",
                                   "subtitle" : "Learn how electric and conventional powertrains work",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/920ec353",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Optical Materials and Devices",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/315bannerimage_part2_378x225.jpg",
                                   "subtitle" : "Learn about the optical materials properties from MIT",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/7eb48d46",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Organic Electronic Devices",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/organic_electronic_devices_378x225.jpg",
                                   "subtitle" : "Use polymer molecules to create next generation electronic devices",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/cb4f1f4",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Fundamentals of Nanoelectronics: Basic Concepts",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/fundamentals-of-nanoelectronics_378x225.jpg",
                                   "subtitle" : "Presents key concepts in nanoelectronics and mesoscopic physics",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/3268a13a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Bioelectricity",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/nano525x-course_image-378x225.jpg",
                                   "subtitle" : "Understand how biological systems generate electrical signals",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6cd83e57",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Hypersonics- Shock Waves to Scramjets",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/hypers301x_course_homepage378x225.jpg",
                                   "subtitle" : "Understand flight at speeds greater than Mach 5",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/363c0882",
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