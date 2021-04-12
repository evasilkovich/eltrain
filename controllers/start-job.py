import json
import boto3
import os

client = boto3.client('stepfunctions')


def handler(event, context):

    print(event)
    print(context)
    print(event["body"])
    print(os.environ.get('ELTRAIN_STEP_FUNCTIONS'))
    body = json.loads(event["body"])
    print(body)

    result = client.start_execution(
        stateMachineArn=os.environ.get('ELTRAIN_STEP_FUNCTIONS'),
        input=event["body"]
    )
    print(result)

    response = {
        "statusCode": 200,
        "body": json.dumps({'executionArn':result['executionArn']})
    }

    return response
