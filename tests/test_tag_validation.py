#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Use a profile to validate attributes."""

import json
import os

import pytest

from tc_dc import tc_dc

from .utility import _read_file

SAMPLE_TAG_PROFILE = {
    "required": ['Bad', 'Ugly'],
    "desired": ['Good']
}


def test_successful_tag_validation():
    """Make sure a valid tag profile passes the test."""
    test_tags = [
        {
            "name": "Bad"
        }, {
            "name": "Ugly"
        }, {
            "name": "Good"
        }
    ]
    results = tc_dc._validate_tags(SAMPLE_TAG_PROFILE, test_tags)
    assert len(results['failures']) == 0
    assert len(results['warnings']) == 0


def test_missing_required_tag():
    test_tags = [
        {
            "name": "Ugly"
        }, {
            "name": "Good"
        }
    ]
    results = tc_dc._validate_tags(SAMPLE_TAG_PROFILE, test_tags)
    assert len(results['failures']) == 1
    assert len(results['warnings']) == 0
    assert tc_dc.MESSAGES['missingTag'].format('required', 'Bad') in results['failures']


def test_missing_desired_tag():
    test_tags = [
        {
            "name": "Bad"
        }, {
            "name": "Ugly"
        }
    ]
    results = tc_dc._validate_tags(SAMPLE_TAG_PROFILE, test_tags)
    assert len(results['failures']) == 0
    assert len(results['warnings']) == 1
    assert tc_dc.MESSAGES['missingTag'].format('desired', 'Good') in results['warnings']


def test_missing_desired_and_required_tag():
    test_tags = [
        {
            "name": "Ugly"
        }
    ]
    results = tc_dc._validate_tags(SAMPLE_TAG_PROFILE, test_tags)
    assert len(results['failures']) == 1
    assert len(results['warnings']) == 1
    assert tc_dc.MESSAGES['missingTag'].format('required', 'Bad') in results['failures']
    assert tc_dc.MESSAGES['missingTag'].format('desired', 'Good') in results['warnings']
