import json
import boto3
import os

client = boto3.client('stepfunctions')


def handler(event, context):

    print(event)
    try:
        result = client.list_executions(
            stateMachineArn=os.environ.get('ELTRAIN_STEP_FUNCTIONS')
        )
        print(result)

        executions = result['executions']
        for d in executions:
            start_d = d['startDate'].isoformat()
            stop_d = d['stopDate'].isoformat()
            print(start_d)
            print(stop_d)
            d.update({'startDate':start_d})
            d.update({'stopDate':stop_d})

        print(executions)

        response = {
            "statusCode": 200,
            "body": json.dumps({'executions':executions})
        }

        return response

    except Exception as err:
        print(f'Error occurred: {err}')
