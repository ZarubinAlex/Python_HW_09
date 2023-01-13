from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import mytoken

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text#.split(" ")
    print(eval(msg[6:]))
    await update.message.reply_text(f'{msg[6:]} = {eval(msg[6:])}')

async def helpp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    '''
    Чтобы произвести вычисление, вводим:\n
    /calc пробел выражение\n
        Наример:
        /calc 5 + 8
    ''')


if __name__ == '__main__':
    app = ApplicationBuilder().token(mytoken.MYTOKEN).build()
    app.add_handler(CommandHandler("help", helpp))
    app.add_handler(CommandHandler("calc", calc))

    print('Server start')
    app.run_polling()

