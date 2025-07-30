import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode
import os
from dotenv import load_dotenv

# ✅ .env 파일 로드
load_dotenv()

nest_asyncio.apply()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# =============================
# 📌 메시지 내용 (채널보기만 하이퍼링크)
# =============================
MESSAGE = """
💎<b>제휴 리스트</b>💎

▫️구인/구직 <a href="http://t.me/ocn2Marketing">채널보기</a>
▫️문자발송 업체 <a href="http://t.me/ocn9Marketing">채널보기</a>
▫️토토/카지노/홀덤 <a href="http://t.me/ocn11Marketing">채널보기</a>

▫️각종DB 업자 <a href="http://t.me/ocn10Marketing">채널보기</a>
▫️DDOS/보안 관련 <a href="http://t.me/ocn1Marketing">채널보기</a>
▫️웹개발/솔루션/제작 <a href="http://t.me/ocn6Marketing">채널보기</a>

▫️디자인/이미지/영상 <a href="http://t.me/ocn12Marketing">채널보기</a>

▫️종합 마케팅/홍보관련 <a href="http://t.me/ocn14Marketing">채널보기</a>
▫️유입/퍼미션/콜센터 <a href="http://t.me/ocn3Marketing">채널보기</a>
▫️010인증/계정관련 <a href="http://t.me/ocn4Marketing">채널보기</a>
▫️유심/라우터/서버 <a href="http://t.me/ocn5Marketing">채널보기</a>

▫️세탁/가상/PG <a href="http://t.me/ocn8Marketing">채널보기</a>
▫️코인대행/OTC 관련 <a href="http://t.me/ocn7Marketing">채널보기</a>

▫️은행업무/장관련 <a href="http://t.me/ocn19Marketing">채널보기</a>
▫️깡/소액/대리결제 <a href="http://t.me/ocn15Marketing">채널보기</a>

▫️유흥업소 수도권 <a href="http://t.me/ocn27Marketing">채널보기</a>
▫️명품/레플리카/주얼리 <a href="http://t.me/ocn13Marketing">채널보기</a>
▫️TV/영화/애니/중계 <a href="http://t.me/ocn26Marketing">채널보기</a>

📢 <b>공지 이벤트</b> : @KBOVVIP365

👑 <b>KBO 보증거래 안내</b> : @KBOEU2
👑 <b>KBO 보증거래 신청</b> : @KBOVVIP

👑 <b>건의 문의 제휴</b> : @KBOVVIP
"""

# ▶️ "제휴" 정확히 입력한 경우 발송
async def keyword_trigger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.strip() == "제휴":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=MESSAGE,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )

# 메인 실행
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), keyword_trigger))
    print("✅ 봇 실행됨 - '제휴' 키워드 감지 시 안내 메시지 발송")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
