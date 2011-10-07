# -*- coding: utf-8 -*-
"""
    Fake Ping plugin a-la "Hello World".

    Can be used as plugin template. For sure.
"""
import re

info = {
    "name": "ping",
    "description": """Some long and boring plugin description.
    And yes - it can be multiline! I hope so...""",
    "author": "Alexey \"NilColor\" Blinov",
    "version": "0.0.1",
    "main": "Ping"
}

class Ping(object):
    def __init__(self, *args, **kwargs):
        pass

    def get_link(self):
        return (
            re.compile(r'^ping', re.L | re.I),
            self.ping_callback,
        )

    def ping_callback(self, cmd, message):
        return "PONG. Hell'yes!"
