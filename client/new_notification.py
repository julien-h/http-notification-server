# use this code to send a new notification from python

endpoint_new = 'http://127.0.0.1:9998/new'

def b64(string_data):
    import base64
    return base64.b64encode(string_data.encode('utf8')).decode('utf8')

def send_notification(title, description = '', data = ''):
    from urllib.parse import urlencode
    from urllib.request import urlopen
    import json

    query_str = urlencode({
        'title':title,
        'description': description,
        'data': b64(data)
    }, doseq=True)

    response = urlopen(endpoint_new + '?' + query_str)
    return json.load(response)