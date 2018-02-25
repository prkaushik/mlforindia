import boto3

client = boto3.client('dynamodb')
paginator = client.get_paginator('scan')

for page in paginator.paginate():
    # do something