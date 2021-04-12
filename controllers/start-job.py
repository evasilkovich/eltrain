import json
import boto3
import os

client = boto3.client('stepfunctions')


def handler(event, context):

    print(event)
    print(context)
    print(event["body"])
    print(os.environ.get('ELTRAIN_STEP_FUNCTIONS'))

    try:

        body = json.loads(event["body"])
        print(body)
        if not body or not body['sites']:
            response = {
                "statusCode": 400,
                "body": json.dumps({'message':'empty payload'})
            }
            return response

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

    except Exception as err:
        print(f'Error occurred: {err}')
