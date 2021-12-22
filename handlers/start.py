from config import *



@bot.message_handler(commands=['start'])
def startbot(msg):
    # import pdb; pdb.set_trace()
    user.id = msg.from_user.id
    "Ignites the bot application to take action"

    bot.reply_to(
        msg,
        "Welcome to Your Group Admin Bot"
    )

    

@bot.message_handler(regexp="^Back")
def startbotn(msg):
    startbot(msg)


