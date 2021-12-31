import pageviewapi.period
import wikipedia

#!/usr/bin/env python
import pika
import sys

message = ' '.join(sys.argv[1:])
#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Creación de la cola
channel.queue_declare(queue='pagina')

#Publicación del mensaje
channel.basic_publish(exchange='',
                      routing_key='visitas',
                      body= str(pageviewapi.period.sum_last('en.wikipedia', str(message), last=30,access='all-access', agent='all-agents')) )
print(" Enviando visitas mensuales de la pagina")

wikipedia.set_lang("en")
resumen=wikipedia.summary(str(message), sentences=1)
channel.basic_publish(exchange='',
                      routing_key='resumen',
                      body= str(resumen) )
print(" Enviando resumen de la pagina")


connection.close()