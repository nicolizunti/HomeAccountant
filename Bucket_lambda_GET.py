import json
import boto3
def lambda_handler(event, context):
  # TODO implement
  dynamodb = boto3.resource('dynamodb')
  tableBucket = dynamodb.Table('Buckets')
  response = tableBucket.scan()
  return {
    'statusCode': 200,
    'body': response['Items']
  }