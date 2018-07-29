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
import popular_course
#sys.path.insert(0, "/popularCourses")
import computer_science
import data_and_statistics
import business_management
import language
import economics_and_finance
import engineering
import humanities
import life_sciences
import science_courses
import chemistry
import electronics
import environmental_studies
import mathematics
import medicine
import physics
import social_science
import energy_and_earth_science
import art_courses
import architecture
import art_and_culture
import communication
import design
import food_and_nutrition
import health_and_safety
import history
import music
import law

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
       return popular_course.popularcourselist()
    elif reqContext.get("result").get("action") == "computerscience":
       return computer_science.computerscience()
    elif reqContext.get("result").get("action") == "data_and_statistics":
       return data_and_statistics.data_and_statistics()
    elif reqContext.get("result").get("action") == "business_management":
       return business_management.business_management()
    elif reqContext.get("result").get("action") == "language":
       return language.language()
    elif reqContext.get("result").get("action") == "economics_and_finance":
       return economics_and_finance.economics_and_finance()
    elif reqContext.get("result").get("action") == "engineering":
       return engineering.engineering()
    elif reqContext.get("result").get("action") == "humanities":
       return humanities.humanities()
    elif reqContext.get("result").get("action") == "life_sciences":
       return life_sciences.life_sciences()
    elif reqContext.get("result").get("action") == "science_courses":
       return science_courses.science_courses()
    elif reqContext.get("result").get("action") == "chemistry":
       return chemistry.chemistry()
    elif reqContext.get("result").get("action") == "electronics":
       return electronics.electronics()
    elif reqContext.get("result").get("action") == "environmental_studies":
       return environmental_studies.environmental_studies()
    elif reqContext.get("result").get("action") == "mathematics":
       return mathematics.mathematics()
    elif reqContext.get("result").get("action") == "medicine":
       return medicine.medicine()
    elif reqContext.get("result").get("action") == "physics":
       return physics.physics()
    elif reqContext.get("result").get("action") == "social_science":
       return social_science.social_science()
    elif reqContext.get("result").get("action") == "energy_and_earth_science":
       return energy_and_earth_science.energy_and_earth_science()
    elif reqContext.get("result").get("action") == "art_courses":
       return art_courses.art_courses()
    elif reqContext.get("result").get("action") == "architecture":
       return architecture.architecture()
    elif reqContext.get("result").get("action") == "art_and_culture":
       return art_and_culture.art_and_culture()
    elif reqContext.get("result").get("action") == "communication":
       return communication.communication()
    elif reqContext.get("result").get("action") == "design":
       return design.design()
    elif reqContext.get("result").get("action") == "food_and_nutrition":
       return food_and_nutrition.food_and_nutrition()
    elif reqContext.get("result").get("action") == "health_and_safety":
       return health_and_safety.health_and_safety()
    elif reqContext.get("result").get("action") == "history":
       return history.history()
    elif reqContext.get("result").get("action") == "music":
       return music.music()
    elif reqContext.get("result").get("action") == "law":
       return law.law()
    elif reqContext.get("result").get("action") == "BacktoWelcomeContent":
       return showpopularcategories()
    elif reqContext.get("result").get("action") == "BackToProfessionalCourses":
       return professional_courses.professionalcourses()
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
    res = {
        "speech": "Wise choice " + first_name + ". Add certificates to your CV and shine at your workplace.",
        "displayText": "Wise choice " + first_name + ". Add certificates to your CV and shine at your workplace.",
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