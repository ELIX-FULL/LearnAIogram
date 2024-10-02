from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def create_menu():
    btn = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🎲'), KeyboardButton(text='🎲'), KeyboardButton(text='🎲')],
        [KeyboardButton(text='🎲'), KeyboardButton(text='🎲')],
        [KeyboardButton(text='🎲')]], resize_keyboard=True, input_field_placeholder='Выберите кнопки ниже')
    return btn


def create_inline_menu():
    inline_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
        [InlineKeyboardButton(text='Бот', callback_data='bot'), InlineKeyboardButton(text='Что то', callback_data='what')],
        [InlineKeyboardButton(text='Топ', callback_data='top')]], row_width=2, resize_keyboard=True)
    return inline_btn

alph = ['A', 'B', 'C', 'D', 'E']
def btn():
    btn = ReplyKeyboardBuilder()
    for alp in alph:
        btn.add(KeyboardButton(text=alp))
    return btn.adjust(3).as_markup()

def btn_inline():
    btn = InlineKeyboardBuilder()
    for alp in alph:
        btn.add(InlineKeyboardButton(text=alp, callback_data=f'alph_{alp}'))
    return btn.adjust(3).as_markup()