import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def translate(event, context):
    print('This is the event')
    print(event)
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )


    Text_ = result['Item']
    SourceLanguageCode_ = event['pathParameters']['from']
    TargetLanguageCode_ = event['pathParameters']['to']
    
    trnslt = boto3.client('translate', region_name='us-east-1', use_ssl=True)
    translation = trnslt.translate_text(Text=Text_, SourceLanguageCode=SourceLanguageCode_, TargetLanguageCode=TargetLanguageCode_)
    print('This is a translation:')
    print(translation)
    
        # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result.get(‘TranslatedText’),
                           cls=decimalencoder.DecimalEncoder)
    }
#class translation():
#    def __init__(self):
#        self.instance = boto3.client('translate', region_name='us-east-1', use_ssl=True)
#        
#    def get_item(self, id):
#        pass
#    
#    def translate_item(self, Text_, SourceLanguageCode_='auto', TargetLanguageCode_='en'):
#        return self.instance.translate_text(Text=Text_, SourceLanguageCode=SourceLanguageCode_, TargetLanguageCode=TargetLanguageCode_)
#        
#        
#
#def translate():
#    action = translate()
#    translation = action.translate_item('Hola, soy Adrian')
#    print(translation)
