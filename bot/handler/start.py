from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.button.inline import region_choise_btn
from bot.button.reply import phone_btn
from bot.db.main import check_user, register_user
from bot.dispacher import dp


@dp.message_handler(commands='start', state='*')
async def main_handler(msg: types.Message, state: FSMContext):
    await msg.answer(f"Assalomu aleykum hurmatli {msg.from_user.first_name}")
    if not check_user(msg.from_user.id):
        await state.set_state("full_name")
        await msg.answer("Siz registrasiyadan otasiz\n<b>Toliq ismingizni kiriting:</b>", parse_mode='HTML')
    else:
        from bot.handler import menu_handler
        await menu_handler(msg, state)


@dp.message_handler(state="full_name")
async def lirst_name_check_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        storage["full_name"] = msg.text
    await state.set_state("phone_number")
    await msg.answer("<b>Telefon raqamingizni kiriting:\nFormati: +998*********</b>", parse_mode='HTML', reply_markup=phone_btn())


@dp.message_handler(state="phone_number", content_types=types.ContentType.ANY)
async def last_name_check_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        if msg.content_type == 'text':
            storage["phone_number"] = msg.text
        else:
            storage["phone_number"] = msg.contact.phone_number
    await state.set_state("region")
    await msg.answer("<b>Regionni kiriting</b>", parse_mode='HTML', reply_markup=region_choise_btn())


@dp.callback_query_handler(state="region")
async def phone_check_handler(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as storage:
        storage["region"] = call.data
    register_user(user_id=call.from_user.id, full_name=storage.get("full_name"),
                  phone_number=storage.get("phone_number"),
                  region=storage.get("region"))
    await call.message.answer("Siz muvaffaqiyat bilan registratsiyadan otdingiz!!!")
    from bot.handler import menu_handler
    await menu_handler(call.message, state)
