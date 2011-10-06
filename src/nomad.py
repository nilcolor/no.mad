#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import re
import hashlib
PROJECT_ROOT = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
VENDOR_ROOT = '%s/vendor' % PROJECT_ROOT

try:
    import pyfire
except ImportError, e:
    sys.path.insert(0, '%s/pyfire' % VENDOR_ROOT)
    import pyfire

NOMAD = re.compile(r'^nomad\s', re.I | re.L)
CAMPFIRE_ROOM_ID=os.environ["CAMPFIRE_ROOM_ID"]
CAMPFIRE_API_KEY=os.environ["CAMPFIRE_API_KEY"]
CAMPFIRE_ACCOUNT=os.environ["CAMPFIRE_ACCOUNT"]

demons = {}

def incoming(message):
    user = ""
    if message.user:
        user = message.user.name

    if message.is_joining():
        print "--> %s ENTERS THE ROOM" % user
    elif message.is_leaving():
        print "<-- %s LEFT THE ROOM" % user
    elif message.is_tweet():
        print "[%s] %s TWEETED '%s' - %s" % (
            user,
            message.tweet["user"],
            message.tweet["tweet"],
            message.tweet["url"]
        )
    elif message.is_text():
        print "[%s] %s" % (user, message.body)
        if NOMAD.match(message.body):
            command = NOMAD.split(message.body)[1]

            for nick in demons:
                for demon in demons[nick]:
                    if demon['token'].match(command):
                        to_say = demon['cb'](command)
                        assert to_say is not None, "Plugin callback HAVE TO RETURN SOMETHING!"
                        room.speak(to_say)
            try:
                to_say
            except Exception, e:
                room.speak('I doesn\'t know this command yet: "%s"' % command)
    elif message.is_upload():
        print "-- %s UPLOADED FILE %s: %s" % (
            user,
            message.upload["name"],
            message.upload["url"]
        )
    elif message.is_topic_change():
        print "-- %s CHANGED TOPIC TO '%s'" % (user, message.body)

def error(e):
    print("Stream STOPPED due to ERROR: %s" % e)
    print("Press ENTER to continue")

from plugin_loader import PluginLoader

pm = PluginLoader("%s/src/plugins" % PROJECT_ROOT)

for p in pm.plugins:
    x = pm.init_plugin(p)
    token, cb = x.get_link()
    hsah = hashlib.md5(token.pattern).hexdigest()
    pkg = {
        "token": token,
        "cb": cb,
    }
    current_list = demons.get(hsah, list())
    current_list.append(pkg)
    demons[hsah] = current_list

# print "Ups! Fake run! Fuck run!"
campfire = pyfire.Campfire(CAMPFIRE_ACCOUNT, CAMPFIRE_API_KEY, "x", ssl=True)
room = campfire.get_room(CAMPFIRE_ROOM_ID)
room.join()
stream = room.get_stream(error_callback=error)
stream.attach(incoming).start()
raw_input("Waiting for messages (Press ENTER to finish)\n")
stream.stop().join()
room.leave()
