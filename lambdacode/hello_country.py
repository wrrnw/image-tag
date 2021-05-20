import json
import datetime
import requests
def lambda_handler(event, context):
  print ('event:' + event)
  data = {
    'output': 'Hello from ' + event['Country'],
    'timestamp': datetime.datetime.utcnow().isoformat()
  }
  return {
    'statusCode:': 200,
    'body': json.dumps(data),
    'headers': {'Content-Type': 'application/json'}
  }