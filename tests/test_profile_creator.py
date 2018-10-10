#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tc_dc import profile_creator

from .test_profile_validation import data_1_a, data_1_b

DATA = [{'address': 'guangluma@hotmail.com',
  'associations': {'groups': [{'dateAdded': '2018-06-29T12:33:55Z',
     'id': 1132777716,
     'name': 'GrьЯe',
     'ownerName': 'Technical Blogs and Reports',
     'type': 'Incident',
     'webLink': 'https://app.threatconnect.com/auth/incident/incident.xhtml?incident=1132777716'}],
   'indicators': [{'confidence': 63,
     'dateAdded': '2018-06-29T12:33:59Z',
     'description': 'This indicator appears in a post from Tamagothi Daily Spam.',
     'id': 1132778073,
     'lastModified': '2018-09-27T13:40:56Z',
     'ownerName': 'Technical Blogs and Reports',
     'rating': 2.0,
     'summary': 'guanglum70@gmail.com',
     'webLink': 'https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=guanglum70%40gmail.com&owner=Technical+Blogs+and+Reports'}]},
  'attribute': [{'dateAdded': '2018-06-29T12:34:03Z',
    'displayed': True,
    'id': 1132778206,
    'lastModified': '2018-06-29T12:34:03Z',
    'type': 'Source',
    'value': 'http://spam.tamagothi.de/2018/06/29/gre-2/'},
   {'dateAdded': '2018-06-29T12:34:03Z',
    'displayed': True,
    'id': 1132778193,
    'lastModified': '2018-06-29T12:34:03Z',
    'type': 'Description',
    'value': 'This indicator appears in a post from Tamagothi Daily Spam.'}],
  'confidence': 63,
  'dateAdded': '2018-06-29T12:34:03Z',
  'description': 'This indicator appears in a post from Tamagothi Daily Spam.',
  'id': 1132778184,
  'lastModified': '2018-09-27T13:40:56Z',
  'name': 'guangluma@hotmail.com',
  'owner': {'id': 10666,
   'name': 'Technical Blogs and Reports',
   'type': 'Source'},
  'rating': 2.0,
  'source': 'http://spam.tamagothi.de/2018/06/29/gre-2/',
  'tag': [{'name': 'Mail',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Mail&owner=Technical+Blogs+and+Reports'},
   {'name': 'BLOG: Tamagothi Daily Spam',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=BLOG%3A+Tamagothi+Daily+Spam&owner=Technical+Blogs+and+Reports'},
   {'name': '419',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=419&owner=Technical+Blogs+and+Reports'},
   {'name': 'gmail.com',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=gmail.com&owner=Technical+Blogs+and+Reports'},
   {'name': 'Geschäftsvorschlag',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Gesch%C3%A4ftsvorschlag&owner=Technical+Blogs+and+Reports'}],
  'webLink': 'https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=guangluma%40hotmail.com&owner=Technical+Blogs+and+Reports'},
 {'address': 'guanglum70@gmail.com',
  'associations': {'groups': [{'dateAdded': '2018-06-29T12:33:55Z',
     'id': 1132777716,
     'name': 'GrьЯe',
     'ownerName': 'Technical Blogs and Reports',
     'type': 'Incident',
     'webLink': 'https://app.threatconnect.com/auth/incident/incident.xhtml?incident=1132777716'}],
   'indicators': [{'confidence': 63,
     'dateAdded': '2018-06-29T12:34:03Z',
     'description': 'This indicator appears in a post from Tamagothi Daily Spam.',
     'id': 1132778184,
     'lastModified': '2018-09-27T13:40:56Z',
     'ownerName': 'Technical Blogs and Reports',
     'rating': 2.0,
     'summary': 'guangluma@hotmail.com',
     'webLink': 'https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=guangluma%40hotmail.com&owner=Technical+Blogs+and+Reports'}]},
  'attribute': [{'dateAdded': '2018-06-29T12:34:00Z',
    'displayed': True,
    'id': 1132778099,
    'lastModified': '2018-06-29T12:34:00Z',
    'type': 'Source',
    'value': 'http://spam.tamagothi.de/2018/06/29/gre-2/'},
   {'dateAdded': '2018-06-29T12:34:00Z',
    'displayed': True,
    'id': 1132778085,
    'lastModified': '2018-06-29T12:34:00Z',
    'type': 'Description',
    'value': 'This indicator appears in a post from Tamagothi Daily Spam.'}],
  'confidence': 63,
  'dateAdded': '2018-06-29T12:33:59Z',
  'description': 'This indicator appears in a post from Tamagothi Daily Spam.',
  'id': 1132778073,
  'lastModified': '2018-09-27T13:40:56Z',
  'name': 'guanglum70@gmail.com',
  'owner': {'id': 10666,
   'name': 'Technical Blogs and Reports',
   'type': 'Source'},
  'rating': 2.0,
  'source': 'http://spam.tamagothi.de/2018/06/29/gre-2/',
  'tag': [{'name': 'Mail',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Mail&owner=Technical+Blogs+and+Reports'},
   {'name': 'BLOG: Tamagothi Daily Spam',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=BLOG%3A+Tamagothi+Daily+Spam&owner=Technical+Blogs+and+Reports'},
   {'name': '419',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=419&owner=Technical+Blogs+and+Reports'},
   {'name': 'gmail.com',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=gmail.com&owner=Technical+Blogs+and+Reports'},
   {'name': 'Geschäftsvorschlag',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Gesch%C3%A4ftsvorschlag&owner=Technical+Blogs+and+Reports'}],
  'webLink': 'https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=guanglum70%40gmail.com&owner=Technical+Blogs+and+Reports'}]


def test_profile_creator_1():
    profile = profile_creator.create_profile(DATA)
    assert profile == {'settings': {'attributes': {'required': [{'type': 'Source', 'value': ''}, {'type': 'Description', 'value': ''}], 'desired': []}, 'associations': {'required': [{'type': 'Incident'}], 'desired': []}, 'tags': {'required': ['Mail', 'BLOG: Tamagothi Daily Spam', '419', 'gmail.com', 'Geschäftsvorschlag'], 'desired': []}}}


def test_profile_creator_differentiate_required_and_desired():
    data = [{'address': 'guangluma@hotmail.com',
  'associations': {'groups': [{'dateAdded': '2018-06-29T12:33:55Z',
     'id': 1132777716,
     'name': 'GrьЯe',
     'ownerName': 'Technical Blogs and Reports',
     'type': 'Incident',
     'webLink': 'https://app.threatconnect.com/auth/incident/incident.xhtml?incident=1132777716'}],
   'indicators': [{'confidence': 63,
     'dateAdded': '2018-06-29T12:33:59Z',
     'description': 'This indicator appears in a post from Tamagothi Daily Spam.',
     'id': 1132778073,
     'lastModified': '2018-09-27T13:40:56Z',
     'ownerName': 'Technical Blogs and Reports',
     'rating': 2.0,
     'summary': 'guanglum70@gmail.com',
     'webLink': 'https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=guanglum70%40gmail.com&owner=Technical+Blogs+and+Reports'}]},
  'attribute': [{'dateAdded': '2018-06-29T12:34:03Z',
    'displayed': True,
    'id': 1132778193,
    'lastModified': '2018-06-29T12:34:03Z',
    'type': 'Description',
    'value': 'This indicator appears in a post from Tamagothi Daily Spam.'}],
  'confidence': 63,
  'dateAdded': '2018-06-29T12:34:03Z',
  'description': 'This indicator appears in a post from Tamagothi Daily Spam.',
  'id': 1132778184,
  'lastModified': '2018-09-27T13:40:56Z',
  'name': 'guangluma@hotmail.com',
  'owner': {'id': 10666,
   'name': 'Technical Blogs and Reports',
   'type': 'Source'},
  'rating': 2.0,
  'source': 'http://spam.tamagothi.de/2018/06/29/gre-2/',
  'tag': [{'name': 'Mail',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Mail&owner=Technical+Blogs+and+Reports'},
   {'name': 'BLOG: Tamagothi Daily Spam',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=BLOG%3A+Tamagothi+Daily+Spam&owner=Technical+Blogs+and+Reports'},
   {'name': '419',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=419&owner=Technical+Blogs+and+Reports'},
   {'name': 'gmail.com',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=gmail.com&owner=Technical+Blogs+and+Reports'},
   {'name': 'Geschäftsvorschlag',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Gesch%C3%A4ftsvorschlag&owner=Technical+Blogs+and+Reports'}],
  'webLink': 'https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=guangluma%40hotmail.com&owner=Technical+Blogs+and+Reports'},
 {'address': 'guanglum70@gmail.com',
  'associations': {'groups': [{'dateAdded': '2018-06-29T12:33:55Z',
     'id': 1132777716,
     'name': 'GrьЯe',
     'ownerName': 'Technical Blogs and Reports',
     'type': 'Incident',
     'webLink': 'https://app.threatconnect.com/auth/incident/incident.xhtml?incident=1132777716'}],
   'indicators': [{'confidence': 63,
     'dateAdded': '2018-06-29T12:34:03Z',
     'description': 'This indicator appears in a post from Tamagothi Daily Spam.',
     'id': 1132778184,
     'lastModified': '2018-09-27T13:40:56Z',
     'ownerName': 'Technical Blogs and Reports',
     'rating': 2.0,
     'summary': 'guangluma@hotmail.com',
     'webLink': 'https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=guangluma%40hotmail.com&owner=Technical+Blogs+and+Reports'}]},
  'attribute': [{'dateAdded': '2018-06-29T12:34:00Z',
    'displayed': True,
    'id': 1132778099,
    'lastModified': '2018-06-29T12:34:00Z',
    'type': 'Source',
    'value': 'http://spam.tamagothi.de/2018/06/29/gre-2/'},
   {'dateAdded': '2018-06-29T12:34:00Z',
    'displayed': True,
    'id': 1132778085,
    'lastModified': '2018-06-29T12:34:00Z',
    'type': 'Description',
    'value': 'This indicator appears in a post from Tamagothi Daily Spam.'}],
  'confidence': 63,
  'dateAdded': '2018-06-29T12:33:59Z',
  'description': 'This indicator appears in a post from Tamagothi Daily Spam.',
  'id': 1132778073,
  'lastModified': '2018-09-27T13:40:56Z',
  'name': 'guanglum70@gmail.com',
  'owner': {'id': 10666,
   'name': 'Technical Blogs and Reports',
   'type': 'Source'},
  'rating': 2.0,
  'source': 'http://spam.tamagothi.de/2018/06/29/gre-2/',
  'tag': [{'name': 'Mail',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Mail&owner=Technical+Blogs+and+Reports'},
   {'name': 'BLOG: Tamagothi Daily Spam',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=BLOG%3A+Tamagothi+Daily+Spam&owner=Technical+Blogs+and+Reports'},
   {'name': '419',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=419&owner=Technical+Blogs+and+Reports'},
   {'name': 'Geschäftsvorschlag',
    'webLink': 'https://app.threatconnect.com/auth/tags/tag.xhtml?tag=Gesch%C3%A4ftsvorschlag&owner=Technical+Blogs+and+Reports'}],
  'webLink': 'https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=guanglum70%40gmail.com&owner=Technical+Blogs+and+Reports'}]
    profile = profile_creator.create_profile(data)
    assert profile == {'settings': {'attributes': {'required': [{'type': 'Description', 'value': ''}], 'desired': [{'type': 'Source', 'value': ''}]}, 'associations': {'required': [{'type': 'Incident'}], 'desired': []}, 'tags': {'required': ['Mail', 'BLOG: Tamagothi Daily Spam', '419', 'Geschäftsvorschlag'], 'desired': ['gmail.com']}}}


# TODO: get the functions below working - the current problem is that the associations in data in data_1_a and data_1_b are not in the same format as the form returned by democritus (which can be seen in the tests above)
def test_profile_creator_a():
    data = data_1_a()
    profile = profile_creator.create_profile(data)
    assert len(profile) == 1
    assert profile == {'settings': {'attributes': {'required': [{'type': 'Description', 'value': ''}, {'type': 'Source', 'value': ''}, {'type': 'Additional Analysis and Context', 'value': ''}], 'desired': []}, 'associations': {'required': [{'type': 'Document'}, {'type': 'Adversary'}], 'desired': []}, 'tags': {'required': ['Ugly'], 'desired': []}}}


def test_profile_creator_b():
    data = data_1_b()
    profile = profile_creator.create_profile(data)
    assert len(profile) == 1
    assert profile == {'settings': {'attributes': {'required': [{'type': 'Description', 'value': ''}, {'type': 'Source', 'value': ''}, {'type': 'Additional Analysis and Context', 'value': ''}], 'desired': []}, 'associations': {'required': [{'type': 'Document'}], 'desired': [{'type': 'Adversary'}]}, 'tags': {'required': [], 'desired': ['Ugly']}}}
