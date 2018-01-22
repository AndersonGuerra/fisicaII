# Carrega as bibliotecas
import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
import Adafruit_DHT
import Adafruit_CharLCD as LCD

 
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
 
GPIO.setmode(GPIO.BCM)
 
# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25
pino_led = 17

# Pinos LCD x Raspberry (GPIO)
lcd_rs        = 18
lcd_en        = 23
lcd_d4        = 12
lcd_d5        = 16
lcd_d6        = 20
lcd_d7        = 21
lcd_backlight = 4

# Define numero de colunas e linhas do LCD
lcd_colunas = 16
lcd_linhas  = 2

# Inicializa o LCD nos pinos configurados acima
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                           lcd_d6, lcd_d7, lcd_colunas, lcd_linhas,
                           lcd_backlight)

lcd.message('nossa')

# set up GPIO output channel
GPIO.setup(pino_led, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Recebeu a mensagem: {}'.format(command))
    
    if command == 'on':
        GPIO.output(pino_led,GPIO.HIGH)
        bot.sendMessage(chat_id, 'O led foi aceso')       
    elif command =='off':
        GPIO.output(pino_led,GPIO.LOW)
        bot.sendMessage(chat_id, 'O led foi desligado')
    elif command == 'temperatura':
        umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
       # Caso leitura esteja ok, mostra os valores na tela
        if umid is not None and temp is not None:
            mensagem = "Temperatura = {0:0.1f}  Umidade = {1:0.1f}n".format(temp, umid)
        else:
            # Mensagem de erro de comunicacao com o sensor
            mensagem ="Falha ao ler dados do DHT11."
        bot.sendMessage(chat_id, mensagem)

bot = telepot.Bot('463886559:AAEC84FJHOWCrJ0RfdERfLJf_f8G67dIMLA') 
bot.message_loop(handle)
print('Aguardando comando')

while 1:
     time.sleep(10)
