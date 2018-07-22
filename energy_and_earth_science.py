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
def energy_and_earth_science():
    print ("I'm in the energy_and_earth_science  method")
    res = {
        "speech": "Know how we can live a better future. You can contribute to the future of humankind.",
        "displayText": "Know how we can live a better future. You can contribute to the future of humankind.",
        "data" : {
        "facebook" : [
               {
                "text": "Know how we can live a better future. You can contribute to the future of humankind."
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
                                   "title" : "Energy Within Environmental Constraints",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/3ee3be46-26a9-4594-bd90-1a91386c534a-987dcbc220f2.small.jpg",
                                   "subtitle" : "Learn about energy system and its environmental impacts",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ff6000f5",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Tropical Coastal Ecosystems",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/tropic101x_course_homepage_278x225.jpg",
                                   "subtitle" : "Problems & solutions to manage tropical coastal ecosystems",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8ab103e0",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Deep Earth Science",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/geos101x-intro_to_deep_earth_science_p1-378x225_0.jpg",
                                   "subtitle" : "Learn about nature of Earth’s core, mantle & crust",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8f120510",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Climate Change: Carbon Capture and Storage",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/07721e0e-0ba7-45ad-b82b-1b6abdcb9dba-438a8910567b.small.jpg",
                                   "subtitle" : "Explore the technology to protect our atmosphere from global warming",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d82b808",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Sustainable Energy",
                                   "image_url" : "https://ocw.tudelft.nl/wp-content/uploads/ewi_energyx_edx_header.png",
                                   "subtitle" : "Learn how to make the transition to 100% renewable energy",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/da2e0831",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Greatest Unsolved Mysteries of the Universe",
                                   "image_url" : "https://i.ytimg.com/vi/rcYHbz1PHY0/maxresdefault.jpg",
                                   "subtitle" : "Exploring the biggest mysteries of modern astrophysics",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ce928826",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Geoscience",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/geo101x-course_card12112015-378x225.jpg",
                                   "subtitle" : "Modern Earth Sciences with application to the Geology",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/7425bcf0",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Dinosaur Ecosystems",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/30138fc7-3d0b-4344-979a-895d2544c403-3af13e59d484.small.jpg",
                                   "subtitle" : "How palaeontologists use fossils to reconstruct dinosaur",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8b8c673c",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Sensing Planet Earth - From Core to Outer Space",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/chm003x-course_card_image11202015-378x225_0.jpg",
                                   "subtitle" : "Learn about the crucial tools for measuring and monitoring our planet",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/dd60e5f4",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Solar Energy",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/solar-energy_378x225_0.jpg",
                                   "subtitle" : "Discover the power of solar energy",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/253055f0",
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