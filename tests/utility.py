#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utility functions for tests."""

import json


def _read_file(file_path):
    """Read a file."""
    with open(file_path, 'r') as f:
        if file_path.endswith('.json'):
            return json.load(f)
        else:
            return f.read()
