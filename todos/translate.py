import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def translate(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id'],
        }
    )

    Text_ = result['Item']
    SourceLanguageCode_ = event['pathParameters']['from']
    TargetLanguageCode_ = event['pathParameters']['to']
    
    trnslt = boto3.client('translate', 
                          region_name='us-east-1', 
                          use_ssl=True)
    translation = trnslt.translate_text(Text=Text_, 
                                        SourceLanguageCode=SourceLanguageCode_, 
                                        TargetLanguageCode=TargetLanguageCode_)
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
##        "body": json.dumps(result.get(‘TranslatedText’),
                           cls=decimalencoder.DecimalEncoder)
    }

