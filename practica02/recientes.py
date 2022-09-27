
#!/usr/bin/env python3
import telepot
import telepot.namedtuple
import time
from telepot.loop import MessageLoop

import recorrerdirectorios

try:
	f=open('token_recientes.txt')
	TOKEN=f.read()
	TOKEN=TOKEN.strip()
	bot = telepot.Bot(TOKEN)
except e:
	print("error: "+e)


def handle(msg):
	chat_id = msg["chat"]["id"]
	text = msg["text"]
	try:
		ruta=text.split("::")[0]
		periodo=text.split("::")[1]
		respuesta=recorrerdirectorios.recorrer(ruta, int(periodo))
		
	except:
		bot.sendMessage(chat_id,"error:formato--> path::periodo")
		return
		
	if respuesta[1] != "ok":
		bot.sendMessage(chat_id, respuesta[1])
	
	else:
		r="\n".join(respuesta[0])

		if len(respuesta[0]) < 1024:
			bot.sendMessage(chat_id, r)
		else:
			bot.sendMessage(chat_id, "Respuesta demasiado larga. " + \
			"Está truncada:\n{}".format(r[0:1024]))

def main():
	MessageLoop(bot, handle).run_as_thread()


	print("Listening...")

	while 1:
		time.sleep(10)
	return

if __name__ == "__main__":
    main()
