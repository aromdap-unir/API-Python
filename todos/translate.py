import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


class translation():
    def __init__(self):
        self.instance = boto3.client('translate', region_name='us-east-1', use_ssl=True)
        
    def get_item(self, id):
        pass
    
    def translate_item(self, Text_, SourceLanguageCode_='auto', TargetLanguageCode_='en'):
        return self.instance.translate_text(Text=Text_, SourceLanguageCode=SourceLanguageCode_, TargetLanguageCode=TargetLanguageCode_)
        
        

def translate():
    action = translate()
    translation = action.translate_item('Hola, soy Adrian')
    print(translation)