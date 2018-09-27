#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Library for validating the contents and structure of data in ThreatConnect."""

import collections
import re


Attribute = collections.namedtuple('Attribute', ['type', 'value'])

MESSAGES = {
    'duplicateAttributes': 'Duplicate attributes were found.',
    'numberOfAttributesDiscrepency': 'Expecting no {} than {} attributes, but found {} attributes.',
    'missingAttribute': 'Missing attribute {}',
    'missingTag': 'Missing {} tag "{}"'
}


def _iterate_and_validate_attributes(profile_attribute_key, profile_attributes, data_attributes):
    messages = list()
    data_attributes_set = set([Attribute(attr['type'], attr['value']) for attr in data_attributes])

    for profile_attribute in profile_attributes[profile_attribute_key]:
        if profile_attribute['type']:
            if profile_attribute['value']:
                if profile_attribute['regex']:
                    # check attributes where the TYPE, VALUE, and REGEX are specified
                    attribute_found = False
                    for attribute in data_attributes:
                        if attribute['type'] == profile_attribute['type']:
                            if re.search(profile_attribute['value'], attribute['value']):
                                attribute_found = True
                                break
                    if not attribute_found:
                        messages.append(MESSAGES['missingAttribute'].format('of type "{}" with a value matching the regex "{}"').format(profile_attribute['type'], profile_attribute['value']))
                else:
                    # check attributes where the TYPE and VALUE are specified
                    if Attribute(profile_attribute['type'], profile_attribute['value']) not in data_attributes_set:
                        messages.append(MESSAGES['missingAttribute'].format('of type "{}" with the value "{}"'.format(profile_attribute['type'], profile_attribute['value'])))
            else:
                # check attributes where only the TYPE is specified
                attribute_found = False
                for attribute in data_attributes:
                    if attribute['type'] == profile_attribute['type']:
                        attribute_found = True
                        break
                if not attribute_found:
                    messages.append(MESSAGES['missingAttribute'].format('of type "{}"').format(profile_attribute['type']))
        elif profile_attribute['value']:
            if profile_attribute['regex']:
                # check attributes where the VALUE and REGEX are specified
                attribute_found = False
                for attribute in data_attributes:
                    if re.search(profile_attribute['value'], attribute['value']):
                        attribute_found = True
                        break
                if not attribute_found:
                    messages.append(MESSAGES['missingAttribute'].format('with a value matching the regex "{}"').format(profile_attribute['value']))
            else:
                # check attributes where only the VALUE is specified
                attribute_found = False
                for attribute in data_attributes:
                    if attribute['value'] == profile_attribute['value']:
                        attribute_found = True
                        break
                if not attribute_found:
                    messages.append(MESSAGES['missingAttribute'].format('with the value "{}"').format(profile_attribute['value']))
        else:
            raise ValueError('Improperly formatted attribute validation test: {}. Every attribute must have either a "type" or "value".'.format(profile_attribute))
    return messages


def _validate_attributes(profile_attributes, data_attributes):
    """Make sure all of the attributes specified by the profile are present in the data."""
    results = {
        'failures': list(),
        'warnings': list()
    }

    if profile_attributes.get('actionOnDuplicates'):
        data_attributes_set = set([Attribute(attr['type'], attr['value']) for attr in data_attributes])
        if len(data_attributes_set) != len(data_attributes):
            if profile_attributes['actionOnDuplicates'] == 'fail':
                results['failures'].append(MESSAGES['duplicateAttributes'])
            elif profile_attributes['actionOnDuplicates'] == 'warn':
                results['warnings'].append(MESSAGES['duplicateAttributes'])

    if profile_attributes.get('minNumberOfAttributes'):
        if len(data_attributes) < profile_attributes['minNumberOfAttributes']:
            results['failures'].append(MESSAGES['numberOfAttributesDiscrepency'].format('less', profile_attributes['minNumberOfAttributes'], len(data_attributes)))

    if profile_attributes.get('maxNumberOfAttributes'):
        if len(data_attributes) > profile_attributes['maxNumberOfAttributes']:
            results['failures'].append(MESSAGES['numberOfAttributesDiscrepency'].format('more', profile_attributes['maxNumberOfAttributes'], len(data_attributes)))

    if profile_attributes.get('required'):
        results['failures'].extend(_iterate_and_validate_attributes('required', profile_attributes, data_attributes))

    if profile_attributes.get('desired'):
        results['warnings'].extend(_iterate_and_validate_attributes('desired', profile_attributes, data_attributes))

    return results


def _iterate_and_validate_associations(profile_association_key, profile_associations, formatted_data_associations):
    messages = list()

    for association in profile_associations[profile_association_key]:
        if not formatted_data_associations.get(association['type']):
            if association.get('count') is not None:
                if association.get('count') > 0:
                    messages.append('Expected this item to be associated with {} {}, but found no associations with {} were found.'.format(association['count'], association['type'], association['type']))
                else:
                    pass
            else:
                messages.append('Expected at least one association with a {}, but no such association was found.'.format(association['type']))
        else:
            if association.get('count'):
                if formatted_data_associations[association['type']] != association['count']:
                    messages.append('Incorrect number of {} associations found. Expected {}, but only found {}.'.format(association['type'], association['count'], formatted_data_associations[association['type']]))
    return messages


def _validate_associations(profile_associations, data_associations):
    """Make sure all of the associations specified by the profile are present in the data."""
    results = {
        'failures': list(),
        'warnings': list()
    }
    formatted_data_associations = dict()
    for association in data_associations:
        if formatted_data_associations.get(association['type']):
            formatted_data_associations[association['type']] += 1
        else:
            formatted_data_associations[association['type']] = 1

    if profile_associations.get('required'):
        results['failures'] = _iterate_and_validate_associations('required', profile_associations, formatted_data_associations)

    if profile_associations.get('desired'):
        results['warnings'] = _iterate_and_validate_associations('desired', profile_associations, formatted_data_associations)

    return results


def _iterate_and_validate_tags(profile_tag_key, profile_tags, formatted_data_tags):
    messages = list()
    for tag in profile_tags[profile_tag_key]:
        if tag not in formatted_data_tags:
            messages.append(MESSAGES['missingTag'].format(profile_tag_key, tag))
    return messages


def _validate_tags(profile_tags, data_tags):
    """Make sure all of the tags specified by the profile are present in the data."""
    results = {
        'failures': list(),
        'warnings': list()
    }
    formatted_data_tags = [tag['name'] for tag in data_tags]

    if profile_tags.get('required'):
        results['failures'] = _iterate_and_validate_tags('required', profile_tags, formatted_data_tags)

    if profile_tags.get('desired'):
        results['warnings'] = _iterate_and_validate_tags('desired', profile_tags, formatted_data_tags)

    return results


def apply_profile(profile, data):
    """Apply the given profile to the given data."""
    results = {
        'failures': list(),
        'warnings': list()
    }

    for item in data:
        # handle ATTRIBUTES
        if profile['settings'].get('attributes'):
            if item.get('attribute'):
                attribute_results = _validate_attributes(profile['settings']['attributes'], item['attribute'])
                results['failures'].extend(attribute_results['failures'])
                results['warnings'].extend(attribute_results['warnings'])
            else:
                if profile['settings']['attributes'].get('required'):
                    results['failures'].append('Expected required attributes, but no attributes found.')
                else:
                    results['warnings'].append('Expected desired attributes, but no attributes found.')

        # handle ASSOCIATIONS
        if profile['settings'].get('associations'):
            if item.get('associations'):
                tag_results = _validate_associations(profile['settings']['associations'], item['associations'])
                results['failures'].extend(tag_results['failures'])
                results['warnings'].extend(tag_results['warnings'])
            else:
                if profile['settings']['associations'].get('required'):
                    results['failures'].append('Expected required associations, but no associations found.')
                else:
                    results['warnings'].append('Expected desired associations, but no associations found.')

        # handle TAGS
        if profile['settings'].get('tags'):
            if item.get('tag'):
                tag_results = _validate_tags(profile['settings']['tags'], item['tag'])
                results['failures'].extend(tag_results['failures'])
                results['warnings'].extend(tag_results['warnings'])
            else:
                if profile['settings']['tags'].get('required'):
                    results['failures'].append('Expected required tags, but no tags found.')
                else:
                    results['warnings'].append('Expected desired tags, but no tags found.')

    return results
