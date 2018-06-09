#!/usr/bin/env python

from __future__ import print_function
from future import standard_library
import requests
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import json
import os
import sys
#import urlparse
from urllib.parse import urljoin
#import emoji
import pprint

from flask import Flask
from flask import request, render_template
from flask import make_response
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
import professional_courses
import popular_courses
from popular_courses.computer_science import computer_science
from popular_courses.data_and_statistics import data_and_statistics

# Flask should start in global layout
context = Flask(__name__)
# Facbook Access Token
ACCESS_TOKEN = "EAAZAAAauLaJYBAAZC4wh4KypFPHnjyjGzYnd0UCo35hD37efh8nC43nZC0wpZCaOs9XZC36VUNFI2cxM89RYDjoTWlrDQvHwY54Cgkq27epEshVHlWCk6Bs58DK0SEimuCZBvZC5TUg4cGK1TZAKqJ9B7zCCK7qlwgmVzJcbCAVnAQZDZD"

#************************************************************************************#
#                                                                                    #
#    All Webhook requests lands within the method --webhook                          #
#                                                                                    #
#************************************************************************************#
reqContext = None
# Webhook requests are coming to this method
@context.route('/webhook', methods=['POST'])
def webhook():
    global reqContext
    print (request.get_json(silent=True, force=True))
    reqContext = request.get_json(silent=True, force=True)
    print("webhook---->" + reqContext.get("result").get("action"))

    if reqContext.get("result").get("action") == "input.welcome.edwin":
       return welcome()
    elif reqContext.get("result").get("action") == "showpopularcategories":
       return showpopularcategories()
    elif reqContext.get("result").get("action") == "professionalcourses":
       return professional_courses.professionalcourses()
    elif reqContext.get("result").get("action") == "professionalcertificates":
       return professional_courses.professionalcertificates()
    elif reqContext.get("result").get("action") == "careeradvancement":
       return professional_courses.careeradvancement()
    elif reqContext.get("result").get("action") == "micromastersprograms":
       return professional_courses.micromastersprograms()
    elif reqContext.get("result").get("action") == "advancedskillsetcourses":
       return professional_courses.advancedskillsetcourses()
    elif reqContext.get("result").get("action") == "popularcourses":
       return popular_courses.popularcourses()
    elif reqContext.get("result").get("action") == "computerscience":
       return computer_science.computerscience()
    elif reqContext.get("result").get("action") == "data_and_statistics":
       return data_and_statistics.data_and_statistics()
    else:
       print("Good Bye")

 
#************************************************************************************#
#                                                                                    #
#   This method is to get the Facebook User Deatails via graph.facebook.com/v2.6     #
#                                                                                    #
#************************************************************************************#

def welcome():
    data = request.json
    global first_name
    print (data)
    if data is None:
        return {}
    #entry = data.get('originalRequest')
    platform = data.get('originalRequest').get('source')
    print ("PLATFORM -->" + platform)

    if platform == "facebook":
       id = data.get('originalRequest').get('data').get('data').get('sender').get('id')
       print ("id :" + id)
       fb_info = "https://graph.facebook.com/v2.6/" + id + "?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=" + ACCESS_TOKEN
       print (fb_info)
       result = urllib.request.urlopen(fb_info).read()
       print (result)
       data = json.loads(result)
       first_name = data.get('first_name')
       print ("FACEBOOK: First Name -->" + first_name)

       
    speech2 = "I'm Edwin - your Academic Virtual Professor."
    speech3 = "I'll help you explore online courses from world's best universities to boost your career."
    res = {
          "speech": speech2,
          "displayText": speech2,
           "data" : {
             "facebook" : [
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
                                   "title" : "Hello! " + first_name + "!",
                                   "image_url" : "https://cdn-images-1.medium.com/max/1366/0*V6bjHlIV81dWUSWp.",
                                   "subtitle" : "Welcome to online world of Digital Learning!"
                                 } 
                           ]
                       } 
                   }
                },
                 {
                    "sender_action": "typing_on"
                  },
                 {
                 "text": speech2
                  },
                 {
                 "text": speech3
                  },
                 {
                  "text": "So, let's start. Shall we?",
                  "quick_replies": [
                 {
                  "content_type": "text",
                  "title": "Yeah Sure",
                  "payload": "Yeah Sure",
                  "image_url": "http://gdurl.com/eNYq"
                 },
                 {
                  "content_type": "text",
                  "title": "No Thanks",
                  "payload": "No Thanks",
                  "image_url": "http://gdurl.com/uViQ"
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
    print (r)
    return r

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    print ("Data.........")
    print (data)
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

#************************************************************************************#
#                                                                                    #
#             Edwin - Show popular course categories to users                        #
#                                                                                    #
#************************************************************************************#

def showpopularcategories():
    otherplatformstatement = "Great! I'll ask two questions only. Then only I can precisely tell whether you need a VISA or NOT to travel your destination country."
    res = {
        "speech": "Great! I'll ask two questions only",
        "displayText": "Great! I'll ask two questions only",
        "data" : {
        "facebook" : [
               {
                "text": "Wise choice " + first_name + ". Add certificates to your CV and shine at your workplace."
               },
              {
                    "sender_action": "typing_on"
              },
              {
                 "text": "From professionals to students - I offer the right courses to choose within."
              },
              {
                    "sender_action": "typing_on"
              },
              {
                  "text": "Choose any of the below categories:",
                  "quick_replies": [
                 {
                  "content_type": "text",
                  "title": "Professional Courses",
                  "payload": "Professional Courses",
                  "image_url": "http://uploads.webflow.com/560a7ccceb20834648665497/560a7ccceb20834648665546_icone-formation-ligne.png"
                 },
                 {
                  "content_type": "text",
                  "title": "Popular Courses",
                  "payload": "Popular Courses",
                  "image_url": "https://www.deltalearn.in/public//course_files/no_course_image.png"
                  },
                 {
                  "content_type": "text",
                  "title": "Science Courses",
                  "payload": "Science Courses",
                  "image_url": "https://cdn2.iconfinder.com/data/icons/energy-technology-flat/2048/274_-_Atom-128.png"
                  },
                 {
                  "content_type": "text",
                  "title": "Arts Courses",
                  "payload": "Arts Courses",
                  "image_url": "https://www.lmc.ac.uk/images/logos/Art.jpg"
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



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting APPLICATION on port %d" % port)
    context.run(debug=True, port=port, host='0.0.0.0')