#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun
from pyfcm import FCMNotification

application = Flask(__name__)

push_service = FCMNotification(
    api_key='AAAAFxr6tmI:APA91bEGjpVkHoeFbVb5H6D9PtCPsmOgTml7FU0NqSWmzEPgJm1hlzTktQUr3mmhmCBLC_BH34otKd0wR_48wUQHPCS80qnqiYYd-e9o7QjYJvirLFUYXAlgn0IzfdsS-VqPeKFNMDMI')
mToken = 'eimH40xBV2k:APA91bFbUXMNZMV3niYDqzoCihPQdv9KZea9mvSvwBDSyDAWdL5CMJI0OQzptxKI57UYE9Aw9f8SIoCJ8erXp_nIFkt7clGvv74AkywnIQD948rvNb05Md7VWxhHZc3q5ogpO94C4szx'
nth = 0


@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)


@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)


@application.route('/push', methods=['GET'])
def push():
    global nth
    nth += 1
    registration_id = mToken

    message_title = "Test title"
    message_body = "Test body"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)
    print(push_service.send_request_responses)
    print(result)
    return Response(json.dumps({'Output': result}), mimetype='application/json', status=200)


if __name__ == '__main__':
    flaskrun(application)
