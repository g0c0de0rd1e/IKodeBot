import asyncio
import logging
import os
from dotenv import load_dotenv
from functools import lru_cache

from aiogram import Bot, Dispatcher, types, F, Router

import buttons
import text

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

@dp.message()
async def start_message(message: types.Message):
    await message.answer(text.greet.format(name=message.from_user.full_name),
                         reply_markup=buttons.menu)

@dp.callback_query(F.data == 'back_to_menu')
async def menu(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)

    await bot.send_message(callback_query.from_user.id,
                           text.greet.format(name=callback_query.from_user.full_name),
                           reply_markup=buttons.menu)
    
@dp.callback_query(F.data == 'info')
async def info(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.info.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'faq')
async def faq(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.faq.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'administration')
async def administration(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.administration.format(),
                           reply_markup=buttons.administration)
    
@dp.callback_query(F.data == 'anna')
async def anna(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.anna.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'irina')
async def irina(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.irina.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'teachers')
async def teachers(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.teachers.format(),
                           reply_markup=buttons.teachers)
    
@dp.callback_query(F.data == 'valera')
async def valera(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.valera.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'timur')
async def timur(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.timur.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'liza')
async def liza(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.liza.format(),
                           reply_markup=buttons.back_to_menu)
     
@dp.callback_query(F.data == 'aziz')
async def aziz(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.aziz.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'sergey')
async def sergey(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.sergey.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'modules')
async def modules(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.modules.format(),
                           reply_markup=buttons.modules)
    
@dp.callback_query(F.data == 'middle')
async def middle(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.middle.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'senior')
async def senior(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.senior.format(),
                           reply_markup=buttons.back_to_menu)
    
@dp.callback_query(F.data == 'suvorova')
async def suvorova(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.suvorova.format(),
                           reply_markup=buttons.suvorova)
    
@dp.callback_query(F.data == 'schedule')
async def schedule(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.schedule.format(),
                           reply_markup=buttons.schedule)
    
@dp.callback_query(F.data == 'antichniy')
async def antichniy(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.antichniy.format(),
                           reply_markup=buttons.antichniy)
    
@dp.callback_query(F.data == 'ostryaki')
async def ostryaki(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.ostryaki.format(),
                           reply_markup=buttons.ostryaki)
    
@dp.callback_query(F.data == 'suvsubota')
async def suvsubota(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.suvsubota.format(),
                           reply_markup=buttons.suvsubota)
    
@dp.callback_query(F.data == 'suvvskr')
async def suvvskr(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.suvvskr.format(),
                           reply_markup=buttons.suvvskr)

@dp.callback_query(F.data == 'antsubota')
async def antsubota(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.antsubota.format(),
                           reply_markup=buttons.antsubota)
    
@dp.callback_query(F.data == 'antvskr')
async def antvskr(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.antvskr.format(),
                           reply_markup=buttons.antvskr)
    
@dp.callback_query(F.data == 'ostsubota')
async def ostsubota(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.ostsubota.format(),
                           reply_markup=buttons.ostsubota)
    
@dp.callback_query(F.data == 'ostvskr')
async def ostvskr(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id,
                             callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text.ostvskr.format(),
                           reply_markup=buttons.ostvskr)

if __name__ == '__main__':
    asyncio.run(main())