
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import requests
import re

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Your bot token from BotFather
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Function to check if the message contains an Instagram link
def is_instagram_link(text):
    return "instagram.com" in text

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "✅ أرسل رابط منشور إنستقرام لتحميل الفيديو أو الصورة\n✅ Send an Instagram post link to download the video or image"
    await update.message.reply_text(message)

# Message handler for links
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    if not is_instagram_link(user_input):
        await update.message.reply_text("❌ الرابط غير صالح. الرجاء إرسال رابط من إنستقرام\n❌ Invalid link. Please send a valid Instagram post URL.")
        return

    # بدل من محاولة الاتصال بـ igram.io، نرد برسالة مؤقتة
try:
    await update.message.reply_text("✅ تم استلام الرابط بنجاح، لكن ميزة التحميل غير مفعّلة حالياً.")
except Exception as e:
    await update.message.reply_text(f"❌ حصل خطأ:\n{e}")

# Main function to start the bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
