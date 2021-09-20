from typing import List
 
from telegram import Bot, Update
from telegram.ext import run_async, Filters
 
from Anim_Manager import dispatcher
from Anim_Manager.modules.disable import DisableAbleCommandHandler
 
normiefont = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
boxfont = ['𝓪','𝓫','𝓬','𝓭','𝓮','𝓯','𝓰','𝓱','𝓲','𝓳','𝓴','𝓵','𝓶','𝓷','𝓸','𝓹','𝓺','𝓻','𝓼','𝓽','𝓾','𝓿','𝔀','𝔁','𝔂','𝔃']
 
@run_async
def box(bot: Bot, update: Update, args: List[str]):
 
	string = '  '.join(args).lower()
	for normiecharacter in string:
		if normiecharacter in normiefont:
			boxcharacter = boxfont[normiefont.index(normiecharacter)]
			string = string.replace(normiecharacter, boxcharacter)
 
	message = update.effective_message
	if message.reply_to_message:
		message.reply_to_message.reply_text(string)
	else:
		message.reply_text(string)
 
 
__help__ = ""  # no help string
 
BOX_HANDLER = DisableAbleCommandHandler("mts", box, pass_args=True)
 
dispatcher.add_handler(MTS_HANDLER)
 
__mod_name__ = "MathBoldScript"
__command_list__ = ["mts"]
__handlers__ = [BOX_HANDLER]
