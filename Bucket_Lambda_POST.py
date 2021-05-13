import json
import boto3

#That's the lambda handler, you can not modify this method
# the parameters from JSON body can be accessed like deviceId = event['deviceId']

def lambda_handler(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    # Getting the table the table Temperatures object
    tableBucket = dynamodb.Table('Buckets')
    
    # Getting parameters from JSON body
    name = event['name']
    
    # Putting a try/catch to log to user when some error occurs
    try:
        
        tableBucket.put_item(
           Item={
                'name': name
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully inserted new Bucket!')
        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving new Bucket')
        }