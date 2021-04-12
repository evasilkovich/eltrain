import requests
import os


def handler(event, context):
    print(event)
    execution = event['execution']
    url = os.environ.get('WEBHOOK_URL')
    print(url)
    print(execution)

    try:
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, data = {'execution':execution}, headers=headers)
        print(r.status_code)
        return
    except Exception as err:
        print(f'Error occurred: {err}')
