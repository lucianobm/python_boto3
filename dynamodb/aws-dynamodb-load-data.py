import boto3
import json

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Games')

with open("gamedata.json") as json_file:
    games = json.load(json_file)
    for game_name in games:
        game = game_name['game']
        developer = game_name['developer']

        print("Adding game:", game, developer)

        table.put_item(
           Item={
               'Game': game,
               'Developer': developer,
            }
        )