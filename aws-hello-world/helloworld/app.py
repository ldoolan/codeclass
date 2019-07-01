from chalice import Chalice
import time
from urllib.parse import parse_qs


app = Chalice(app_name='helloworld')


# @app.route('/')
# def  index():
#     return {'goodbye': 'me'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

@app.route('/time',
  methods = ['POST'],
  content_types=['application/x-www-form-urlencoded']
  )
def hello_there():
    # You can access the text the user typed after the command too:
    time = time.localtime(dst=1)
    hour = str(time[3])
    minute = str(time[4])
    sec = str(time[5])
    time_to_return = '{}:{}:{}'.format(hour, minute, sec)
    params = parse_qs(app.current_request.raw_body.decode())
    user_text = params['text']
    if user_text != ['time']:
        return {'response_type': 'in_channel',
        'text': 'invalid'}
    else:
        return {
        'response_type': 'in_channel',
        'text': '{}'.format(time_to_return)}
   
