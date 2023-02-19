import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.query(
    ExpressionAttributeValues={
        ':v1': {
            'S': 'Starcraft',
        },
    },
    KeyConditionExpression='Game = :v1',
    ProjectionExpression='Developer',
    TableName='Games',
)

print(response)