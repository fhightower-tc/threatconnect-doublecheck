#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Library for validating the contents and structure of data in ThreatConnect."""

import collections
import re


Attribute = collections.namedtuple('Attribute', ['type', 'value'])

MESSAGES = {
    'duplicateAttributes': 'Duplicate attributes were found.',
    'numberOfAttributesDiscrepency': 'Expecting no {} than {} attributes, but found {} attributes.',
    'missingAttribute': 'Missing attribute {}'
}


def _iterate_and_validate_attributes(profile_attribute_key, profile_attributes, data_attributes):
    """."""
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


def _apply_profile(profile, data):
    """Apply the given profile to the given data."""
    results = {
        'failures': list(),
        'warnings': list()
    }
    for item in data:
        # handle attributes
        if profile['settings'].get('attributes'):
            if item.get('attribute'):
                attribute_results = _validate_attributes(profile['settings']['attributes'], item['attribute'])
                results['failures'].extend(attribute_results['failures'])
                results['warnings'].extend(attribute_results['warnings'])
            else:
                # TODO: record a failure
                pass

        # handle tags


    return results


def main():
    pass


if __name__ == '__main__':
    main()
