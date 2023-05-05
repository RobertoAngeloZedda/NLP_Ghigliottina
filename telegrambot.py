from telegram.ext import *
from ipynb.fs.full.Algorithm import ghigliottina, inverted_dictionary
import re

API_KEY = '6132340853:AAFJ83pZj1COOfNLFdezRndawTzCEHIc_b4'

def start(update, context):
    update.message.reply_text('Inserisci 5 indizi separati da spazi o virgole')

def handle_message(update, context):
    words = process_input(update.message.text)
    n = len(words)
    if n == 5:
        update.message.reply_text(f'Indizi:\n{words[0]}\n{words[1]}\n{words[2]}\n{words[3]}\n{words[4]}\n\nCi penso un minuto...')
        solution_str = 'La soluzione potrebbe essere una di queste parole:\n'
        for solution, value in ghigliottina(words):
            solution_str += '\n' + inverted_dictionary[solution]
        update.message.reply_text(solution_str)
    else:
        if (n == 1):
            update.message.reply_text(f'ERRORE: Hai inserito {n} parola')
        else:
            update.message.reply_text(f'ERRORE: Hai inserito {n} parole')
    start(update, context)

def error(update, context):
    print(f'update: {update}\ncaused error: {context.error}\n')

def process_input(string):
    words = [word.strip(', ') for word in re.split(r'[,\s]+', string) if word.strip(', ')]
    
    return words

print("Bot in esecuzione...")

updater = Updater(API_KEY, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, handle_message))
dp.add_error_handler(error)

updater.start_polling()
updater.idle()