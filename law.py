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
def law():
    print ("I'm in the law method")
    res = {
        "speech": "Studying law develops one's understanding of the levers of power in our society",
        "displayText": "Studying law develops one's understanding of the levers of power in our society",
        "data" : {
        "facebook" : [
               {
                "text": "Studying law develops one's understanding of the levers of power in our society"
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
                                   "title" : "Contract Law",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/5f1d3726-e78b-41f9-8e71-b904fddd102e-e5bd837ee3a6.small.jpg",
                                   "subtitle" : "From Trust to Promise to Contract - Learn How",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/1a73b3ce",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Human Rights Law",
                                   "image_url" : "https://www.worldatlas.com/r/w728-h425-c728x425/upload/5e/0d/5e/shutterstock-263354150.jpg",
                                   "subtitle" : "Learn how an individual’s human rights are protected",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/81d49954",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Intellectual Property Law and Policy",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/1af38483-a96c-489d-857a-a1b01c666641-9ae324da5b61.small.jpg",
                                   "subtitle" : "Explore the legal doctrines at the core of innovation economy",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6a0504ef",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "International Law",
                                   "image_url" : "http://3.bp.blogspot.com/-zCwCqCJvzdI/VG-E8B6LkbI/AAAAAAAAAEQ/-O7EHQHqIIs/s1600/MAIN_SUB_LJ2.jpg",
                                   "subtitle" : "You’ll master the language and institutions of international law",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/717e00b8",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Project Finance: Funding Projects Successfully",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/f8d26e31-a9ea-4891-8e4d-ccf3be0e10f2-935f1884326d.small.png",
                                   "subtitle" : "Learn the key strategies used by project managers",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/87c1aec4",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Open Government",
                                   "image_url" : "http://www.osec.doc.gov/opog/images/opengov.jpg",
                                   "subtitle" : "Explore the challenges, benefits and processes that govts face",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/8a6f83d2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Climate Change Law & Policy",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/e3ecabae-0a9a-4893-8b2f-11eb9c86847a-92b35f478457.small.jpg",
                                   "subtitle" : "Learn international laws and policies to combat climate change",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/ce08f600",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Genomic Medicine Gets Personal",
                                   "image_url" : "https://www.genomicseducation.hee.nhs.uk/taught-courses/wp-content/uploads/2017/04/primer-genomic-medicine.jpg",
                                   "subtitle" : "Introduction to genomic medicine",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/22795a62",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Human Rights Defenders",
                                   "image_url" : "https://sviluppofelice.files.wordpress.com/2014/03/freedomfromwarlogo.jpg",
                                   "subtitle" : "Learn about the stories of human rights defenders",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/fd5e92b7",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Legal Risk Management Strategies",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/compliancex-378x225.jpg",
                                   "subtitle" : "Learn about the concept of corporate accountability",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/b0213b1a",
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