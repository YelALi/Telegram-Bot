from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Қазақстан өңірлерін тандаңыз')],
                                     [KeyboardButton(text='Қазақстан жайлы')],
                                     [KeyboardButton(text='БОТ жайлы ')]],
                            resize_keyboard=True,
                            input_field_placeholder='Керегін тандаңыз!')
                            

kala = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton
(text='Батыс Қазақстан',callback_data='Batys')],
   
   
   [InlineKeyboardButton(text='Шығыс Қазақстан',callback_data='Shy')],
 
 
 [InlineKeyboardButton(text='Оңтүстік Қазақстан',callback_data='Ont')],
 [InlineKeyboardButton(text='Орталық Қазақстан',callback_data='Ort')],
 [InlineKeyboardButton(text='Солтүстік Қазақстан',callback_data='Solt')]])


