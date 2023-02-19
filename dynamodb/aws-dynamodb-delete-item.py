import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_item(
    Key={
        'Game': {
            'S': 'DeadSpace',
        },
        'Developer': {
            'S': 'EASports',
        },
    },
    TableName='Games',
)

print(response)