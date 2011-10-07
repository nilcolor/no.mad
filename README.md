What is this?
=============
This is [Campfire][campfire] bot that can be used like GitHub's Hubot.

Usage
=====
It builds on top of [pyfire][] - Campfire API wrapper. This means you have to have `pyfire`.
You can install it in your `PYTHONPATH` or you can simply `git clone https://github.com/mariano/pyfire.git`
it into `vendor` folder.  
Oh, and pyfire itself depends on [twisted][] for streaming support. If you are using MacOS X 10.5+ -- it's pre-installed.
Otherwise -- check Twisted's site for instructions.  
When all requirements are met, issue this command:

    export CAMPFIRE_ROOM_ID=_room_id_;export CAMPFIRE_API_KEY=_api_key_;export CAMPFIRE_ACCOUNT=_chat_subdomain_;python src/nomad.py

within `no.mad` folder and your bot is ready. Try to put `nomad ping` command in Campfire's chat - and you will see.

[campfire]: http://campfirenow.com
[pyfire]: https://github.com/mariano/pyfire
[twisted]: http://twistedmatrix.com