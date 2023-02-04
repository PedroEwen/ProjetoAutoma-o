import datetime
from tkinter import *
import requests
def hora():
    geral = datetime.datetime.now()
    horastr = geral.strftime('%c')
    texto_tela['text'] = f'''
    {horastr}'''

def clima():
    key = 'bcae6f5df366d07aa9063949701c6665'
    lat = -8.02044
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

    texto_tela['text'] = f''' 
City: {cidade} 
Weather: {tempo} 
Humdity: {umidade}
Temperature: {'%.2f' % temperatura} 
-> Max: {'%.2f' % temperaturamax}
-> Min: {'%.2f' % temperaturamin}'''

tela = Tk()
tela.title('Central de Comandos')
tela.geometry('500x300')
botao_hora = Button(tela, text='Hora', command=hora)
botao_hora.grid(column=1, row=2)
botao = Button(tela, text='Clima', command=clima)
botao.grid(column=1, row=3)
texto_tela = Label(tela, text='')
texto_tela.grid(column=5, row=4)
tela_sair = Button(tela, text='Sair', command='')
tela_sair.grid(column=1, row=6)
tela_sair['command'] = tela_sair.quit
tela.mainloop()
