import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Game',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Developer',
            'AttributeType': 'S',
        },
    ],
    TableName='Games',
    KeySchema=[
        {
            'AttributeName': 'Game',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'Developer',
            'KeyType': 'RANGE'  #Sort key
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print(response)