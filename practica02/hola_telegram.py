#!/usr/bin/env python3
import telepot
import telepot.namedtuple
import time
from telepot.loop import MessageLoop

try:
    f=open('token.txt')
    TOKEN=f.read()
    TOKEN=TOKEN.strip()
    bot = telepot.Bot(TOKEN)
except e:
    print("error: "+e)


def handle(msg):
    chat_id = msg["chat"]["id"]
    texto = msg["text"]
    print("Entering message:")
    print("msg id: {0[message_id]}\nfrom:\n\tid: {1[from][id]}\n\tis bot: {2[from][is_bot]}\n\tfirst name: {3[from][first_name]}\n\tlanguage code: {4[from][language_code]}\nid: {5[chat][id]}\n\tfirst name: {6[chat][first_name]}\n\ttype: {7[chat][first_name]}"
    .format(msg,msg,msg,msg,msg,msg,msg,msg)) 
    respuesta = "Feliz navidad {0[from][first_name]}".format(msg)
    bot.sendMessage(chat_id, respuesta)
    return


def main():
    MessageLoop(bot, handle).run_as_thread()
    print("Listening...")

    while 1:
        time.sleep(10)
    return

if __name__ == "__main__":
    main()
