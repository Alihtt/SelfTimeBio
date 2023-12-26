import asyncio
import datetime
from pyrogram import Client
from config import api_id, api_hash, phone_number, time_zone
from pyrogram.errors.exceptions import FloodWait
import logging
import pytz


async def main():
    async with Client(name="my_account",
                      api_id=api_id,
                      api_hash=api_hash,
                      phone_number=phone_number) as app:

        while True:
            n = datetime.datetime.now(pytz.timezone(time_zone))
            if n.second == 0:
                now_str = "⏱ Now: " + datetime.datetime.now().strftime('%H:%M') + " ⏱"
                logging.info(f'Time is {now_str}')
                try:
                    logging.info(f'Trying to update Profile')
                    await app.update_profile(bio=now_str)
                    logging.info(f'Profile updated to : {now_str}')
                except FloodWait as e:
                    logging.warning(f'Flood waited for {e.value}', exc_info=True)
                    await asyncio.sleep(e.value + 1)
            await asyncio.sleep(1)


if __name__ == '__main__':
    logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    logging.info('Bot started...')
    print('Bot started...')
    asyncio.run(main())
