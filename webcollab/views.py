import os

from werkzeug import Response
from werkzeug.exceptions import NotFound, BadRequest, MethodNotAllowed

from webcollab.utils import expose
from webcollab.utils import datadir

@expose('/messages/')
def index(request):
    listdir = '\n'.join(os.listdir(datadir))
    return Response(listdir)
    
@expose('/messages/<string:name>')
def message(request, name):
    response = Response()
    path = os.path.join(datadir, str(name))
    
    if request.method == 'HEAD':
        pass # we only need to return headers
        
    elif request.method == 'GET':
        try:
            response.data = open(path, 'r').read()
        except IOError, e:
            print e
            raise NotFound()
                
    elif request.method == 'POST':
        try:
            print request.form['message']
            open(path, 'w').write(request.form['message'])
        except IOError, e:
            raise BadRequest()
            
            
    elif request.method == 'DELETE':
        try:
            os.remove(path)
        except IOError, e:
            raise NotFound()
            
    else:
        raise MethodNotAllowed()
    
    return response