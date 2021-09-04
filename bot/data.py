#!/usr/bin/env python3

import os
import random
import requests
import json

TEXT_GEN_API_VAR = 'DEEP_AI_KEY'

words = [
  'The', 'he', 'at', 'but', 'there', 'of', 'was', 'be', 'not', 'use', 'and', 'for', 'this', 'what', 'an', 'a', 'on', 'have', 'all', 'each',
  'to', 'are', 'from', 'were', 'which', 'in', 'as', 'or', 'we', 'she', 'is', 'with', 'ine', 'when', 'do', 'you', 'his', 'had', 'your',
  'how', 'that', 'they', 'by', 'can', 'their', 'it', 'I', 'word', 'said', 'if'
]

with open(os.path.join(os.path.dirname(__file__), './data/cities.json')) as cities_file:
  cities = json.load(cities_file)

gop_members = [
  'Gary VanDeaver', 'Bryan Slaton', 'Cecil Bell Jr.', 'Keith Bell', 'Cole Hefner', 'Matt Schaefer', 'Jay Dean', 'Cody Harris',
  'Chris Paddie', 'Travis Clardy', 'Kyle Kacal', 'Ben Leman', 'John N. Raney', 'Steve Toth', 'Will Metcalf', 'John Cyrier', 'Ernest Bailes',
  'James White', 'Terry Wilson', 'Dade Phelan', 'Mayes Middleton', 'Greg Bonnen', 'Cody Vasut', 'Brooks Landgraf', 'Tom Craddick',
  'Dustin Burrows', 'John Frullo', 'Phil Stephenson', 'John T. Smithee', 'Four Price', 'Ken King', 'Candy Noble', 'Stephanie Klick',
  'Jeff Cason', 'Matt Krause', 'Tony Tinderholt', 'David Cook', 'Craig Goldman', 'Giovanni Capriglione', 'Charlie Geren', 'Sam Harless',
  'Dan Huberty', 'Briscoe Cain', 'Dennis Paul', 'Tom Oliverson', 'Mike Schofield'
]
firstNames = ['Hannah', 'Olivia', 'Marcia', 'Sarah', 'Tara', 'Brooke', 'Wanda', 'Andrea', 'Julie']

maleFirstNames = [
  'Michael',
  'Christopher',
  'Matthew',
  'Joshua',
  'Jacob',
  'Nicholas',
  'Andrew',
  'Daniel',
  'Tyler',
  'Joseph',
  'Brandon',
  'David',
  'James',
  'Ryan',
  'John',
  'Zachary',
  'Justin',
  'William',
  'Anthony',
  'Robert',
  'Patrick',
]

lastNames = [
  'Morgan', 'Walker', 'Lewis', 'Butler', 'Jones', 'Barnes', 'Martin', 'Wright', 'Foster', 'Smith', 'Johnson', 'Williams', 'Brown', 'Miller',
  'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Jackson', 'Thompson', 'White'
]

# Seeds for text body generation
gpt2_prompts = [
  'My neighbor got an illegal abortion.', 'I suspect my father has violated the abortion ban.',
  random.choice(firstNames) + ' ' + random.choice(lastNames) + ' is helping people get abortions.',
  random.choice(gop_members) + ' has been sneaking around the abortion clinic in ' + random.choice(list(cities)) + '.'
]

info_location = [
  'A friend saw them', 'I work at the clinic', 'I know his secretary', 'He told me at the club', 'The police report', 'His wife told me',
  'From a coworker', 'From a neighbor', 'From a family member.', 'Heard from a friend', 'a relative told me', 'a private source',
  'A confession at church', 'I know their cousin', 'a taxi driver', 'From a cashier', 'Got a confidential tip', 'From a fellow parent',
  'a concerned citizen', 'From a relative.', 'A PP volunteer', 'A charity worker', 'A social worker', 'From my friend who knows cops',
  'from a lawyer', 'From a government employee'
]

zip_codes = [
  75001,
  75006,
  75011,
  75014,
  75015,
  75016,
  75017,
  75019,
  75030,
  75038,
  75039,
  75040,
  75041,
  75042,
  75043,
  75044,
  75045,
  75046,
  75047,
  75048,
  75048,
  75049,
  75050,
  75051,
  75052,
  75053,
  75054,
  75060,
  75061,
  75062,
  75063,
  75080,
  75081,
  75082,
  75083,
  75085,
  75088,
  75089,
  75104,
  75106,
  75115,
  75116,
  75123,
  75134,
  75137,
  75138,
  75141,
  75146,
  75149,
  75150,
  75159,
  75159,
  75172,
  75180,
  75180,
  75181,
  75182,
  75182,
  75185,
  75187,
  75201,
  75202,
  75203,
  75204,
  75205,
  75206,
  75207,
  75208,
  75209,
  75210,
  75211,
  75212,
  75214,
  75215,
  75216,
  75217,
  75218,
  75219,
  75220,
  75221,
  75222,
  75223,
  75224,
  75225,
  75226,
  75227,
  75228,
  75229,
  75230,
  75231,
  75232,
  75233,
  75234,
  75234,
  75235,
  75236,
  75237,
  75238,
  75239,
  75240,
  75241,
  75242,
  75243,
  75244,
  75244,
  75245,
  75246,
  75247,
  75248,
  75249,
  75250,
  75251,
  75253,
  75254,
  75258,
  75260,
  75261,
  75262,
  75263,
  75264,
  75265,
  75266,
  75267,
  75270,
  75295,
  75313,
  75315,
  75336,
  75339,
  75342,
  75354,
  75355,
  75356,
  75357,
  75359,
  75360,
  75367,
  75370,
  75371,
  75372,
  75374,
  75376,
  75378,
  75379,
  75380,
  75381,
  75382,
  75398,
]
# TX IPs gathered from here: https://www.xmyip.com/ip-addresses/united--states/texas
ips = [
  "66.241.29.", 	# Addison
  "63.113.179.",	# Austin
  "66.68.131.",	  # Austin
  "67.198.60.",	  # Austin
  "65.237.143.",	# Baytown
  "50.207.247.",	# Baytown
  "66.135.128.",	# Bellaire
  "23.92.6.",	    # Bryan
  "63.25.240.",	  # Carrollton
  "66.63.230.",	  # Cat Spring
  "68.93.99.",	  # Cedar Hill
  "47.183.96.",	  # Coleman
  "64.244.23.",	  # Dallas
  "67.192.56.",	  # Dallas
  "50.11.16.",	  # Dallas
  "17.168.60.",	  # Dallas
  "24.178.211.",	# Dallas
  "68.94.16.",	  # Dallas
  "32.149.82.",	  # Dallas
  "12.51.71.",	  # Dallas
  "32.100.250.",	# Dallas
  "64.130.247.",	# Dallas
  "47.32.214.",	  # Dallas
  "12.130.66.",	  # Dallas
  "32.146.241.",	# Dallas
  "66.136.72.",	  # Dallas
  "47.37.65.",	  # Denton
  "24.178.215.",	# Denton
  "24.26.205.",	  # Edinburg
  "47.185.43.",	  # Fort Worth
  "63.174.150.",	# Henderson
  "64.91.186.",	  # Houston
  "50.232.177.",	# Houston
  "63.20.88.",	  # Houston
  "67.154.251.",	# Houston
  "50.171.94.",	  # Houston
  "50.162.76.",	  # Houston
  "66.85.21.",	  # Houston
  "12.155.35.",	  # Houston
  "12.127.182.",	# Houston
  "66.94.28.",	  # Huntsville
  "47.32.201.",	  # Keller
  "65.118.126.",	# Lancaster
  "12.21.60.",	  # Laredo
  "68.90.9.",	    # McKinney
  "24.238.135.",	# Mesquite
  "12.145.15.",	  # Midland
  "12.234.53.",	  # Nacogdoches
  "68.95.104.",	  # Odessa
  "24.155.134.",	# Odessa
  "50.8.31.",	    # Pearland
  "67.36.38.",	  # Plano
  "64.217.80.",	  # Plano
  "67.64.17.",	  # Plano
  "67.64.98.",	  # Plano
  "65.68.105.",	  # Plano
  "66.138.97.",	  # Plano
  "66.138.46.",	  # Plano
  "65.71.242.",	  # Plano
  "68.89.223.",	  # Richardson
  "68.89.72.",	  # Richardson
  "64.123.77.",	  # Richardson
  "66.73.16.",	  # Richardson
  "63.207.81.",	  # Richardson
  "67.119.241.",	# Richardson
  "66.10.99.",	  # Richardson
  "66.137.60.",	  # Richardson
  "67.74.143.",	  # Rosenberg
  "15.172.130.",	# San Antonio
  "15.145.190.",	# San Antonio
  "15.229.1.",	  # San Antonio
  "67.65.218.",	  # San Antonio
  "15.123.42.",	  # San Antonio
  "15.216.138.",	# San Antonio
  "15.113.233.",	# San Antonio
  "15.232.35.",	  # San Antonio
  "15.179.154.",	# San Antonio
  "66.142.91.",	  # San Antonio
  "15.130.49.",	  # San Antonio
  "15.213.171.",	# San Antonio
  "15.119.8.",	  # San Antonio
  "15.197.59.",	  # San Antonio
  "15.113.152.",	# San Antonio
  "15.178.211.",	# San Antonio
  "15.215.118.",	# San Antonio
  "23.100.192.",	# San Antonio
  "15.169.189.",	# San Antonio
  "15.222.61.",	  # San Antonio
  "15.123.98.",	  # San Antonio
  "15.209.38.",	  # San Antonio
  "24.174.189.",	# San Antonio
  "15.162.111.",	# San Antonio
  "12.97.5.",	    # San Antonio
  "15.140.30.",	  # San Antonio
  "15.165.165.",	# San Antonio
  "66.114.208.",	# Stafford
  "64.123.128.",	# Waco
  "68.113.212.",	# Watauga
  "63.82.222.",	  # Weatherford
  "24.27.66."	    # Wylie
]
# random element from each list


def anonymous_form():
  while True:
    city, county = random.choice(list(cities.items()))
    form_data = {
      'textarea-1': get_tip_body(),
      'text-1': random.choice(info_location),
      'text-6': 'Dr. ' + random.choice(maleFirstNames) + ' ' + random.choice(lastNames),
      'text-2': city,
      'text-3': 'Texas',
      'text-4': str(random.randint(75001, 79942)),
      'text-5': county,
      'hidden-1': random.choice(ips) + str(random.randint(0, 255)),
      'checkbox-1[]': 'no',
    }
    yield form_data


def sign_up_page():
  raise NotImplementedError()


def get_tip_body():
  # If we have an API key for GPT2, use it
  if TEXT_GEN_API_VAR in os.environ:
    prompt = random.choice(gpt2_prompts)
    r = requests.post(
      "https://api.deepai.org/api/text-generator", data={
        'text': prompt,
      }, headers={'api-key': os.environ[TEXT_GEN_API_VAR]}
    )
    rv = str(r.json()['output'].encode('utf-8'))
    # cut out the prompt, which comes from a limited set and can be filtered on
    rv = rv.replace(prompt, '').lstrip()
    # take string up through last complete sentence since we occasionally get trailing words
    if '.' in rv:
      rv = rv[0:rv.rindex('.')] + '.'
    return rv
  else:
    # standard tip body generation
    return random.choice(gop_members) + ' took their mistress ' + random.choice(firstNames) + ' ' + random.choice(
      lastNames
    ) + ' to get an abortion after their affair.'
