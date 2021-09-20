from telegram import ParseMode, Update, Bot
from telegram.ext import run_async

from Anim_Manager.modules.disable import DisableAbleCommandHandler
from Anim_Manager import dispatcher

from requests import get


@run_async
def github(bot: Bot, update: Update):
    message = update.effective_message
    text = message.text[len('/git '):]
    usr = get(f'https://api.github.com/users/{text}').json()
    if usr.get('login'):
        reply_text = f"""*Name:* `{usr['name']}`
*👨‍💼Username:* `{usr['login']}`
*🔖Account ID:* `{usr['id']}`
*📝Account type:* `{usr['type']}`
*📍Location:* `{usr['location']}`
*✍️Bio:* `{usr['bio']}`
*➡️Followers:* `{usr['followers']}`
*⬅️Following:* `{usr['following']}`
*🌚Hireable:* `{usr['hireable']}`
*⛵️Public Repos:* `{usr['public_repos']}`
*🚁Public Gists:* `{usr['public_gists']}`
*📨Email:* `{usr['email']}`
*🏢Company:* `{usr['company']}`
*🌍Website:* `{usr['blog']}`
*♻️Last updated:* `{usr['updated_at']}`
*📒Account created at:* `{usr['created_at']}`
"""
    else:
        reply_text = "User not found. Make sure you entered valid username!"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


__help__ = """
Imagine you find a person in Github.⚫️ But you don't know his info in Github.ℹ️ So you have to go to page by page and gather info about that account.😖 But no more!😃 With this feature you can get all the information about that person using his/her Github username.⭕️ A list got using this command is shown below.⬇️

 - /git:{GitHub username} Returns info about a GitHub user or organization.
"""

__mod_name__ = "Github💠"

github_handle = DisableAbleCommandHandler("git", github)

dispatcher.add_handler(github_handle)
