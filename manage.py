#!/usr/bin/env python
import os

from werkzeug import script

def make_app():
    from werkzeug import SharedDataMiddleware
    
    from webcollab.app import WebCollab
    from webcollab.utils import datadir
    
    return SharedDataMiddleware(WebCollab(), {'/':  os.path.dirname(__file__)})

def make_shell():
    from webcollab import utils
    app = make_app()
    return locals()

action_runserver = script.make_runserver(make_app, use_reloader=True)
action_shell = script.make_shell(make_shell)

script.run()
