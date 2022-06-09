from operator import index
from random import randint
from smtplib import OLDSTYLE_AUTH
import sys
from time import sleep
from os import system
from eel import *
from flask import render_template
# ijaidj
def server_status(server):

    # Check if we can ping the server
    response = system("ping -c 1 " + server)
    
    if response == 0:
        return True
    else:
        return False

# 0
def rotateproxy_start(intervalo):

    print('green', '\n[+]Comenzando')

    while True:

        # Generate proxy
        seed = randint(0, 2238)

        f = open("proxyList.txt", "r")
        proxy = f.readlines()[seed]
        f.close

        proxyWithoutPort = proxy.split(':')

        # Check if generated proxy is working and execute it
        if server_status(proxyWithoutPort[0]):

            system('pconf ' + proxy)
            print('[+]' + proxy + 'es nuestro proxy ahora mismo!')

            # Countdown
            for x in range(0,intervalo):
                minutosRestantes = intervalo - x
                sleep(60)
                return '[i]Quedan ' + str(minutosRestantes) + ' minutos para el siguiente salto...', 
                
        else:
            # try with another proxy
            print('[-]El proxy no responde, probando con otro.')
            sleep(2)

# 1
def rotateproxy_manual():
    seed = randint(0, 2238)
    f = open("proxyList.txt", "r")
    proxy = f.readlines()[seed]
    f.close
    proxyWithoutPort = proxy.split(':')

    if server_status(proxyWithoutPort[0]):
            system('pconf ' + proxy)
            print('green', '[+]' + proxy + 'es nuestro proxy ahora mismo!')
            print('yellow','[i]Enter para saltar al siguiente nodo...')
            input()
            return rotateproxy_manual()
    else:
            # try with another proxy
            print('red', 'El proxy no responde, probando con otro.')
            sleep(2)
            return rotateproxy_manual()

# 2
def proxy_none():
    system('pconf none')
    return '[-]Current proxy has been removed'

# 3
def proxy_set(proxy):
    system('pconf' + proxy)

def showCommandList():
    # help command content
    print('Lista comandos:')
    print('     help | ver lista de comandos.')
    print('     proxy.start [intervalo entre saltos(minutos)] | comienza a saltar por los servidores disponibles.')
    print('     proxy.start.manual | genera proxys aleatorios pero salta manualmente.')
    print('     proxy.none | quita el proxy establecido detiene la cola de saltos.')
    print('     proxy.set [proxyserverip:port] | establece manualmente el servidor proxy que deseas.')
    print('')

def main(function):
    if function == 0:
        sleep(0)
    elif function == 1:
        sleep(0)
    elif function == 2:
        output_log = proxy_none()
        return render_template('index.html', output_log = output_log)
    elif function == 3:
        sleep(0)
