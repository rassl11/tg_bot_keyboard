from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
from const import TOKEN
from func import *

u=Updater(token=TOKEN, workers=4)
d=u.dispatcher
d.add_handler(CommandHandler('start',callback=start, run_async=True))
d.add_handler(CallbackQueryHandler(pattern='gallery',callback=gallery))
d.add_handler(MessageHandler(Filters.text,callback=others_methods))
d.add_handler(CallbackQueryHandler(pattern='about_me',callback=about_me))
d.add_handler(CallbackQueryHandler(pattern='mark',callback=mark))



u.start_polling()