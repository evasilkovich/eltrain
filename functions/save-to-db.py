# import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

def handler(event, context):

    print(event)
    print(context)

    table = dynamodb.Table(os.environ.get('ELTRAIN_JOBS_TABLE'))
    response = table.put_item(
        Item={
            'domain_name': event['site_response']['url'],
            'created_date': datetime.now().isoformat(),
            'content': event['site_response']['content'],
            'requested_time': str(event['site_response']['time']),
            'execution_name': event['execution']
        }
    )
    return response
