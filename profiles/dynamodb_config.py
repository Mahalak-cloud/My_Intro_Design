import boto3

dynamodb = boto3.resource('dynamodb', region_name='your-region')
table = dynamodb.Table('Profiles')

