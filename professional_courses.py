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
#   PROFESSIONAL COURSE CATEGORY - SHOWS FOUR MAJOR CATEGORIES EACH WITH 10 ITEMS    #
#                                                                                    #
#************************************************************************************#
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
                                        "title": "Explore Courses",
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
                                        "title": "Explore Courses",
                                        "payload": "Career Advancement"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Micromasters Programs",
                                   "image_url" : "http://blog.edx.org/wp-content/uploads/2017/06/micromasters-edx-hero.jpg",
                                   "subtitle" : "Earn professional degrees from top universities",
                                   "buttons": [{
                                        "type": "postback",
                                        "title": "Explore Courses",
                                        "payload": "Micromasters Programs"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Advanced Skillset Courses",
                                   "image_url" : "https://6lli539m39y3hpkelqsm3c2fg-wpengine.netdna-ssl.com/wp-content/uploads/2017/01/shutterstock_life_science-405x228.jpg",
                                   "subtitle" : "Earn professional degrees from top universities",
                                   "buttons": [{
                                        "type": "postback",
                                        "title": "Explore Courses",
                                        "payload": "Advanced Skillset Courses"
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
                  "title": "Back to Home",
                  "payload": "BacktoWelcomeContent",
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

#************************************************************************************#
#                                                                                    #
#   PROFESSIONAL CERTIFICATES - THIS CONTAINS 10 COURSE ITEMS                        #
#                                                                                    #
#************************************************************************************#
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
                                        "title": "Enroll for Free"
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
                                        "title": "Enroll for Free"
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
                                        "title": "Enroll for Free"
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
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Foundations of Data Science",
                                   "image_url" : "https://www.accttwo.com/hubfs/data-science-blog.jpg?t=1524256234833",
                                   "subtitle" : "Datascience is within top paid jobs. Earn a degree from Berkeley today.",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/efe59bb4",
                                        "title": "Enroll for Free"
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
                                        "title": "Enroll for Free"
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
                                        "title": "Enroll for Free"
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
                                        "title": "Enroll for Free"
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
                                        "title": "Enroll for Free"
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
                  "payload": "BackToProfessionalCourses",
                  "image_url": "https://maxcdn.icons8.com/Share/icon/Arrows/reply_all_arrow_filled1600.png"
                  }
                  ]
                }
             ]
          } 
       };
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


#************************************************************************************#
#                                                                                    #
#   CAREER ADVANCEMENT - THIS CONTAINS 10 COURSE ITEMS                               #
#                                                                                    #
#************************************************************************************#
def careeradvancement():
    print ("I'm in the careeradvancement method")
    res = {
        "speech": "Constant upgrade is the mantra to be the top in your career. I'll help you to reach that goal.",
        "displayText": "Constant upgrade is the mantra to be the top in your career. I'll help you to reach that goal.",
        "data" : {
        "facebook" : [
               {
                "text": "Constant upgrade is the mantra to be the top in your career. I'll help you to reach that goal."
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
                                   "title" : "Design Thinking",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/think503x_image-378225.jpg",
                                   "subtitle" : "Learn how ideas transform into solutions through iteration and validation with best practices for communicating it to stakeholders",
                                   "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "http://tidd.ly/233060da",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Astrophysics : Exploring Exoplanets",
                                   "image_url" : "https://www.reader.gr/sites/default/files/astrofysiki.jpg",
                                   "subtitle" : "Explore the mysteries of exoplanets - planets around other stars - Australian National University",
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
                                   "title" : "Autonomous Mobile Robots",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/c2750912-8e29-426f-91b8-c03b0dd9ee8f-5afb8449c402.small.jpg",
                                   "subtitle" : "Basic concepts and algorithms for locomotion, perception, and intelligent navigation - University of Zurich",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2a7c5a70",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Programming with Python for Data Science",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/838396a5-1110-4e49-8bb3-55536924ab90-2957bde4a93f.small.jpg",
                                   "subtitle" : "Learn Machine Learning & Data Visualization - from Microsoft",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/831377cd",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Microsoft Excel for the Data Analyst",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/703521a6-b2e3-4b5a-813a-1e70504e13ab-4d95beaff4a9.small.jpg",
                                   "subtitle" : "Learn Excel - one of the most popular data analysis tools from Microsoft",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/6a774a5f",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Cloud Computing for Enterprises",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/cloudcomputing-course1image_378x225.jpg",
                                   "subtitle" : "Understand cloud computing technologies and how they can increase business productivity and effectiveness",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c71cdbc9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Analyzing & Visualizing Data with Power BI",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/1bda401c-840c-4316-b3b6-e9357f26ad92-b86d4db4dcf5.small.jpg",
                                   "subtitle" : "Power BI, a powerful cloud-based service that helps data scientists visualize and share insights from their data",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/62f5913e",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "IELTS Academic Test Preparation",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/d61d7a1f-3333-4169-a786-92e2bf690c6f-e5d57786f124.small.jpg",
                                   "subtitle" : "Prepare for the IELTS Academic tests in this comprehensive, self-paced course - University of Queensland",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/4a3a7e00",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Predictive Modelling in Learning Analytics",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/pm_378x225.jpg",
                                   "subtitle" : "Predictive models in educational data mining and learning analytics - University of Texas",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/5384934a",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "The Science of Parenting",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/parenting_101x_378x225.jpg",
                                   "subtitle" : "UC San Diego presents scientific findings that can help you make sensible, informed parenting decisions",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/f513c6f8",
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
                  "payload": "BackToProfessionalCourses",
                  "image_url": "https://maxcdn.icons8.com/Share/icon/Arrows/reply_all_arrow_filled1600.png"
                  }
                  ]
                }
             ]
          } 
       };
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


#************************************************************************************#
#                                                                                    #
#   MICROMASTERS PROGRAMS - THIS CONTAINS 10 COURSE ITEMS                            #
#                                                                                    #
#************************************************************************************#
def micromastersprograms():
    print ("I'm in the micromastersprograms method")
    res = {
        "speech": "This is a series of graduate level courses from top universities designed to advance your career.",
        "displayText": "This is a series of graduate level courses from top universities designed to advance your career.",
        "data" : {
        "facebook" : [
               {
                "text": "Micromasters Program is a series of graduate level courses from top universities designed to advance your career."
               },
              {
                    "sender_action": "typing_on"
              },
              {
                "text": "They provide deep learning in a specific career field and are recognized by employers for their real job relevance."
               },
              {
                 "attachment" : {
                   "type" : "template",
                     "payload" : {
                      "template_type" : "generic",
                       "elements" : [ 
                                 {
                                   "title" : "Artificial Intelligence",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/course_image_csmm_101x_378x225.jpg",
                                   "subtitle" : "Columbia University will give you a rigorous, advanced, professional, graduate-level foundation in Artificial Intelligence",
                                   "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "http://tidd.ly/67462b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Internet of Things (ioT)",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/51821230-63f3-49bb-86af-0d3073a28648-c1f54677af8b.small.jpg",
                                   "subtitle" : "Gain an understanding of what the IoT is and the requirements to design your own IoT solutions",
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
                                   "title" : "Digital Product Management",
                                   "image_url" : "http://blog.edx.org/wp-content/uploads/2017/07/Untitled-design-13.png",
                                   "subtitle" : "Advance your career as a Digital Product Manager - from Boston University",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e2ba4dfd",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Corporate Innovation",
                                   "image_url" : "https://www.edx.org/sites/default/files/corpinn-landing-page_378x225.jpg",
                                   "subtitle" : "Learn how to apply state-of-the-art methods to foster innovation and sustained growth in your organization",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/dcee1df5",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Business Leadership",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/buslead5-banner-large-378225.jpg",
                                   "subtitle" : "Advance your career by learning how to effectively lead complex, modern organisations",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/caab7861",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Sustainable Energy",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/engycap-banner-378.jpg",
                                   "subtitle" : "Apply the knowledge and skills you acquired through in-depth assessment - from The University of Queensland",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/e1c050e4",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Cloud Computing",
                                   "image_url" : "https://www.edx.org/sites/default/files/cloud_computing_378x225_2.jpg",
                                   "subtitle" : "Gain expertise in one of the hottest fields in IT, as you learn how to design, implement, and manage cloud computing systems",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/1b9324da",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Bioinformatics",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/72c27b2f-3419-430f-a28f-10dbc7120457-f65614c7500b.small.jpg",
                                   "subtitle" : "Learn how to analyze biological big data to unlock the next big biotech discovery - University of Maryland",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/cb4f5d08",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "CyberSecurity",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/153cedc6-d710-41c4-bd39-58363ef0f7db-cfe55cbb7d26.small.jpg",
                                   "subtitle" : "Launch your career in a high demand industry that projects 2 million new jobs annually",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/d924a7cf",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Data Science Essentials",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/6922fad4-4a1b-4064-8644-48030e5bbbc7-098558fd6e34.small.jpg",
                                   "subtitle" : "Explore data visualization and exploration concepts with experts from MIT and Microsoft",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/1503510b",
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
                  "payload": "BackToProfessionalCourses",
                  "image_url": "https://maxcdn.icons8.com/Share/icon/Arrows/reply_all_arrow_filled1600.png"
                  }
                  ]
                }
             ]
          } 
       };
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

#************************************************************************************#
#                                                                                    #
#   ADVANCED SKILLSET COURSES - THIS CONTAINS 10 COURSE ITEMS                        #
#                                                                                    #
#************************************************************************************#
def advancedskillsetcourses():
    print ("I'm in the advancedskillsetcourses method")
    res = {
        "speech": "If you are ready to push your career a step ahead, you are at the right place.",
        "displayText": "If you are ready to push your career a step ahead, you are at the right place.",
        "data" : {
        "facebook" : [
               {
                "text": "If you are ready to push your career a step ahead, you are at the right place."
               },
              {
                    "sender_action": "typing_on"
              },
              {
                "text": "Equip yourself with ost demanding advanced skillset and earn a high salary."
               },
              {
                 "attachment" : {
                   "type" : "template",
                     "payload" : {
                      "template_type" : "generic",
                       "elements" : [ 
                                 {
                                   "title" : "Business Principles and Entrepreneurial Thought",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/00169f68-ff4b-4621-a741-25ba70c98482-69e5133f3217.small.jpg",
                                   "subtitle" : "Learn core business skills and how they intersect with Entrepreneurship of All Kinds® from the #1 business school in Entrepreneurship",
                                   "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "http://tidd.ly/32b345b9",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 }, 
                                 {
                                   "title" : "Fundamentals of Computer Science",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/2c7051ee-6c29-4c90-921c-92112bcfa866-8aea86c230e8.small.jpg",
                                   "subtitle" : "Learn the software engineering essentials for next generation software engineering - from IIT Bombay",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/800182c2",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Food Security and Sustainability",
                                   "image_url" : "https://briandcolwell.com/wp-content/uploads/2016/09/Emerging-Businessedit.jpg",
                                   "subtitle" : "Learn how to feed all people in the world in a sustainable way.",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/546e1dd6",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Corporate Financial Analytics",
                                   "image_url" : "https://www.edx.org/sites/default/files/corporatefinance_coursecard_378px_v2.jpg",
                                   "subtitle" : "Learn to conduct rigorous financial analysis with real-world examples - from University of Michigan",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/c0469ecc",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Essentials for MBA Success",
                                   "image_url" : "https://www.edx.org/sites/default/files/edx_banner_378x225px.jpg",
                                   "subtitle" : "Prepare yourself for success on an MBA program - from Imperial College of London",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/b794c22b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Genomics Data Analysis",
                                   "image_url" : "https://prod-discovery.edx-cdn.org/media/course/image/42f20043-d067-4d4a-8952-d6bb9c60b747-e5ad73fe9b45.small.jpg",
                                   "subtitle" : "Advanced techniques to analyze genomics data using open source software - from Harvard University",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/2b2e4bba",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "IT Project Management",
                                   "image_url" : "https://www.edx.org/sites/default/files/course/image/promoted/fom-ebm04x_378x225.jpg",
                                   "subtitle" : "Become an effective project manager by applying these PM techniques and strategies - University of Washington",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/973aab6b",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Astrophysics : Exploring Exoplanets",
                                   "image_url" : "https://www.reader.gr/sites/default/files/astrofysiki.jpg",
                                   "subtitle" : "Explore the mysteries of exoplanets - planets around other stars - Australian National University",
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
                                   "title" : "Future Cities",
                                   "image_url" : "https://statetechmagazine.com/sites/statetechmagazine.com/files/articles/ST_5g_ThinkstockPhotos-539964528.jpg",
                                   "subtitle" : "Understand a city’s people, components, functions, scales and dynamics",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/44237a71",
                                        "title": "Enroll for Free"
                                    },
                                    {
                                        "type": "element_share"
                                    }]
                                 },
                                 {
                                   "title" : "Anatomy",
                                   "image_url" : "https://www.fairfield.edu/media/main-site/2017-18/images/news/2018/03-march/03-23-18_image_anatomage-table_amb.jpg",
                                   "subtitle" : "Learn the foundations of human anatomy - from University of Michigan",
                                   "buttons": [{
                                        "type": "web_url",
                                        "url": "http://tidd.ly/968d87dc",
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
                  "title": "Back to Home",
                  "payload": "BacktoWelcomeContent",
                  "image_url": "https://maxcdn.icons8.com/Share/icon/Arrows/reply_all_arrow_filled1600.png"
                  }
                  ]
                }
             ]
          } 
       };
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r