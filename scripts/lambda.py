import json
import github
import os
import boto3

ssm = boto3.client('ssm', region_name='us-east-1')

def lambda_handler(event, context):
    alphavantage = ssm.get_parameter(Name="/simple-stock-tracer/testing-value2", WithDecryption=True)['Parameter']['Value']
    
