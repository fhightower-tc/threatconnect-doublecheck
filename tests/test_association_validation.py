#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Use a profile to validate associations."""

from tc_dc import tc_dc


SAMPLE_ASSOCIATIONS_PROFILE = {
    "required": [{
            "type": "Document",
            "count": 2
        },
        {
            "type": "File",
            "count": 0
        },
        {
            "type": "Host"
        }
    ],
    "desired":[{
            "type": "Adversary",
            "count": 1
        }
    ]
}


def test_successful_association_validation():
    """Make sure a valid association profile passes the test."""
    test_associations = [{
        'type': 'Document',
        'name': 'blahblah.txt'
    }, {
        'type': 'Document',
        'name': 'blahblah.pdf'
    }, {
        'type': 'Host',
        'name': 'hightower.space'
    }, {
        'type': 'Adversary',
        'name': 'Bad guy'
    }]
    results = tc_dc._validate_associations(SAMPLE_ASSOCIATIONS_PROFILE, test_associations)
    assert len(results['failures']) == 0
    assert len(results['warnings']) == 0


def test_successful_association_validation_2():
    """This test adds another host to make sure that associations with no count specified in the profile are handled correctly."""
    test_associations = [{
        'type': 'Document',
        'name': 'blahblah.txt'
    }, {
        'type': 'Document',
        'name': 'blahblah.pdf'
    }, {
        'type': 'Host',
        'name': 'hightower.space'
    }, {
        'type': 'Host',
        'name': 'deep.space'
    }, {
        'type': 'Adversary',
        'name': 'Bad guy'
    }]
    results = tc_dc._validate_associations(SAMPLE_ASSOCIATIONS_PROFILE, test_associations)
    assert len(results['failures']) == 0
    assert len(results['warnings']) == 0


def test_assoc_count_failure():
    """Make sure missing associations are handled correctly."""
    test_associations = [{
        'type': 'Document',
        'name': 'blahblah.txt'
    }, {
        'type': 'Host',
        'name': 'hightower.space'
    }, {
        'type': 'Adversary',
        'name': 'Bad guy'
    }]
    results = tc_dc._validate_associations(SAMPLE_ASSOCIATIONS_PROFILE, test_associations)
    assert len(results['failures']) == 1
    assert len(results['warnings']) == 0
    assert results['failures'][0] == 'Incorrect number of Document associations found. Expected 2, but only found 1.'


def test_assoc_precense_failure():
    """Test validation of associations with one missing."""
    test_associations = [{
        'type': 'Document',
        'name': 'blahblah.txt'
    }, {
        'type': 'Document',
        'name': 'blahblah.pdf'
    }, {
        'type': 'Adversary',
        'name': 'Bad guy'
    }]
    results = tc_dc._validate_associations(SAMPLE_ASSOCIATIONS_PROFILE, test_associations)
    assert len(results['failures']) == 1
    assert len(results['warnings']) == 0
    assert results['failures'][0] == 'Expected at least one association with a Host, but no such association was found.'


def test_assoc_desired_missing():
    """Test validation of associations with one missing."""
    test_associations = [{
        'type': 'Document',
        'name': 'blahblah.txt'
    }, {
        'type': 'Document',
        'name': 'blahblah.pdf'
    }, {
        'type': 'Host',
        'name': 'hightower.space'
    }]
    results = tc_dc._validate_associations(SAMPLE_ASSOCIATIONS_PROFILE, test_associations)
    assert len(results['failures']) == 0
    assert len(results['warnings']) == 1
    assert results['warnings'][0] == 'Expected this item to be associated with 1 Adversary, but found no associations with Adversary were found.'
