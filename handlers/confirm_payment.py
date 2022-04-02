from config import *
from utils import *



@bot.message_handler(commands=['confirmSub'])
def validatePayment(msg):
    "Get Validation On Payment"

    # Please provide a payment Id
    question = bot.send_message(
        msg.from_user.id,
        "To confirm your subscription, please provide your <b>Payment ID</b>",
        parse_mode="html"
    )
    bot.register_next_step_handler(question, check_payment_id)


def check_payment_id(msg):
    "validate payment Id"
    payment_id = msg.text
    
    status = payment_status(payment_id)

    if status == True:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        a = types.InlineKeyboardButton(text="Join VIP Divine Chat Group", callback_url="#")
        keyboard.add(a)

        bot.send_message(
            msg.from_user.id,
            "✅ You are a validate subscriber",
            reply_markup=keyboard
        )
    
    else:
        bot.send_message(
            msg.from_user.id,
            "You are not a subscribe. Please make sure you have paid for this month."
        )

