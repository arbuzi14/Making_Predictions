from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import os
from dotenv import load_dotenv


zodiaks = {
        'овен': 'Сегодня день для решительных действий! Вас ждёт успех.',
        'телец': 'Проведите день спокойно, подумайте о будущем. Хороший день для планирования.',
        'близнецы': 'Будьте осторожны с новыми знакомыми, не все они искренни.',
        'рак': 'Сегодня удачный день для улучшения отношений с близкими.',
        'лев': 'Постарайтесь избежать конфликтов на работе, они могут затянуться.',
        'дева': 'Сегодня удачный день для финансовых вложений и покупок.',
        'весы': 'Возможно, вам придется принять важное решение, доверьтесь интуиции.',
        'скорпион': 'Не бойтесь рисковать сегодня, это принесет свои плоды.',
        'стрелец': 'Сегодня отличный день для путешествий и новых впечатлений.',
        'козерог': 'Уделите внимание здоровью, не перегружайте себя на работе.',
        'водолей': 'Вы найдете решение проблемы, которая давно вас беспокоит.',
        'рыбы': 'Сегодня вас ждет приятный сюрприз от близкого человека.'
        }



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я могу предсказать твою судьбу по знаку зодиака. Напиши свой знак!")
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Напиши свой знак зодиака, и я дам тебе предсказание!")
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)
    updater.start_polling()


def zodiac_prediction(update, context):
    user_text=update.message.text.lower()
    print(user_text)
    if user_text == "зодиаки":
        context.bot.send_message(chat_id=update.effective_chat.id, text=", ".join(zodiaks.keys()))
    elif user_text == "овен":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['овен']))
    elif user_text == "телец":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['телец']))
    elif user_text == "близнецы":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['близнецы']))
    elif user_text == "рак":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['рак']))
    elif user_text == "лев":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['лев']))
    elif user_text == "дева":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['дева']))
    elif user_text == "весы":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['весы']))
    elif user_text == "скорпион":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['скорпион']))
    elif user_text == "стрелец":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['стрелец']))
    elif user_text == "козерог":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['козерог']))
    elif user_text == "водолей":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['водолей']))
    elif user_text == "рыбы":
        context.bot.send_message(chat_id=update.effective_chat.id, text="".join(zodiaks['рыбы']))
    else:
        text = update.message.text
        context.bot.send_message(chat_id=update.effective_chat.id, text="Моя твоя не понимать напиши свой знак зодиака (пример:овен)")    
    zodiac_prediction_handler = MessageHandler(Filters.text & (~Filters.command), zodiac_prediction)
    dispatcher.add_handler(zodiac_prediction_handler)


def main():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)

    zodiac_prediction_handler = MessageHandler(Filters.text & (~Filters.command), zodiac_prediction)
    dispatcher.add_handler(zodiac_prediction_handler)

    updater.start_polling()
    updater.idle()



if __name__ == "__main__":
    main()
