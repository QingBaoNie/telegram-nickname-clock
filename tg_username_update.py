#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import sys
import logging
import asyncio
import re
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# === Telegram API 配置 ===
api_auth_file = 'api_auth'
if not os.path.exists(api_auth_file + '.session'):
    api_id = int(input('api_id: '))
    api_hash = input('api_hash: ')
else:
    api_id = 22928445
    api_hash = '8265f5dfaf0d71acefba05854c931938'

client1 = TelegramClient(api_auth_file, api_id, api_hash)

# === 日志配置 ===
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

original_first_name = None
original_last_name = None

# 匹配末尾的时间格式：2025-07-18 20:40
time_pattern = re.compile(r'\s*\d{4}-\d{2}-\d{2} \d{2}:\d{2}$')

async def change_name_auto():
    global original_first_name, original_last_name
    print('will change name')

    # 初始记录原始昵称
    me = await client1.get_me()
    original_first_name = me.first_name or ''
    original_last_name = me.last_name or ''

    while True:
        try:
            now = time.localtime()
            year = now.tm_year
            month = f"{now.tm_mon:02d}"
            day = f"{now.tm_mday:02d}"
            hour = f"{now.tm_hour:02d}"
            minute = f"{now.tm_min:02d}"
            second = f"{now.tm_sec:02d}"

            if second == '00' or second == '30':
                me = await client1.get_me()
                current_first_name = me.first_name or ''
                clean_name = re.sub(time_pattern, '', current_first_name).strip()

                new_first_name = f"{clean_name} {year}-{month}-{day} {hour}:{minute}"
                await client1(UpdateProfileRequest(first_name=new_first_name, last_name=""))
                logger.info(f'Updated -> {new_first_name}')

        except KeyboardInterrupt:
            print('\nResetting name...\n')
            await client1(UpdateProfileRequest(
                first_name=original_first_name,
                last_name=original_last_name
            ))
            sys.exit()

        except Exception as e:
            print(f'{type(e)}: {e}')

        await asyncio.sleep(1)

async def main(loop):
    await client1.start()
    print('creating task')
    task = loop.create_task(change_name_auto())
    await task
    task.cancel()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
