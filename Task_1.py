import requests


def get_a_winner():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    data = list(response.json())
    my_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
    for k in my_dict.keys():
        for i in data:
            if i['name'] == k:
                my_dict[k] = i['powerstats']['intelligence']
    result = max(my_dict, key=my_dict.get)
    print(f'Ответ: {result} c показателями интеллекта - {my_dict[result]}')


if __name__ == '__main__':
    get_a_winner()