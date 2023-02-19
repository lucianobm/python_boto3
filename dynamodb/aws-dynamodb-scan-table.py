import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.scan(
    ExpressionAttributeNames={
        '#GA': 'Game',
        '#DE': 'Developer',
    },
    ExpressionAttributeValues={
        ':a': {
            'S': 'Blizzard',
        },
    },
    FilterExpression='Developer = :a',
    ProjectionExpression='#DE, #GA',
    TableName='Games',
)

print(response)