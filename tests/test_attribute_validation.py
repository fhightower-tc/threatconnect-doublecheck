#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Use a profile to validate attributes."""

from tc_dc import tc_dc

SAMPLE_ATTRIBUTE_PROFILE = {
    "required": [
    {
        "type": "Source",
        "value": "https://threatconnect.com/blog",
        "regex": False
    },
    {
        "type": "Description",
        "value": "",
        "regex": False
    },
    {
        "type": "Additional Analysis and Context",
        "value": r"https://hightower.space",
        "regex": True
    }],
    "desired": []
}


def test_successful_attribute_validation():
    """Make sure a valid attribute profile passes the test."""
    test_attributes = [{
        "type": "Description",
        "value": "This is just a test."
    },
    {
        "type": "Source",
        "value": "https://threatconnect.com/blog"
    },
    {
        "type": "Additional Analysis and Context",
        "value": "https://hightower.space/projects"
    }]
    results = tc_dc._validate_attributes(SAMPLE_ATTRIBUTE_PROFILE, test_attributes)
    assert len(results['failures']) == 0
    assert len(results['warnings']) == 0


def test_attribute_type_failure():
    """Test to make sure a missing type is detected properly."""
    test_attributes = [
    {
        "type": "Source",
        "value": "https://threatconnect.com/blog"
    },
    {
        "type": "Additional Analysis and Context",
        "value": "https://hightower.space/projects"
    }]
    results = tc_dc._validate_attributes(SAMPLE_ATTRIBUTE_PROFILE, test_attributes)
    assert len(results['failures']) == 1
    assert len(results['warnings']) == 0
    assert results['failures'][0] == tc_dc.MESSAGES['missingAttribute'].format('of type "Description"')


def test_attribute_missing_nonregex_value():
    """Test to make sure a missing value (not a regex) is detected properly."""
    test_attributes = [{
        "type": "Description",
        "value": "This is just a test."
    },
    {
        "type": "Source",
        "value": "threatconnect.com"
    },
    {
        "type": "Additional Analysis and Context",
        "value": "https://hightower.space/projects"
    }]
    results = tc_dc._validate_attributes(SAMPLE_ATTRIBUTE_PROFILE, test_attributes)
    assert len(results['failures']) == 1
    assert len(results['warnings']) == 0
    assert results['failures'][0] == tc_dc.MESSAGES['missingAttribute'].format('of type "Source" with the value "https://threatconnect.com/blog"')


def test_attribute_missing_regex_value():
    """Test to make sure a missing value (a regex) is detected properly."""
    test_attributes = [{
        "type": "Description",
        "value": "This is just a test."
    },
    {
        "type": "Source",
        "value": "https://threatconnect.com/blog"
    },
    {
        "type": "Additional Analysis and Context",
        "value": "https://foo.space/projects"
    }]
    results = tc_dc._validate_attributes(SAMPLE_ATTRIBUTE_PROFILE, test_attributes)
    assert len(results['failures']) == 1
    assert len(results['warnings']) == 0
    assert results['failures'][0] == tc_dc.MESSAGES['missingAttribute'].format('of type "Additional Analysis and Context" with a value matching the regex "https://hightower.space"')


def test_attribute_missing_type_and_nonregex_value():
    """Test to make sure a missing type and value (not a regex) is detected properly."""
    test_attributes = [
    {
        "type": "Source",
        "value": "foo"
    },
    {
        "type": "Additional Analysis and Context",
        "value": "https://hightower.space/projects"
    }]
    results = tc_dc._validate_attributes(SAMPLE_ATTRIBUTE_PROFILE, test_attributes)
    assert len(results['failures']) == 2
    assert len(results['warnings']) == 0
    assert tc_dc.MESSAGES['missingAttribute'].format('of type "Source" with the value "https://threatconnect.com/blog"') in results['failures']
    assert tc_dc.MESSAGES['missingAttribute'].format('of type "Description"') in results['failures']


def test_attribute_missing_type_and_regex_value():
    """Test to make sure a missing type and value (a regex) is detected properly."""
    test_attributes = [
    {
        "type": "Source",
        "value": "https://threatconnect.com/blog"
    },
    {
        "type": "Additional Analysis and Context",
        "value": "https://foo.space/projects"
    }]
    results = tc_dc._validate_attributes(SAMPLE_ATTRIBUTE_PROFILE, test_attributes)
    assert len(results['failures']) == 2
    assert len(results['warnings']) == 0
    assert tc_dc.MESSAGES['missingAttribute'].format('of type "Additional Analysis and Context" with a value matching the regex "https://hightower.space"') in results['failures']
    assert tc_dc.MESSAGES['missingAttribute'].format('of type "Description"') in results['failures']


def test_attribute_missing_nonregex_value_and_regex_value():
    """Test to make sure a value (not a regex) and a value (a regex) is detected properly."""
    test_attributes = [{
        "type": "Description",
        "value": "This is just a test."
    },
    {
        "type": "Source",
        "value": "foo"
    },
    {
        "type": "Additional Analysis and Context",
        "value": "https://foo.space/projects"
    }]
    results = tc_dc._validate_attributes(SAMPLE_ATTRIBUTE_PROFILE, test_attributes)
    assert len(results['failures']) == 2
    assert len(results['warnings']) == 0
    assert tc_dc.MESSAGES['missingAttribute'].format('of type "Additional Analysis and Context" with a value matching the regex "https://hightower.space"') in results['failures']
    assert tc_dc.MESSAGES['missingAttribute'].format('of type "Source" with the value "https://threatconnect.com/blog"') in results['failures']
