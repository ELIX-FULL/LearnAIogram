from aiogram import Router, F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import time

import buttons

user_router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()

@user_router.message(CommandStart())
async def start_command(message: Message):
    await message.reply("Привет я тестовый бот Elixa", reply_markup=buttons.btn())


@user_router.message(Command('help'))
async def help_command(message: Message):
    await message.reply("Помощь @ELIX_BOTS", parse_mode='HTML', reply_markup=buttons.create_inline_menu())


@user_router.message(F.dice.emoji == DiceEmoji.DICE)
async def dice_message(message: Message):
    value = message.dice.value
    time.sleep(3)
    await message.reply(f"Выпавшее число: {value}")

@user_router.message(F.dart.emoji == DiceEmoji.DART)
async def dice_message(message: Message):
    value = message.dice.value
    time.sleep(3)
    await message.reply(f"Выпавшее число: {value}")

@user_router.message(F.text == 'как дела')
async def how_are_you(message: Message):
    await message.reply('Привет, как дела?')

@user_router.message(F.photo)
async def photo_message(message: Message):
    await message.reply(f'Фотография отправлена! {message.photo[-1].file_id} {message.photo[-1].file_size}')

@user_router.callback_query(F.data == 'catalog')
async def catalog_message(query: CallbackQuery):
    await query.answer('Вы перешли в каталог')
    await query.message.edit_text('Каталог товаров', reply_markup=buttons.create_inline_menu())

@user_router.message(Command('reg'))
async def reg(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.reply('Введите ваше имя:')

@user_router.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.reply('Введите ваш номер телефона:')

@user_router.message(Reg.number)
async def reg_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.reply(f'Регистрация завершена!\n {data["name"]} {data["number"]}')
    await state.clear()
