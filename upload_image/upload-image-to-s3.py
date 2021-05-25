import json
import base64
import boto3

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    
    s3 = boto3.client('s3')
    s3_bucket = 'fit5225-image-bucket'
    file_name = event['headers']['content-disposition']
    file_name = file_name[10:-1]
    encoded_file_content = event['content']
    decoded_content = base64.b64decode(encoded_file_content)
    
    
    s3_upload = s3.put_object(Bucket=s3_bucket, Key=file_name, Body=decoded_content)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'{file_name} has been saved into {s3_bucket} successfully!')
    }
