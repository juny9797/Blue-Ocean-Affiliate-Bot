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
# 📌 메시지 내용
# =============================
MESSAGE = """
💎<b>제휴 리스트</b>💎

▫️<a href="http://t.me/ocn2Marketing">구인/구직 채널보기</a>
▫️<a href="http://t.me/ocn9Marketing">문자발송 업체 채널보기</a>
▫️<a href="http://t.me/ocn11Marketing">토토/카지노/홀덤 채널보기</a>

▫️<a href="http://t.me/ocn10Marketing">각종DB 업자 채널보기</a>
▫️<a href="http://t.me/ocn1Marketing">DDOS/보안 관련 채널보기</a>
▫️<a href="http://t.me/ocn6Marketing">웹개발/솔루션/제작 채널보기</a>

▫️<a href="http://t.me/ocn12Marketing">디자인/이미지/영상 채널보기</a>

▫️<a href="http://t.me/ocn14Marketing">종합 마케팅/홍보관련 채널보기</a>
▫️<a href="http://t.me/ocn3Marketing">유입/퍼미션/콜센터 채널보기</a>
▫️<a href="http://t.me/ocn4Marketing">010인증/계정관련 채널보기</a>
▫️<a href="http://t.me/ocn5Marketing">유심/라우터/서버 채널보기</a>

▫️<a href="http://t.me/ocn8Marketing">세탁/가상/PG 채널보기</a>
▫️<a href="http://t.me/ocn7Marketing">코인대행/OTC 관련 채널보기</a>

▫️<a href="http://t.me/ocn19Marketing">은행업무/장관련 채널보기</a>
▫️<a href="http://t.me/ocn15Marketing">깡/소액/대리결제 채널보기</a>

▫️<a href="http://t.me/ocn27Marketing">유흥업소 수도권 채널보기</a>
▫️<a href="http://t.me/ocn13Marketing">명품/레플리카/주얼리 채널보기</a>
▫️<a href="http://t.me/ocn26Marketing">TV/영화/애니/중계 채널보기</a>

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
