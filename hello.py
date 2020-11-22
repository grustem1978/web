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
    data = 'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
