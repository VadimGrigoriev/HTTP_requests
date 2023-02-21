import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_link(self):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        file_name = path_to_file.split('/')[-1]
        params = {'path': f'/{file_name}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_link = self.get_link()
        response = requests.put(upload_link, headers=self.get_headers(), data=open(file_path, 'rb'))
        if response.status_code == 201:
            print('Запрос прошел успешно')
        else:
            print(f'Ошибка {response.status_code}')


if __name__ == '__main__':
    path_to_file = '...'
    token = '...'
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
