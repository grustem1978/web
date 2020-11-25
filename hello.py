def simple_app(environ, start_response):

    
    #(dict, callable( status: str,
    #                 headers: list[(header_name: str, header_value: str)]))
    #              -> body: iterable of strings
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return 'Hello world!\n'

def app(environ, start_response):
    """Simplest possible application object"""
    data = 'Hell'
    body = environ['QUERY_STRING'].replace('&','\n')
    #body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
    start_response(status, response_headers)
    return [body]
