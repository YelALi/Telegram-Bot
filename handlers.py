from aiogram import F,Router
from aiogram.types import Message,CallbackQuery,FSInputFile
from aiogram.filters import CommandStart,Command

import app.keyboards as kb
import app.database.request as rq
router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Сәлем!',reply_markup=kb.main)
    await message.reply('Қандай көмегім керек?')

@router.message(Command('Не үшін құрылған'))
async def cmd_bb(message:Message):
    await message.answer('Бұл әзірге нақты құрылғы емес! требует проведения дальнейших исследований ')



@router.message(F.text=='Қазақстан өңірлерін тандаңыз')
async def kala(message:Message):
    await message.answer('Өңірді тандаңыз!',reply_markup=kb.kala)

@router.callback_query(F.data=="Batys")
async def batys(callback:CallbackQuery):
    await callback.answer('Батыс Қазақстандағы қалаларды тандадыңыз!')
    await callback.message.answer('Батыс Қазақстандағы қалаларды тандадыңыз!')

@router.callback_query(F.data=="Shy")
async def shy(callback:CallbackQuery):
    await callback.answer('Шығыс Қазақстандағы қалаларды тандадыңыз!')
    await callback.message.answer('Шығыс Қазақстандағы қалаларды тандадыңыз!')

@router.callback_query(F.data=="Ort")
async def ort(callback:CallbackQuery):
    await callback.answer('Орталық Қазақстандағы қалаларды тандадыңыз!')
    await callback.message.answer('Орталық Қазақстандағы қалаларды тандадыңыз!')

@router.callback_query(F.data=="Solt")
async def solt(callback:CallbackQuery):
    await callback.answer('Солтүстік Қазақстандағы қалаларды тандадыңыз!')
    await callback.message.answer('Солтүстік Қазақстандағы қалаларды тандадыңыз!')

@router.callback_query(F.data=="Ont")
async def ont(callback:CallbackQuery):
    await callback.answer('Онтүстік Қазақстандағы қалаларды тандадыңыз!')
    await callback.message.answer('Онтүстік Қазақстандағы қалаларды тандадыңыз!')




@router.message(F.text == 'Қазақстан жайлы')
async def about_ubt(message: Message):
    await message.answer('Қазақстан Республикасы – мемлекет аумағының ауданы бойынша дүниежүзінде тоғызыншы орынғаие.Әкімшілік-аумақтық құрылымы бойынша мемлекет 17 облысқа және 3 республикалық маңызы бар қалаларға бөлінеді: Астана, Алматы және Шымкент.Мемлекет басшысы Президент – Қасым-Жомарт Кемелұлы Тоқаев. Үкімет Қазақстан Республикасының атқарушылық билігін жүзеге асырады, атқарушы органдаржүйесін басқарады және олардың қызметіне жетекшілік жасайды')
    await message.answer_photo('https://th.bing.com/th/id/R.02ad80ab542abed46dafea40df5c5fee?rik=J4LFOJ6WA7eUzg&pid=ImgRaw&r=0')


@router.message(F.text== 'БОТ жайлы')
async def about_reg(message:Message):
    await message.answer('Бұл Telegram ботты қалалар туралы ақпарат беру үшін жасалған жоба болып табылады. Қала атын енгізгенде, бот сол қала туралы пайдалы мәліметтерді ұсынады. Бұл бот әзірше тек рубежный контрольға арналған, бірақ болашақта кеңейтіліп, көптеген қалалар мен ақпараттар қосылады. Ботты қолдану арқылы сіз қала туралы толық ақпарат ала аласыз.')
    await message.answer_photo('https://avatars.githubusercontent.com/u/207612082?s=400&u=06159f0b4162489a04d41e15e6cef8304b410965&v=4')


