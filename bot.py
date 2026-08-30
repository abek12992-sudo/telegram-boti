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
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 **Assalomu alaykum! Mobile Protsessorlar Botiga xush kelibsiz!**\n\n"
        "Ushbu bot orqali siz zamonaviy smartfonlarning protsessorlari (chipset) "
        "va ularning imkoniyatlari haqida batafsil ma'lumot olishingiz mumkin.\n\n"
        "📌 **Mavjud buyruqlar:**\n"
        "▫️ /snapdragon — Qualcomm Snapdragon chiplari\n"
        "▫️ /mediatek — MediaTek Dimensity seriyasi\n"
        "▫️ /exynos — Samsung Exynos protsessorlari\n"
        "▫️ /taqqosla — Protsessorlarni o'zaro taqqoslash\n"
        "▫️ /texnologiya — Ishlab chiqarish texnologiyalari (nm)"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def snapdragon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🚀 **Qualcomm Snapdragon**\n\n"
        "Snapdragon — Amerika Qo'shma Shtatlarining Qualcomm kompaniyasi tomonidan ishlab chiqariluvchi dunyodagi eng mashhur chipsetlar brendi.\n\n"
        "✨ **Asosiy ustunliklari:**\n"
        "• **Adreno grafikasi:** Mobil o'yinlarda (MLBB, PUBG, Genshin) eng yuqori FPS va barqarorlikni beradi.\n"
        "• **Dasturiy moslashuvchanlik:** O'yin va ilova yaratuvchilar birinchi navbatda Snapdragon chiplariga optimizatsiya qilishadi.\n"
        "• **Modem va aloqa:** 5G va Wi-Fi tezligi bo'yicha dunyoda yetakchi.\n\n"
        "💡 *Flagman chiplari:* Snapdragon 8 Gen 2, 8 Gen 3, 8 Elite."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def mediatek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💎 **MediaTek Dimensity**\n\n"
        "MediaTek — Tayvan kompaniyasi bo'lib, so'nggi yillarda o'zining **Dimensity** seriyasi bilan Snapdragon'ga kuchli raqobat tug'dira olgan brend.\n\n"
        "✨ **Asosiy ustunliklari:**\n"
        "• **Narx va unumdorlik:** Hamyonbop va o'rta narxdagi smartfonlar uchun eng zo'r tanlov.\n"
        "• **Energiya tejamkorligi:** Bateriya quvvatini kam sarflaydi va qizish darajasi sezilarli darajada pasaytirilgan.\n"
        "• **Mali va Immortalis grafikasi:** O'yinlarda doimiy va silliq ishlashni ta'minlaydi.\n\n"
        "💡 *Flagman chiplari:* Dimensity 9200, 9300, 9400."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def exynos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📱 **Samsung Exynos**\n\n"
        "Exynos — Janubiy Koreyaning Samsung kompaniyasi tomonidan o'z smartfonlari va boshqa qurilmalari uchun maxsus ishlab chiqariladigan protsessorlar liniyasi.\n\n"
        "✨ **Asosiy xususiyatlari:**\n"
        "• **Xclipse grafikasi:** So'nggi modellerda AMD (RDNA) grafik arxitekturasidan foydalanilmoqda.\n"
        "• **Multimediya va Displey:** Ekran ranglarini uzatish va kameralar bilan ishlash (ISP) imkoniyati juda yuqori.\n"
        "• **Optimizatsiya:** Samsung qurilmalari va One UI qobig'i bilan chuqur integratsiya qilingan.\n\n"
        "💡 *Flagman chiplari:* Exynos 2200, Exynos 2400."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def taqqosla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "⚖️ **Protsessorlar Taqqoslovi**\n\n"
        "🎮 **O'yinlar va Grafikada:**\n"
        "Snapdragon barqaror FPS va o'yinlardagi optimizatsiyasi bilan ustun turadi.\n\n"
        "🔋 **Energiya Tejamkorligi va Narxda:**\n"
        "MediaTek Dimensity kamroq energiya sarflaydi hamda arzonroq narxda yuqori kuch taklif etadi.\n\n"
        "📸 **Fotosurat va Kundalik Ishlashda:**\n"
        "Exynos kameradan olingan tasvirni qayta ishlash va tasvir sifatini oshirishda juda yaxshi natija ko'rsatadi."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def texnologiya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🔬 **Texnologik Jarayon (Nanometr - nm)**\n\n"
        "Protsessordagi nanometr (nm) ko'rsatkichi chip ichidagi tranzistorlarning hajmini bildiradi.\n\n"
        "⚙️ **Bu nimani beradi?**\n"
        "• Raqam qanchalik kichik bo'lsa (masalan, 3nm yoki 4nm), bir chipga shunchalik ko'p tranzistor sig'adi.\n"
        "• Kichik nanometr = **Yuqoriroq tezlik** + **Kamlangan qizish** + **Tejamkor batareya**.\n\n"
        "🏭 Bugungi kunda eng ilg'or chiplar **TSMC** va **Samsung** zavodlarida 3nm va 4nm texnologiyalari asosida ishlab chiqarilmoqda."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("snapdragon", snapdragon))
    app.add_handler(CommandHandler("mediatek", mediatek))
    app.add_handler(CommandHandler("exynos", exynos))
    app.add_handler(CommandHandler("taqqosla", taqqosla))
    
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
