{\rtf1\ansi\ansicpg1251\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask\
from threading import Thread\
from telegram import Update\
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes\
import os\
\
app = Flask(__name__)\
\
@app.route('/')\
def home():\
    return "\uc0\u1041 \u1086 \u1090  \u1088 \u1072 \u1073 \u1086 \u1090 \u1072 \u1077 \u1090 !"\
\
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    await update.message.reply_text("\uc0\u1055 \u1088 \u1080 \u1074 \u1077 \u1090 ! \u1071  \u1075 \u1086 \u1090 \u1086 \u1074  \u1082  \u1088 \u1072 \u1073 \u1086 \u1090 \u1077 .")\
\
def run_telegram_bot():\
    token = os.getenv("BOT_TOKEN")\
    if not token:\
        print("\uc0\u10060  \u1053 \u1077  \u1079 \u1072 \u1076 \u1072 \u1085  BOT_TOKEN")\
        return\
\
    application = ApplicationBuilder().token(token).build()\
    application.add_handler(CommandHandler("start", start))\
    application.run_polling()\
\
if __name__ == '__main__':\
    Thread(target=run_telegram_bot).start()\
    app.run(host='0.0.0.0', port=10000)\
}