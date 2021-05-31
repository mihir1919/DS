import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
print(logger.setLevel(logging.INFO))

from telegram.ext import Updater#this is used to start updater which has a job of a polling server
from telegram.ext import CommandHandler,MessageHandler,Filters#this is picked up from github doc diff from cb
TOKEN="1689415388:AAGbsnbRpz1xXwsTt8e6CVOakxi0n-w3nIY"

def main():
    updater=Updater(TOKEN)#try to recieve updates from telegram server
    
    dp = updater.dispatcher#handling updates
    
    start_handler = CommandHandler('start', start)
    how_handler = CommandHandler('how',how)
    echo_handler =  MessageHandler(Filters.text & (~Filters.command), echo)
    emo_handler = MessageHandler(Filters.sticker, emo)
    dp.add_handler(start_handler)
    dp.add_handler(how_handler)
    dp.add_handler(echo_handler)
    dp.add_handler(emo_handler)
#     dp.error_handler(error)
    updater.start_polling()
#     updater.stop()
    updater.idle()
    
def how(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm fine thank you!")
    
def start(update, context):
#     print(update)
#     print(context)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi {} I'm a bot, please talk to me!".format(update.message.from_user.first_name+" "+update.message.from_user.last_name))
    
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def emo(update,context):
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=update.message.sticker.file_id)

def error(bot, update, error):
    if not (error.message == "Message is not modified"):
        logger.warning('Update "%s" caused error "%s"' % (update, error))
    
if __name__=="__main__":
    main()