from telegram import ParseMode, Update, Bot, Chat
from telegram.ext import CommandHandler, MessageHandler, BaseFilter, run_async

from Anim_Manager import dispatcher

from requests import get

import json
from urllib.request import urlopen




@run_async
def covid(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/covid '):]
    fetch = get(f'https://coronavirus-tracker-api.herokuapp.com/all')

    if fetch.status_code == 200:
        usr = fetch.json()
        data = fetch.text
        parsed = json.loads(data)
        total_confirmed_global = parsed["latest"]["confirmed"]
        total_deaths_global = parsed["latest"]["deaths"]
        total_recovered_global = parsed["latest"]["recovered"]
        active_cases_covid19 = total_confirmed_global - total_deaths_global - total_recovered_global
        reply_text = ("*🦠 Corona Virus Results 🦠:*\n"
        "🌡 Confirmed : `" + str(total_confirmed_global) + "`\n"
        "⚰️ Deaths    : `" + str(total_deaths_global) + "`\n"
        "♻️ Recovered : `" + str(total_recovered_global) +"`\n"
        "🩸 Active    : `"+ str(active_cases_covid19) + "`")
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

        return

    elif fetch.status_code == 404:
        reply_text = "The API is currently down."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


__help__ = """
 If you want to get the Global Covid 19 status🌍, then this is a command for you.😘 You can type this command and get worldwide Covid 19 status and BOOM!💣
 
 - /covid get worldwide corona status
"""

__mod_name__ = 'Covid 19🦠'

COVID_HANDLER = CommandHandler("covid", covid, admin_ok=True)
dispatcher.add_handler(COVID_HANDLER)


