import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.put_item(
    Item={
        'Game': {
            'S': 'Starcraft',
        },
        'Developer': {
            'S': 'Blizzard',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Games',
)

print(response)