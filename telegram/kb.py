from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

btn1 = InlineKeyboardButton(
    text="Войти как студент",
    callback_data="Logging"
)
btn2 = InlineKeyboardButton(
    text="Войти как преподователь",
    callback_data="Logging"
)
keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[btn1],
                     [btn2]]
)

btn3 = InlineKeyboardButton(
    text="Войти",
    callback_data="Logging"
)
btn4 = InlineKeyboardButton(
    text="Регистрация",
    callback_data="Register"
)
keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[[btn3],
                     [btn4]]
)