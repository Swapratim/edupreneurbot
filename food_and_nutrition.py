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
def food_and_nutrition():
    print ("I'm in the food_and_nutrition method")
    res = {
        "speech": "For a healthy and cretive lifestyle. you must know about food and nutrition",
        "displayText": "For a healthy and cretive lifestyle. you must know about food and nutrition",
        "data" : {
        "facebook" : [
               {
                "text": "For a healthy and cretive lifestyle. you must know about food and nutrition"
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
                                   "title" : "Science & Cooking",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/d37884e7-363e-471b-ad1b-1250b1fdae23-484acb0a4f40.small.jpg",
                                   "subtitle" : "Harvard researchers explore the fundamentals of everyday cooking",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8edad98a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Lifestyle Medicine Core Principles",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/fd2010af-5595-48e6-83ad-98e1e24f1156-ebcabd817c01.small.jpg",
                                   "subtitle" : "Learn key concepts of evidence-based lifestyle therapeutic approaches",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/526598b9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Nutrition and Health",
                                   "image_url" : "https://www.class-central.com/report/app/uploads/2015/09/Nutrition-and-Health-Part-1-Macronutrients-and-Overnutrition.jpg",
                                   "subtitle" : "Learn about malnutrition and micronutrients and how they impact human health",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/9bcf126b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Science of Beer",
                                   "image_url" : "http://blog.edx.org/wp-content/uploads/2018/04/blog-hero.jpg",
                                   "subtitle" : "Discover what's in your beer, how it's made and marketed and the effect",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c3a16dbc",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "World History of Wine",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/0af6995d-ecda-4835-a4fb-a52fa5b3b745-1c64a5058948.small.jpg",
                                   "subtitle" : "Explore wine through the eyes of a historian",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a08ad6bd",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Science of Weight loss",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/2a879208-f559-4f71-b401-dbc8df884334-006d25ebe2e6.small.jpeg",
                                   "subtitle" : "Learn the science behind weight loss and dispel diet and nutrition myths",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/dc4d2174",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Science & Politics of GMO",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/usegen.2x-course_card_image-378x225.jpg",
                                   "subtitle" : "Learn the basics of genetic engineering, biotechnology & GMO",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e4c6eb0",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Science & Cooking",
                                   "image_url" : "https://i.ytimg.com/vi/mC12B2XseqM/maxresdefault.jpg",
                                   "subtitle" : "Harvard researchers explore how traditional and modernist cooking techniques",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/af7e1d8a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Sustainable Food Security",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/04bdf14f-b56d-49b1-80e4-f0ecbd45ce99-e6d7d1800f6e.small.jpg",
                                   "subtitle" : "Learn the basics of food access decision-making",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/514be4a9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Ethics of Eating",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ethics-of-eating_378x225-new.jpg",
                                   "subtitle" : "Explore the ethical issues you confront each time you decide what to eat",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/71916dcf",
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