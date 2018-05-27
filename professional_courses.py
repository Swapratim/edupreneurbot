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

def professionalcourses():
    print ("I'm in the PROFESSIONAL COURSE method")
    res = {
        "speech": "Excel your career with recent advancements around",
        "displayText": "Excel your career with recent advancements around",
        "data" : {
        "facebook" : [
               {
                "text": "Excel your career with recent advancements around. Select the latest trendy categories & explore."
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
                                   "title" : "Professional Certificates",
                                   "image_url" : "http://www.businesslinkuae.com/wp-content/uploads/2016/02/Professional-Company-Formation-Dubai.jpg",
                                   "subtitle" : "Best guidance to reach top at your career",
                                   "buttons": [{
                                        "type": "postback",
                                        "title": "Explore top courses",
                                        "payload": "Professional Certificates"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Career Advancement",
                                   "image_url" : "https://www.manager.bg/sites/default/files/mainimages/0f94af1.jpg",
                                   "subtitle" : "Learn most high paid skills and give a boost to your career",
                                   "buttons": [{
                                        "type": "postback",
                                        "title": "Explore top courses",
                                        "payload": "Career Advancement"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Micromasters Program",
                                   "image_url" : "http://blog.edx.org/wp-content/uploads/2017/06/micromasters-edx-hero.jpg",
                                   "subtitle" : "Earn professional degrees from top universities",
                                   "buttons": [{
                                        "type": "postback",
                                        "title": "Explore top courses",
                                        "payload": "Micromasters Program"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Advanced Skilled Courses",
                                   "image_url" : "https://6lli539m39y3hpkelqsm3c2fg-wpengine.netdna-ssl.com/wp-content/uploads/2017/01/shutterstock_life_science-405x228.jpgg",
                                   "subtitle" : "Earn professional degrees from top universities",
                                   "buttons": [{
                                        "type": "postback",
                                        "title": "Explore top courses",
                                        "payload": "Advanced Skilled Courses"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Back",
                                   "image_url" : "https://maxcdn.icons8.com/Share/icon/Arrows/reply_all_arrow_filled1600.png",
                                   "subtitle" : "Get back to previous step",
                                   "buttons": [{
                                        "type": "postback",
                                        "title": "Back",
                                        "payload": "BackToProfessionalCourses"
                                    }]
                                 }
                           ]
                       } 
                   }
                }
             ]
          } 
       };
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def professionalcertificates():
    print ("I'm in the professionalcertificates method")
    res = {
        "speech": "Do you know - you can be within top 1% skilled professional with proper education",
        "displayText": "Do you know - you can be within top 1% skilled professional with proper education",
        "data" : {
        "facebook" : [
               {
                "text": "Do you know - you can be within top 1% skilled professional with proper education"
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
                                   "title" : "Six Sigma & Lean",
                                   "image_url" : "https://www.edx.org/sites/default/files/tum_prof_cert_card_378x225.jpg",
                                   "subtitle" : "Quantitative Tools for Quality & Productivity",
                                   "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6271731b",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "IT Fundamentals",
                                   "image_url" : "https://www.theknowledgeacademy.com/_public/images/categoryClassroom/thumb_1512040567_programmingdatabase-min.jpg",
                                   "subtitle" : "For Business Professionals: Programming",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/4a0c132",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Science of Happiness at Work",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/73484215-4007-48cd-ba90-c945cde6030d-b2e9efe0d29a.small.jpg",
                                   "subtitle" : "Earn degree from University of California, Berkeley",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/10cb3556",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Virtual Reality App Development",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/c887397e-8e7a-417a-a207-893f4a81f168-081c957041f2.small.jpg",
                                   "subtitle" : "VR is the most money-making skill now. Laern it from UCSanDiegoX",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/1374640e",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Foundations of Data Science",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/c887397e-8e7a-417a-a207-893f4a81f168-081c957041f2.small.jpg",
                                   "subtitle" : "Datascience is within top paid jobs. Earn a degree from Berkeley today.",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/efe59bb4",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Product Design & Health",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/5dedf011-dfb5-4ea4-8714-30196590eb52-8abe9f50a87a.small.png",
                                   "subtitle" : "Boost your entrepreunership skills with this course",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6e429f7d",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Digital Marketing",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/7b72aca9-0f77-428a-b6d1-e8aeffe8c89b-710f50a76ceb.small.png",
                                   "subtitle" : "Digital marketing has a bright prospect within global top professionals",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f282ae31",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Corporate Finance",
                                   "image_url" : "https://www.justetf.com/images/news/etf-unternehmensanleihen.jpg",
                                   "subtitle" : "Are you a corporate professional? Then this course is best choice for you.",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/a6f98912",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Business Writing",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/course2_effective_business_writing_-_378225_0.jpg",
                                   "subtitle" : "Brilliant course offer from University of California, Berkeley",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e84d134d",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Soft Skills",
                                   "image_url" : "https://www.edx.org/sites/default/files/softskills_pc_thumbnail-378225.jpg",
                                   "subtitle" : "Sharpen your soft skills via diploma from Rochester Institute of Technology",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/305a694b",
                                        "title": "View Course"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Back",
                                   "image_url" : "https://maxcdn.icons8.com/Share/icon/Arrows/reply_all_arrow_filled1600.png",
                                   "subtitle" : "Get back to previous step",
                                   "buttons": [{
                                        "type": "postback",
                                        "title": "Back",
                                        "payload": "BackToProfessionalCourses"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }
                           ]
                       } 
                   }
                }
             ]
          } 
       };
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r