from werkzeug import Request, ClosingIterator
from werkzeug.exceptions import HTTPException

from webcollab.utils import url_map
from webcollab import views

class WebCollab(object):
    '''The WSGI callable'''
    def __call__(self, environ, start_response):
        request = Request(environ)
        
        adapter = url_map.bind_to_environ(environ)
        
        try:
            endpoint, values = adapter.match()
            handler = getattr(views, endpoint)
            response = handler(request, **values)
        except HTTPException, e:
            response = e
        
        return response(environ, start_response)