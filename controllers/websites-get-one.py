import json
import boto3
import os
import urllib.parse
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('ELTRAIN_JOBS_TABLE'))


def handler(event, context):

    print(event)

    try:

        url = event['pathParameters']['domain_name']
        print(url)
        parsed_url =  urllib.parse.unquote(url)
        print(parsed_url)

        response = table.query(
            KeyConditionExpression=Key('domain_name').eq(parsed_url),
            ScanIndexForward=False,
            IndexName='CreatedDateIndex'
        )
        items = response['Items']
        print(items)


        response = {
            "statusCode": 200,
            "body": json.dumps({'items': items})
        }

        return response

    except Exception as err:
        print(f'Error occurred: {err}')
