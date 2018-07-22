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
def music():
    print ("I'm in the music method")
    res = {
        "speech": "Music and memory go hand in hand. Music education is also linked to higher IQ levels :)",
        "displayText": "Music and memory go hand in hand. Music education is also linked to higher IQ levels :)",
        "data" : {
        "facebook" : [
               {
                "text": "Music and memory go hand in hand. Music education is also linked to higher IQ levels :)"
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
                                   "title" : "Introduction to Music Theory",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/239e085d-8118-43bd-bd46-5820e7242151-0b675b6ef6aa.small.jpg",
                                   "subtitle" : "Learn key concepts to create & perform contemporary music",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/302880f7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Vocal Recording Technology",
                                   "image_url" : "https://i4.ytimg.com/vi/TiZzG3nnagc/maxresdefault.jpg",
                                   "subtitle" : "Explore emerging innovations in audio recording & mixing",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2df4acc6",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Sharpen Your Piano Artistry",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/bbc62ad9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Jazz Music",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/music160x-course_card_image-378x225a.jpg",
                                   "subtitle" : "Learn what’s unique about jazz",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/bbc62ad9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Religion and Hip Hop Culture",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/religion_and_hip_hop_culture_378x225.jpg",
                                   "subtitle" : "Learn Hip Hop culture's religious dimensions via musical",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a8a258d7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Creativity and Entrepreneurship",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/f71c0691-559c-4fa9-ab00-d86a3ad56e07-501be9c7eaa4.small.jpg",
                                   "subtitle" : "Learn parallels between creative & entrepreneurial journeys",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a1defb95",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "First Nights: Beethoven's 9th Symphony",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/2dfeaf7e-6edc-4c1f-9a6d-d90a30534639-e170cfd1af44.small.jpg",
                                   "subtitle" : "Learn about Beethoven’s monumental 9th Symphony",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5e9c0503",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "How to Listen to Great Music for Orchestra",
                                   "image_url" : "",
                                   "subtitle" : "",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f00d3b35",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Italian opera",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/dart.mus_.01x-intro_to_italian_opera-378x225.jpg",
                                   "subtitle" : "Explore Italian Opera",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/7bc146a6",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Music Business",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/mb110x_378.jpg",
                                   "subtitle" : "Learn the latest about rapidly changing music industry",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/452a037e",
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