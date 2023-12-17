import boto3
import random


def lambda_handler(event, context):
    return random_item()


def random_item():
    # Create a DynamoDB client
    dynamodb = boto3.resource('dynamodb')

    # Reference your DynamoDB table
    table = dynamodb.Table('StarbucksDrinksCatalog')

    # Scan the table to get only the keys (BeverageID)
    response = table.scan(ProjectionExpression="BeverageID")
    keys = response['Items']

    # Select a random key if keys are present
    if keys:
        random_key = random.choice(keys)['BeverageID']

        # Fetch the full item for the selected key
        result = table.get_item(Key={'BeverageID': random_key})
        return result.get('Item', {})
    else:
        return {'message': 'No keys found in the table'}
