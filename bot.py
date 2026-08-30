import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Ishlab chiqaruvchilar haqida ma'lumot olish uchun quyidagi buyruqlardan foydalaning:\n\n"
        "/snapdragon - Snapdragon ma'lumotlari\n"
        "/mediatek - MediaTek ma'lumotlari\n"
        "/exynos - Exynos ma'lumotlari\n"
        "/taqqosla - Taqqoslash\n"
        "/texnologiya - Texnologiyalar"
    )

async def snapdragon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Snapdragon — Qualcomm kompaniyasining kuchli va o'yinlar uchun moslashtirilgan protsessorlari.")

async def mediatek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("MediaTek — Dimensity seriyasi bilan mashhur va hamyonbop protsessorlar ishlab chiqaruvchi brend.")

async def exynos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Exynos — Samsung kompaniyasining o'z qurilmalari uchun mo'ljallangan chipsets seriyasi.")

async def taqqosla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Snapdragon o'yinlarda barqaror grafikaga ega, Dimensity esa energiyani tejamkorligi va narxi bilan ajralib turadi.")

async def texnologiya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Zamonaviy chiplar 4nm va 3nm texnolik jarayonlarda ishlab chiqarilmoqda.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("snapdragon", snapdragon))
    app.add_handler(CommandHandler("mediatek", mediatek))
    app.add_handler(CommandHandler("exynos", exynos))
    app.add_handler(CommandHandler("taqqosla", taqqosla))
    app.add_handler(CommandHandler("texnologiya", texnologiya))

    app.run_polling()

if __name__ == "__main__":
    main()
