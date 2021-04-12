import json
import boto3
import os

client = boto3.client('stepfunctions')


def handler(event, context):

    print(event)
    print(context)
    print(event['pathParameters'])
    print(event['pathParameters']['job_id'])

    job_id = event['pathParameters']['job_id']
    result = client.describe_execution(
        executionArn=job_id
    )

    start_d = result['startDate'].isoformat()
    stop_d = result['stopDate'].isoformat()
    print(start_d)
    print(stop_d)
    result.update({'startDate':start_d})
    result.update({'stopDate':stop_d})

    print(result)

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
