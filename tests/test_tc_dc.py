#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tc_dc
----------------------------------

Tests for `tc_dc` module.
"""

import json
import os

import pytest

from tc_dc import tc_dc


def _read_file(file_path):
    """Read a file."""
    with open(file_path, 'r') as f:
        if file_path.endswith('.json'):
            return json.load(f)
        else:
            return f.read()


@pytest.fixture
def rules_1():
    return _read_file(os.path.abspath(os.path.join(os.path.dirname(__file__), "./data/sample_rules1.json")))


def test_rule(rules_1):
    assert len(rules_1) > 50
