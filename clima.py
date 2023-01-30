import requests

key = 'link da key'
lat  = -8.02044
lon = -34.9817
link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&lang=pt_br'

requisicao = requests.get(link)
requisicao_geral = requisicao.json()
cidade = requisicao_geral['name']
tempo = requisicao_geral['weather'][0]['description']
temperatura = requisicao_geral['main']['temp'] - 273.15
temperaturamin = requisicao_geral['main']['temp_min'] - 273.15
temperaturamax = requisicao_geral['main']['temp_max'] - 273.15
umidade = requisicao_geral['main']['humidity']
print(cidade)
print('Tempo:', tempo)
print(f'Temperatura, {temperatura}, ºC')
print(f'Max:, {temperaturamax}, ºC')
print(f'Min, {temperaturamin}, ºC')
print(f'Umidade, {umidade}')
