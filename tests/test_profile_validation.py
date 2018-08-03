#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Use a profile to validate data."""

import json
import os

import pytest

from tc_dc import tc_dc

from .utility import _read_file


@pytest.fixture
def profile_1():
    return _read_file(os.path.abspath(os.path.join(os.path.dirname(__file__), "./data/profile_1.json")))


@pytest.fixture
def data_1_a():
    return _read_file(os.path.abspath(os.path.join(os.path.dirname(__file__), "./data/data_1_a.json")))


@pytest.fixture
def data_1_b():
    return _read_file(os.path.abspath(os.path.join(os.path.dirname(__file__), "./data/data_1_b.json")))


def test_valid_profile_1(profile_1, data_1_a):
    results = tc_dc._apply_profile(profile_1, data_1_a)
    assert len(results['failures']) == 0
    assert len(results['warnings']) == 0


def test_invalid_profile_1(profile_1, data_1_b):
    results = tc_dc._apply_profile(profile_1, data_1_b)
    assert len(results['failures']) == 2
    assert len(results['warnings']) == 1
    assert 'Missing attribute of type "Source" with the value "https://threatconnect.com/blog"' in results['failures']
    assert 'Missing required tag "Ugly"' in results['failures']
    assert 'Expected this item to be associated with 1 Adversary, but found no associations with Adversary were found.' in results['warnings']


def test_nonexistent_attibutes(profile_1):
    results = tc_dc._apply_profile(profile_1, [{}])
    assert len(results['failures']) == 3
    assert len(results['warnings']) == 0
    assert 'Expected required attributes, but no attributes found.' in results['failures']
    assert 'Expected required associations, but no associations found.' in results['failures']
    assert 'Expected required tags, but no tags found.' in results['failures']
