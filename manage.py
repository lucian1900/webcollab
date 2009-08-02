#!/usr/bin/env python
from werkzeug import script

def make_app():
    from webcollab.app import WebCollab
    return WebCollab()

def make_shell():
    from webcollab import utils
    app = make_app()
    return locals()

action_runserver = script.make_runserver(make_app, use_reloader=True)
action_shell = script.make_shell(make_shell)

script.run()
