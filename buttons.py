from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
    [InlineKeyboardButton(text='Информация 📚', callback_data='info'),
     InlineKeyboardButton(text='FAQ ❓', callback_data='faq'),
     InlineKeyboardButton(text='Модули 📖', callback_data='modules')],
    [InlineKeyboardButton(text='Администрация', callback_data='administration'),
    InlineKeyboardButton(text='Преподаватели 👩‍🏫👨‍🏫', callback_data='teachers'),
     InlineKeyboardButton(text='Расписание 🗓️', callback_data='schedule')]
]

back_to_menu = [
    [InlineKeyboardButton(text='Меню 🏠', callback_data='back_to_menu')]
]

administration = [
    [InlineKeyboardButton(text='Ирина Тимуразовна', callback_data='irina'),
    InlineKeyboardButton(text='Анна ', callback_data='anna')]
]

teachers = [
    [InlineKeyboardButton(text='Валерий Витальевич', callback_data='valera'),
    InlineKeyboardButton(text='Тимур Русланович', callback_data='timur')],
    [InlineKeyboardButton(text='Елизавета Владимировна', callback_data='liza'),
    InlineKeyboardButton(text='Азиз Казимович', callback_data='aziz')],
    [InlineKeyboardButton(text='Сергей Владимирович', callback_data='sergey')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

modules = [
    [InlineKeyboardButton(text='Младшая группа', callback_data='junior')],
    [InlineKeyboardButton(text='Средняя группа', callback_data='middle')],
    [InlineKeyboardButton(text='Старшая группа', callback_data='senior')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

schedule = [
    [InlineKeyboardButton(text='Суворова', callback_data='suvorova')],
    [InlineKeyboardButton(text='Античный', callback_data='antichniy')],
    [InlineKeyboardButton(text='Генерала Острякова', callback_data='ostryaki')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

suvorova = [
    [InlineKeyboardButton(text='Суббота', callback_data='suvsubota')],
    [InlineKeyboardButton(text='Воскресенье', callback_data='suvvskr')],
    [InlineKeyboardButton(text='Назад', callback_data='schedule')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

antichniy = [
    [InlineKeyboardButton(text='Суббота', callback_data='antsubota')],
    [InlineKeyboardButton(text='Воскресенье', callback_data='antvskr')],
    [InlineKeyboardButton(text='Назад', callback_data='schedule')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

ostryaki = [
    [InlineKeyboardButton(text='Суббота', callback_data='ostsubota')],
    [InlineKeyboardButton(text='Воскресенье', callback_data='ostvskr')],
    [InlineKeyboardButton(text='Назад', callback_data='schedule')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

suvsubota = [
    [InlineKeyboardButton(text='Младшие')],
    [InlineKeyboardButton(text='Средние')],
    [InlineKeyboardButton(text='Старшие')],
    [InlineKeyboardButton(text='Назад', callback_data='suvorova')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

suvvskr = [
    [InlineKeyboardButton(text='Младшие')],
    [InlineKeyboardButton(text='Средние')],
    [InlineKeyboardButton(text='Старшие')],
    [InlineKeyboardButton(text='Назад', callback_data='suvorova')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

antsubota = [
    [InlineKeyboardButton(text='Младшие')],
    [InlineKeyboardButton(text='Средние')],
    [InlineKeyboardButton(text='Старшие')],
    [InlineKeyboardButton(text='Назад', callback_data='antichniy')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

antvskr = [
    [InlineKeyboardButton(text='Младшие')],
    [InlineKeyboardButton(text='Средние')],
    [InlineKeyboardButton(text='Старшие')],
    [InlineKeyboardButton(text='Назад', callback_data='antichniy')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

ostsubota = [
    [InlineKeyboardButton(text='Младшие')],
    [InlineKeyboardButton(text='Средние')],
    [InlineKeyboardButton(text='Старшие')],
    [InlineKeyboardButton(text='Назад', callback_data='ostryaki')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

ostvskr = [
    [InlineKeyboardButton(text='Младшие')],
    [InlineKeyboardButton(text='Средние')],
    [InlineKeyboardButton(text='Старшие')],
    [InlineKeyboardButton(text='Назад', callback_data='ostryaki')],
    [InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
back_to_menu = InlineKeyboardMarkup(inline_keyboard=back_to_menu)
administration = InlineKeyboardMarkup(inline_keyboard=administration)
teachers = InlineKeyboardMarkup(inline_keyboard=teachers)
modules = InlineKeyboardMarkup(inline_keyboard=modules)
schedule = InlineKeyboardMarkup(inline_keyboard=schedule)
suvorova = InlineKeyboardMarkup(inline_keyboard=suvorova)
antichniy = InlineKeyboardMarkup(inline_keyboard=antichniy)
ostryaki = InlineKeyboardMarkup(inline_keyboard=ostryaki)
suvsubota = InlineKeyboardMarkup(inline_keyboard=suvsubota)
suvvskr = InlineKeyboardMarkup(inline_keyboard=suvvskr)
antsubota = InlineKeyboardMarkup(inline_keyboard=antsubota) 
antvskr = InlineKeyboardMarkup(inline_keyboard=antvskr)
ostsubota = InlineKeyboardMarkup(inline_keyboard=ostsubota)
ostvskr =InlineKeyboardMarkup(inline_keyboard=ostvskr)