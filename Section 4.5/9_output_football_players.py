import zipfile
import json


def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False


with zipfile.ZipFile('data.zip', 'r') as zip_file:
    data = zip_file.infolist()
    players = []
    arsenals_players = []

    for some_file in data:
        try:
            file = zip_file.read(some_file).decode('utf-8')

            if is_correct_json(file):
                players.append(json.loads(file))
        except:
            continue

    for player in players:
        if player['team'] == 'Arsenal':
            arsenals_players.append(f'{player["first_name"]} {player["last_name"]}')

    print(*sorted(arsenals_players), sep='\n')