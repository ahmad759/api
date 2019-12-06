author = 'ahmad'
email = 'mbuhyaa0@gmail.com'
app_title = 'menggunakan python untuk memanggil django API'
print (f'{app_title} oleh {author}')

url = 'http://127.0.0.1:8000/'
import requests

response = requests.get (url)
print (response)

if response.status_code == 200:
    print ('Koneksi berhasil')

    url_api = f'{url}api/v1/stats/'
    response = requests.get (url_api)
    if response.status_code == 200:
        import json
        data = json.loads (response.text)
        data_terakhir = data[len(data) - 1 ]

        suhu = data_terakhir ['suhu']
        humidity = data_terakhir ['humidity']
        print (f'Hasil Percobaan sensor : suhu = {suhu}, humidity = {humidity}')
