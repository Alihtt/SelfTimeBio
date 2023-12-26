import asyncio
import datetime
from pyrogram import Client
from config import api_id, api_hash, phone_number, time_zone
from pyrogram.errors.exceptions import FloodWait
import logging
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = Client(name="my_account",
             api_id=api_id,
             api_hash=api_hash,
             phone_number=phone_number)


async def main():
    n = datetime.datetime.now(pytz.timezone(time_zone))
    now_str = "⏱ Now: " + n.strftime('%H:%M') + " ⏱"
    logging.info(f'Time is {now_str}')
    try:
        logging.info(f'Trying to update Profile')
        await app.update_profile(bio=now_str)
        logging.info(f'Profile updated to: {now_str}')
    except FloodWait as e:
        logging.warning(f'Flood waited for {e.value}', exc_info=True)
        await asyncio.sleep(e.value + 1)


if __name__ == '__main__':
    scheduler = AsyncIOScheduler(timezone=pytz.timezone(time_zone))
    scheduler.add_job(main, 'cron', minute='*')
    logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    logging.info('Bot started...')
    print('Bot started...')
    scheduler.start()
    app.run()
