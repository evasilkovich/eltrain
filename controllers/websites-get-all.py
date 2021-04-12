import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('ELTRAIN_JOBS_TABLE'))


def handler(event, context):

    print(event)
    print(context)

    response = table.scan()
    items = response['Items']
    print(items)

    response = {
        "statusCode": 200,
        "body": json.dumps({"items": items})
    }

    return response
