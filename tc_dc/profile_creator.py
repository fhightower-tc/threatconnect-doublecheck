#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create a TC-DC profile based on some data."""


def create_profile(data):
    """Create a TC-DC profile based on the given data."""
    proposed_profile = {
        "settings":
        {
            "attributes": {
                "required": [],
                "desired": []
            },
            "associations": {
                "required": [],
                "desired": []
            },
            "tags": {
                "required": [],
                "desired": []
            }
        }
    }

    # capture the attributes, tags, and associations from the data
    attributes = {}
    tags = {}
    associations = {}
    for i in data:
        if i.get('attribute'):
            for attribute in i['attribute']:
                attributes[attribute['type']] = attributes.get(attribute['type'], 0) + 1
        if i.get('tag'):
            for tag in i['tag']:
                tags[tag['name']] = tags.get(tag['name'], 0) + 1
        if i.get('associations'):
            for association in i['associations']['groups']:
                associations[association['type']] = associations.get(association['type'], 0) + 1

    # do some analysis to determine what should be required vs. desired
    item_count = len(data)
    # ATTRIBUTES
    for key, value in attributes.items():
        # if the attribute is used one every data point, make it required
        if value >= item_count:
            proposed_profile['settings']['attributes']['required'].append({
                'type': key,
                'value': ''
            })
        # if the attribute is used on more than half of the data points, make it desired
        elif value >= (item_count / 2):
            proposed_profile['settings']['attributes']['desired'].append({
                'type': key,
                'value': ''
            })
    # TAGS
    for key, value in tags.items():
        # if the tag is used one every data point, make it required
        if value >= item_count:
            proposed_profile['settings']['tags']['required'].append(key)
        # if the tag is used on more than half of the data points, make it desired
        elif value >= (item_count / 2):
            proposed_profile['settings']['tags']['desired'].append(key)
    # ASSOCIATIONS
    for key, value in associations.items():
        # if the association is used one every data point, make it required
        if value >= item_count:
            proposed_profile['settings']['associations']['required'].append({
                "type": key
            })
        # if the association is used on more than half of the data points, make it desired
        elif value >= (item_count / 2):
            proposed_profile['settings']['associations']['desired'].append({
                "type": key
            })

    return proposed_profile
