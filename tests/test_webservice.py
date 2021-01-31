#!/usr/bin/env python3

import os
import tempfile
import pytest
import json
from kmt_calculator.utils.webservice import app as flask_app

"""Unit tests for the webservice application
"""


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index_calculator(app, client):
    # Setup
    desired_status_code = 200
    desired_text = "Welcome to the KMT Calculator Flask Application"

    # Exercise
    response = client.get("/calculator")
    actual_status_code = response.status_code
    actual_text = response.get_data(as_text=True)

    # Verify
    assert actual_status_code == desired_status_code
    assert actual_text == desired_text


def test_index(app, client):
    # Setup
    desired_status_code = 404

    # Exercise
    response = client.get("/")
    actual_status_code = response.status_code

    # Verify
    assert actual_status_code == desired_status_code


def test_app_infix(app, client):
    # Setup
    expression = "( 1 + ( 2 * 3 ) )"
    result = 7
    headers = {"Content-Type": "application/json"}
    expression_dict = {"expression": expression}
    desired = f"{expression} evaluates to: {result} \n"

    # Exercise
    response = client.post("/calculator/infix", data=json.dumps(expression_dict), headers=headers)
    actual = response.get_data(as_text=True)

    # Verify
    assert actual == desired


def test_app_prefix(app, client):
    # Setup
    expression = "+ * 1 2 3"
    result = 5
    headers = {"Content-Type": "application/json"}
    expression_dict = {"expression": expression}
    desired = f"{expression} evaluates to: {result} \n"

    # Exercise
    response = client.post("/calculator/prefix", data=json.dumps(expression_dict), headers=headers)
    actual = response.get_data(as_text=True)

    # Verify
    assert actual == desired
