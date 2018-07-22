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
def art_and_culture():
    print ("I'm in the art_and_culture  method")
    res = {
        "speech": "If you like to express yourself with a sense satisfaction, then below chosen courses are just for you",
        "displayText": "If you like to express yourself with a sense satisfaction, then below chosen courses are just for you",
        "data" : {
        "facebook" : [
               {
                "text": "If you like to express yourself with a sense satisfaction, then below chosen courses are just for you."
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
                                   "title" : "Grant Writing and Crowdfunding",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/607x_378.jpg",
                                   "subtitle" : "Learn to increase your impact & innovate fundraising and grant writing approaches",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/9e018f1b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Design Theory",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/1f0aa40b-7a5a-4a7d-adbc-99b934b0a714-a78f47d78149.small.jpg",
                                   "subtitle" : "Explore key concepts in the new field of design theory",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/dff6dea9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Poetry in America: Whitman",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/poetry_378x225.jpg",
                                   "subtitle" : "Harvard University offers Whitman's contribution on American poetry",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6ea2b58d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "World History of Modern Wine",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/0af6995d-ecda-4835-a4fb-a52fa5b3b745-1c64a5058948.small.jpg",
                                   "subtitle" : "Explore wine through the eyes of a historian - Trnity College",
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
                                   "title" : "Hollywood; History, Industry, Art",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/penn_hollywood_378x225.jpg",
                                   "subtitle" : "Explore the history of Hollywood - a beautiful journey",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e875f5b8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Social Media",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/3dc13ec0-1749-4dc5-9c5a-f63bc8fa3379-740c5b05566a.small.png",
                                   "subtitle" : "Discover how social media evolved our lives",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2198341a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Great War & Modern Philosophy",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/graphx-course_image-378x225_0.jpg",
                                   "subtitle" : "Learn how First World War & Philosophy impacted each other",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ec3417fb",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Modern Masterpieces of World Literature",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/18833403-d3a4-4b16-9c28-271748847951-a1868dfd9b1e.small.jpg",
                                   "subtitle" : "Examine how great modern writers capture the intricacies of our globalized world",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/67b8ee77",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Inspiring and Motivating Arts and Culture Teams",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/622dca1e-5f75-4cda-ac93-81ca23057797-66c0d3bf5757.small.jpg",
                                   "subtitle" : "Learn critical leadership skills that enable you to inspire and motivate individuals and teams",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e6b4dc8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Pyramids of Giza",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/d32bba34-f516-4116-bf61-9c6b124c3e3c-8e9ab4c8eeec.small.jpg",
                                   "subtitle" : "Harvard University explores archaeology, history, art, and hieroglyphs surrounding Giza",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/b7518b37",
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
                  "payload": "BackToHomeArtCourses",
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