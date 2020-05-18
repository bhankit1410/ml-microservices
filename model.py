"""
model.py
--------
Implements the model for our website
"""

import json


def load_file():
    with open("sample.json") as f:
        return json.load(f)


db = load_file()
