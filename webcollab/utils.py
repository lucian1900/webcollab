import os

from werkzeug.routing import Map, Rule

url_map = Map()
def expose(rule, **kw):
    def decorate(f):
        kw['endpoint'] = f.__name__
        url_map.add(Rule(rule, **kw))
        return f
    return decorate

datadir = '/tmp/webcollab'
if not os.path.isdir(datadir):
    os.mkdir(datadir)