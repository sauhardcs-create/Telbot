from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8739715978:AAHxSCLtTYR3l3E3JJgqCbf6E5K5nkdV8FU"

# Temporary memory storage
user_profiles = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    
    user_profiles[user_id]={
        "step":"style",
        "style":None
    }
    await update.message.reply_text(
        "Hi! 🎬\n"
        "Let me understand your personality.\n"
        "Do you prefer:\n"
        "1. Deep & Thoughtful\n"
        "2. Fun & Light"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    if user_id not in user_profiles:
        await update.message.reply_text("Please type /start first.")
        return

    step = user_profiles[user_id]["step"]
    # Personality choice
    if step == "style":
        if text == "1":
            user_profiles[user_id]["style"] = "deep"
            user_profiles[user_id]["step"] = "deep_type"
            await update.message.reply_text(
                "Nice. Do you like:\n"
                "1. Dark themes\n"
                "2. Inspirational stories"
            )

        elif text == "2":
            user_profiles[user_id]["style"] = "fun"
            user_profiles[user_id]["step"] = "fun_type"
            await update.message.reply_text(
                "Cool 😎 Do you prefer:\n"
                "1. Sitcoms\n"
                "2. Adventure"
            )

        else:
            await update.message.reply_text("Please choose 1 or 2.")

    # STEP 2A: Deep branch
    elif step == "deep_type":
        if text == "1":
            await update.message.reply_text(
                "You might love:\n"
                "🎬 Fight Club\n"
                "📺 True Detective\n"
                "📖 1984"
            )
            user_profiles[user_id]["step"] = "done"
        elif text == "2":
            await update.message.reply_text(
                "Try these:\n"
                "🎬 The Pursuit of Happiness\n"
                "📖 Atomic Habits\n"
                "📺 Ted Lasso"
            )
            user_profiles[user_id]["step"] = "done"
        else:
            await update.message.reply_text("Please choose 1 or 2.")
        

    # STEP 2B: Fun branch
    elif step == "fun_type":
        if text == "1":
            await update.message.reply_text(
                "You should watch:\n"
                "📺 Friends\n"
                "🎬 The Intern\n"
                "📖 The Hitchhiker's Guide to the Galaxy"
            )
            user_profiles[user_id]["step"] = "done"
        elif text == "2":
            await update.message.reply_text(
                "Adventure mode activated 🚀\n"
                "🎬 Interstellar\n"
                "📺 Stranger Things\n"
                "📖 The Hobbit"
            )
            user_profiles[user_id]["step"] = "done"
        else:
            await update.message.reply_text("Please choose 1 or 2.")
        
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()