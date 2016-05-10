def app(environ, start_response):
    # method = environ['REQUEST_METHOD']
    # params = environ['QUERY_STRING']
    start_response('200 OK', [('Content-Type', 'text/html')])

    response = '<!DOCTYPE html><head><meta charset="utf-8"></head><body>' 
               # 'Привет, мир!<br>Метод: {0}<br>Параметры: {1}</body></html>'.format(method, params)

    return [response]