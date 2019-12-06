author = 'ahmad'
email = 'mbuhyaa0@gmail.com'
app_title = 'menggunakan python untuk memanggil django API'
print (f'{app_title} oleh {author}')

url = 'http://127.0.0.1:8000/'
import requests

response = requests.get (url)
print (response)
