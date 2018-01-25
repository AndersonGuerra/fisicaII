# Carrega as bibliotecas
import time
import telepot
import RPi.GPIO as GPIO
import Adafruit_DHT
 
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11

# Configura a numeração dos pinos 
GPIO.setmode(GPIO.BCM)
 
# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25
pino_led = 17
pino_buzzer = 21

# configura uma GPIO como saída
GPIO.setup(pino_led, GPIO.OUT)
GPIO.setup(pino_buzzer, GPIO.OUT)

def handle(msg):
    chat_id = msg["chat"]["id"]
    command = msg["text"].lower()

    print ("Recebeu a mensagem: {}".format(command))
    
    if command == "on":
        if (GPIO.input(pino_led) == 1):
            bot.sendMessage(chat_id, "O led já está aceso")
            GPIO.output(pino_buzzer, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(pino_buzzer, GPIO.LOW)
        else:
            GPIO.output(pino_led,GPIO.HIGH)
            bot.sendMessage(chat_id, 'U+1F601')
    elif command =="off":
        if (GPIO.input(pino_led) == 0):
            bot.sendMessage(chat_id, "O led já está desligado")
            GPIO.output(pino_buzzer, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(pino_buzzer, GPIO.LOW)
        else:
            GPIO.output(pino_led,GPIO.LOW)
            bot.sendMessage(chat_id, "O led foi desligado")
    elif command == "alarme":
        bot.sendMessage(chat_id, "\xF0\x9F\x9A\xA8 O alarme foi acionado")
        for i in range(10):
            GPIO.output(pino_led, GPIO.HIGH)
            GPIO.output(pino_buzzer, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(pino_led, GPIO.LOW)
            GPIO.output(pino_buzzer, GPIO.LOW)
            time.sleep(0.3)
    elif command == "temperatura":
        umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
       # Caso leitura esteja ok, mostra os valores na tela
        if umid is not None and temp is not None:
            mensagem = "Temperatura = {0:0.1f}  Umidade = {1:0.1f}n".format(temp, umid)
        else:
            # Mensagem de erro de comunicacao com o sensor
            mensagem ="Falha ao ler dados do DHT11."
        bot.sendMessage(chat_id, mensagem)

bot = telepot.Bot("463886559:AAEC84FJHOWCrJ0RfdERfLJf_f8G67dIMLA") 
bot.message_loop(handle)
print("Aguardando comando")

while 1:
     time.sleep(10)
