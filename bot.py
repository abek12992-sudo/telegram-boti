import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class Health(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

def run_port():
    server = HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 8080))), Health)
    server.serve_forever()

threading.Thread(target=run_port, daemon=True).start()

import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

SNAPDRAGON = """Snapdragon — bu asosan smartfonlar, planshetlar, aqlli soatlar va hattoki noutbuklar uchun mo‘ljallangan juda mashhur va kuchli mikroprotsessorlar (chip) oilasi. Oddiyroq aytganda, u smartfoningizning "miyasi" hisoblanadi. Snapdragon chiplari AQSHning Kaliforniya shtatida joylashgan, simsiz aloqa texnologiyalari bo‘yicha dunyodagi eng yirik gigantlardan biri bo‘lgan Qualcomm kompaniyasi tomonidan ishlab chiqiladi. Ilk bor namoyish etilishi: Qualcomm birinchi Snapdragon chipini (QSD8250 modeli) 2007-yil noyabr oyida taqdim etgan va 2009-yilda sotuvga chiqqan. Nomining ma’nosi: "Snapdragon" so‘zi inglizchadan tarjima qilinganda "ajdar og‘zi" degan ma'no bildiradi ദ്ദിᵔ.˛.ᵔ₎✧."""

MEDIATEK = """MediaTek Dimensity: Kompaniyaning eng zamonaviy, kuchli va 5G tarmog'ini qo'llab-quvvatlaydigan flagman chiplari seriyasi. Masalan, Dimensity 9300 va 9400 kabi modellar bugungi kunda tezlik va sun'iy intellekt (AI) imkoniyatlari bo'yicha Qualcomm Snapdragon va Apple chiplari bilan bemalol raqobatlasha oladi Hozirda global smartfon protsessorlari bozorida MediaTek eng katta ulushga ega (bozorning 30-35% qismini egallab, Qualcomm kompaniyasidan ham oldinda bormoqda"""

EXYNOS = """Exynos = 2000-yillar oʻrtalari: Samsung smartfonlar va media-pleyerlar uchun oddiy ARM bazasidagi chip-setlar ishlab chiqarar edi. Masalan, 2007-yilda chiqqan birinchi iPhone (2G) va iPhone 3GS prosessorlarini ham aynan Samsung tayyorlab bergan! 2010-yil (Asos solinishi): Samsung oʻzining birinchi Galaxy S (S1) flagman smartfonini chiqardi. Unda S5PC110 (kodli nomi "Hummingbird") chipi ishlatildi. 2011-yil (Rasmiy Exynos brendi): Samsung ushbu chip-setlar oilasiga rasman Exynos nomini berdi. Birinchi rasmiy brend ostidagi chip Exynos 4210 boʻlib, u afsonaviy Galaxy S2 smartfoniga oʻrnatildi."""

TAQQOSLA = """⚔️ Snapdragon vs MediaTek 1. 🎮 O'yin unumdorligi Snapdragon: Adreno grafik protsessori tufayli og'ir o'yinlarda (PUBG, Mobile Legends, Genshin Impact) va emulyatorlarda yuqori, barqaror FPS beradi. Dasturchilar o'yinlarni ko'pincha aynan Snapdragon uchun optimallashtirishadi. MediaTek: Dimensity seriyasi bilan kuchli sakrash qildi. Ko'p yadroli (Multi-core) ishlashda va narxiga nisbatan beradigan quvvatida juda yuqori natija ko'rsatadi. 2. 🔋 Energiya tejamkorligi va Qizib ketish Snapdragon: Yuqori yuklama ostida va uzoq vaqt foydalanganda haroratni yaxshi nazorat qiladi. MediaTek: Kunlik foydalanishda (ijtimoiy tarmoqlar, video ko'rish, tarmoq va 5G) batareya quvvatini juda tejamkor sarflaydi."""

TEXNOLOGIYA = """⚙️ 3nm dan 2nm Texnologiyaga O'tish 🤖 Smartfondagi AI (On-Device AI): Bulutli serverlarga ulanmasdan, to'g'ridan-to'g'ri telefonning o'zida ishlaydigan sun'iy intellekt (NPU) chiplari standartga aylanmoqda. ⚡ Matn va Tasvirni Lahzada Qayta Ishlash: Yangi avlod NPU birliklari matnlarni tarjima qilish, fotosuratlarni AI yordamida tahrirlash va ovozli yordamchilar javobini bir necha millisoniyada taqdim etmoqda. 🖥️ Server Chiplari Poygasi: Nvidia, AMD va Intel ma'lumotlar markazlari uchun AI GPU'larini yanada kuchaytirmoqda, bu esa smartfonlardagi AI imkoniyatlarini ham bilvosita rivojlantirmoqda. 🔬 GAA (Gate-All-Around) Arxitekturasi: TSMC va Samsung yangi 2nm chiplarida mutlaqo yangi GAA tranzistor texnologiyasiga o'tmoqda. Bu eski FinFET texnologiyasiga qaraganda tok sizib chiqishini keskin kamaytiradi va quvvatni tejaydi. 🚀 Tezlik va Energiya Tejamkorligi: 2nm chiplar 3nm ga nisbatan 10-15% yuqoriroq unumdorlik va 25-30% kamroq energiya sarfini ta'minlaydi. 🏁 Kim Birinchi? TSMC hamda Samsung 2nm chiplarini ommaviy ishlab chiqarishni yo'lga qo'ymoqda. Ular dastlab eng so'nggi flagman smartfonlar hamda AI serverlariga o'rnatiladi."""

async def send_text(update: Update, text: str):
    await update.message.reply_text(text)

async def snapdragon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_text(update, SNAPDRAGON)

async def mediatek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_text(update, MEDIATEK)

async def exynos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_text(update, EXYNOS)

async def taqqosla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_text(update, TAQQOSLA)

async def texnologiya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_text(update, TEXNOLOGIYA)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! 👋\n\nMavzularni ko‘rish uchun buyruqlardan foydalaning:\n"
        "/snapdragon\n/mediatek\n/exynos\n/taqqosla\n/texnologiya"
    )

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN environment variable topilmadi.")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("snapdragon", snapdragon))
    app.add_handler(CommandHandler("mediatek", mediatek))
    app.add_handler(CommandHandler("exynos", exynos))
    app.add_handler(CommandHandler("taqqosla", taqqosla))
    app.add_handler(CommandHandler("texnologiya", texnologiya))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
