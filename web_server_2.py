#Codigo para pantalla OLED
#Importaciones para Wifi
try:
  import usocket as socket
except:
  import socket

from machine import Pin, I2C
import ssd1306
from time import sleep
import network

# ESP8266 Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'TIGO-8A6E'
password = '4D9687402209'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
imp = station.ifconfig()

def pantalla():
    oled.fill(0)
    oled.show()
    oled.text('Control de video:',0,0)
    oled.text('Direccion:',0,16)
    oled.text(imp[0],0,28)
    
    oled.text('Video:',0,45)
    oled.text(oled_video,50,45)
    oled.text('audio:',0,56)
    oled.text(oled_audio,50,56)
    oled.show()
    
    oled.show()

oled_video = 'OFF'
oled_audio = 'OFF'
pantalla()


led1 = Pin(16, Pin.OUT) #D0
led2 = Pin(0, Pin.OUT) #D3
led3 = Pin(14, Pin.OUT) #D5
led4 = Pin(12, Pin.OUT) #D6

led5 = Pin(3, Pin.OUT) #RX PIN
led6 = Pin(15, Pin.OUT) #D8
led7 = Pin(1, Pin.OUT) #TX PIN

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
led5.value(0)
led6.value(0)
led7.value(0)



def web_page():
  if led1.value() == 1:
    gpio_state="Video 1"    
  elif led2.value() == 1:
    gpio_state="Video 2"
  elif led3.value() == 1:
    gpio_state="Video 3"
  elif led4.value() == 1:
    gpio_state="Video 4"
  else:
    gpio_state="OFF"
  
  html = """<!DOCTYPE html><html> <head> <title>ESP Web Server</title> <meta name="viewport"
    content="width=device-width, initial-scale=1"> <link rel="icon" href="data:,">
    <style> html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0d1b2a; padding: 2vh; font-size: 2rem;} p{font-size: 1rem;} .button{display: inline-block;
    background-color: #415a77; border: none; border-radius: 4px; color: white; padding: 16px 40px;
    text-decoration: none; font-size: 15px; margin: 2px; cursor: pointer;} .button:hover { background-color: #778da9; }
    .button:active{ position: relative; background-color: #e0e1dd; color: #0d1b2a }
    .button2:hover{ position: relative; background-color: #bc4749; color: #e0e1dd }
    .button2:active{ position: relative; background-color: #540b0e; color: #e0e1dd }
    </style> </head> <body> <h1>Control de video</h1> <p>Estado de salida: <strong>""" + gpio_state + """
    </strong></p> <p><a href="/?state1=on"><button class="button">VIDEO 1</button></a></p>
    <p><a href="/?state2=on"><button class="button">VIDEO 2</button></a></p> <p><a href="/?state3=on">
    <button class="button">VIDEO 3</button></a></p> <p><a href="/?state4=on"><button class="button">VIDEO 4</button></a>
    </p> <p><a href="/?state5=on"><button class="button2 button">Desconectar</button></a></p>
    <h1 id="audio">Control de audio</h1> <p><a href="/?state6=on"><button class="button">AUDIO 1</button></a></p>
    <p><a href="/?state7=on"><button class="button">AUDIO 2</button></a></p>
    <p><a href="/?state8=on"><button class="button">AUDIO 3</button></a></p><p><a href="/?state10=on">
    <button class="button2 button">Desconectar</button></a></p> <br> <h5>Laboratorio Comunicaciones 3</h5> </body></html>"""
  return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(2)


    
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  video1 = request.find('/?state1=on')
  video2 = request.find('/?state2=on')
  video3 = request.find('/?state3=on')
  video4 = request.find('/?state4=on')
  video5 = request.find('/?state5=on')
  
  audio1 = request.find('/?state6=on')
  audio2 = request.find('/?state7=on')
  audio3 = request.find('/?state8=on')
  audio5 = request.find('/?state10=on')
  
  if video1 == 6:
    oled_video = '1'
    pantalla()
    print('VIDEO 1 ON')
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(0.6)
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(0)
  if video2 == 6:
    oled_video = '2'
    pantalla()
    print('VIDEO 2 ON')
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(0.6)
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(0)
  if video3 == 6:
    oled_video = '3'
    pantalla()
    print('VIDEO 3 ON')
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(0.6)
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(0)
  if video4 == 6:
    oled_video = '4'
    pantalla()
    print('VIDEO 4 ON')
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(0.6)
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(1)
  if video5 == 6:
    oled_video = 'OFF'
    pantalla()
    print('VIDEO 1 ON')
    print('ALL LED OFF')
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)

  if audio1 == 6:
    oled_audio = '1'
    pantalla()
    led5.value(0)
    led6.value(0)
    led7.value(0)
    sleep(0.6)
    led5.value(0)
    led6.value(1)
    led7.value(0)
    print('AUDIO 1 ON')
  if audio2 == 6:
    oled_audio = '2'
    pantalla()
    led5.value(0)
    led6.value(0)
    led7.value(0)
    sleep(0.6)
    led5.value(1)
    led6.value(0)
    led7.value(0)
    print('AUDIO 2 ON')
  if audio3 == 6:
    oled_audio = '3'
    pantalla()
    led5.value(0)
    led6.value(0)
    led7.value(0)
    sleep(0.6)
    led5.value(0)
    led6.value(0)
    led7.value(1)
    print('AUDIO 3 ON')
  if audio5 == 6:
    oled_audio = 'OFF'
    pantalla()
    led5.value(0)
    led6.value(0)
    led7.value(0)
    print('AUDIO OFF')

  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
