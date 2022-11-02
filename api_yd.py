import requests

TOKEN_YD = ''
url_yd = 'https://cloud-api.yandex.net/v1/disk/'
name_folder = "image"

def get_headers(TOKEN_YD):
    return {
        'Context-Type': 'application/json',
        'Authorization': f'OAuth {TOKEN_YD}'
    }

def put_resources(TOKEN_YD, url_yd, name_folder):
    url_resourses = f'{url_yd}resources/'
    headers = get_headers(TOKEN_YD)
    params = {
        'path': f'/{name_folder}',
        'fields': 'size, name'
    }
    put_res = requests.put(url_resourses, params = params, headers = headers)
    folder = requests.get(url_resourses, params=params, headers=headers)
    status = folder.status_code
    return status, folder.json()['name']

if __name__ == '__main__':
    status, folder = put_resources(TOKEN_YD, url_yd, name_folder)
    print(status)
    print(folder)