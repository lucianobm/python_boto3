import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.batch_write_item(
    RequestItems={
        'Games': [
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Starcraft',
                        },
                        'Developer': {
                            'S': 'Blizzard',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Diablo',
                        },
                        'Developer': {
                            'S': 'Blizzard',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Game': {
                            'S': 'Overwatch',
                        },
                        'Developer': {
                            'S': 'Blizzard',
                        },
                    },
                },
            },
        ],
    },
)

print(response)