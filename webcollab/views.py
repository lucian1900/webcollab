import os

from werkzeug import Response
from werkzeug.exceptions import NotFound, BadRequest, MethodNotAllowed

from webcollab.utils import expose

tempdir = '/tmp/webcollab'
if not os.path.isdir(tempdir):
    os.mkdir(tempdir)

@expose('/')
def index(request):
    listdir = '\n'.join(os.listdir(tempdir))
    return Response(listdir)
    
@expose('/<string:name>')
def message(request, name):
    response = Response()
    path = os.path.join(tempdir, str(name))
    
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