
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
BOT_TOKEN = "7203062916:AAFHvG7Vnxr8cbCwaShZsC-Sb8XVZmZvvX4"

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

    # Use igram.io or another public API (this is a placeholder simulation)
    try:
        api_url = f"https://igram.io/i/{user_input}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(api_url, headers=headers)

        if response.ok:
            # Simulate a successful return (actual implementation would parse HTML/JSON)
            await update.message.reply_text("✅ تم استلام الرابط وجاري التحميل...\n✅ Link received. Downloading...")
            # You can expand this part with real scraping logic or API calls
        else:
            await update.message.reply_text("❌ حدث خطأ أثناء الاتصال بالموقع\n❌ Error connecting to the download service.")

    except Exception as e:
        await update.message.reply_text(f"❌ حصل خطأ: {e}")

# Main function to start the bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
