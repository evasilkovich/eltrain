import json


def handler(event, context):

    print(event)
    print(event["body"])

    response = {
        "statusCode": 200,
    }

    return response
