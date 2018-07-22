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
def physics():
    print ("I'm in the physics  method")
    res = {
        "speech": "Physics encompasses the study of the universe from the largest galaxies to the smallest subatomic particles",
        "displayText": "Physics encompasses the study of the universe from the largest galaxies to the smallest subatomic particles",
        "data" : {
        "facebook" : [
               {
                "text": "Physics encompasses the study of the universe from the largest galaxies to the smallest subatomic particles. Learn them now."
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
                                   "title" : "Astrophysics: Exploring Exoplanets",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/astro2x_course_homepage_378x225.jpg",
                                   "subtitle" : "The mysteries of exoplanets - planets around other stars",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e303a440",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Plasma physics",
                                   "image_url" : "https://actu.epfl.ch/image/46663/original/2560x1440.jpg",
                                   "subtitle" : "Learn the basics of plasma",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d895f2aa",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Mechanics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/phys_101.1x-378225.jpg",
                                   "subtitle" : "Learn the physics of mechanics",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/df0854b2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Effective Field Theory",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/eft-378x225.jpg",
                                   "subtitle" : "Great course from MIT on EFT",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f2acc268",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Quantum Computation",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/featured-card/quantum_cs-191x_378x225.jpg",
                                   "subtitle" : "Berkeley presents quantum mechanics & computation",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ab8cccfa",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Space Mission",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/411504b9-ef0f-4656-b6b9-119afffd3ded-041780d0a4a6.small.jpg",
                                   "subtitle" : "Learn the concepts used in the design of space missions",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c399a4f2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Nuclear Reactor Physics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/mephi005x-course-banner_378x225.jpg",
                                   "subtitle" : "Become familiar with nuclear reactor physics",
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
                                   "title" : "Atomic & Optical Physics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/8.422.5x_banner_378x225.jpg",
                                   "subtitle" : "Learn about ultracold atoms and Bose-Einstein Condensate",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/bf266be3",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Flight Vehicle Aerodynamics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/16.110x-course_card_image-378x225.jpg",
                                   "subtitle" : "Learn about aerodynamic analysis of modern aircraft",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5a01c29d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Neuronal Dynamics",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/907185f6-0f8e-4e58-9099-4521428a4712-2bee1e16da15.small.jpg",
                                   "subtitle" : "Learn mathematical neuron models",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/387dbbb6",
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