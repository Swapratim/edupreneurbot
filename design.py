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
def design():
    print ("I'm in the design  method")
    res = {
        "speech": "Design is a great way to make a living. It can be fulfilling, helpful and satisfying.",
        "displayText": "Design is a great way to make a living. It can be fulfilling, helpful and satisfying.",
        "data" : {
        "facebook" : [
               {
                "text": "Design is a great way to make a living. It can be fulfilling, helpful and satisfying."
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
                                   "title" : "Circular Economy",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/02d007b2-609c-4526-af7e-f9962458aaa8-7c39aba55dc5.small.png",
                                   "subtitle" : "Contribute to a sustainable economic system by design approaches",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/45003c31",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Design Practice in Business",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/ide_dpb001x_edx_378x225.jpg",
                                   "subtitle" : "Essentials of design practice for developing new business opportunities & innovation",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e068cc84",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Design Thinking Fundamentals",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/think501x_image-378225.jpg",
                                   "subtitle" : "Learn how user-centered approach & design-thinking principles inspire innovative ideas",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/b1943fcc",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Make Your Own App",
                                   "image_url" : "http://blog.edx.org/wp-content/uploads/2016/03/Mobile-Apps.jpg",
                                   "subtitle" : "Learn to build your own mobile apps & softwares",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ea36a369",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Introduction to Game Design",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/checkers-378x225.jpg",
                                   "subtitle" : "MIT offers a practical introduction to game design concepts",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a232dc6e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Design Educational Technology",
                                   "image_url" : "https://mitopencourseware.files.wordpress.com/2014/09/11-132x-blog.jpg",
                                   "subtitle" : "MIT presents theories & technologies underlying development",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/b6d67f4b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Basic 3D Modeling using Blender",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/skani101x_banner-378225.jpg",
                                   "subtitle" : "IIT Bombay offers basic 3D modeling skills",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d0ccb13d",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "UX Design",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/b6045388-0f3e-4c4b-b87b-34197eb1349e-efa14c44e2f8.small.jpg",
                                   "subtitle" : "Learn about the UX design process from wireframes to prototypes",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/22d15424",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Gamification for Business",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/bb7079e3-c0b5-4fd1-926a-06af590536e3-0afcb587e2fe.small.jpg",
                                   "subtitle" : "Learn how accessibility plays into gamification fundamentals, creating efficiency in business ",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/af0b385",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "CyberSecurity in IoT",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/aea32c0b-0d17-4ead-8996-a880b32aa433-36f8a49ae011.small.jpg",
                                   "subtitle" : "Learn about the security and privacy implications of the IoT",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ed14acd5",
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