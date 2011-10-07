# -*- coding: utf-8 -*-
"""
    Fake Hello World plugin.

    Can be used as plugin template. For sure.
"""
import re

info = {
    "name": "hello_world",
    "description": """Some long and boring plugin description.
    And yes - it can be multiline! I hope so...""",
    "author": "Alexey \"NilColor\" Blinov",
    "version": "0.0.1",
    "main": "Fake"
}

class Fake(object):
    def __init__(self, *args, **kwargs):
        pass

    def get_link(self):
        return (
            re.compile(ur'^привет', re.L | re.I),
            self.hello_callback,
        )

    def hello_callback(self, cmd, message):
        message.room.speak("Plugin can talk too!")
        message.room.speak(u"Привет, дорогой %s" % message.user.name)
