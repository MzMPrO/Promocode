from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.button.reply import menu_rkm_button, back_btn
from bot.db.main import get_balance, check_promocode, activated_promocode
from bot.dispacher import dp


@dp.message_handler()
async def menu_handler(msg: types.Message, state: FSMContext):
    await state.set_state('menu-state')
    await msg.answer(f"Siz menu bolimida siz.", reply_markup=menu_rkm_button())


@dp.message_handler(state='menu-state')
async def buttons_handler(msg: types.Message, state: FSMContext):
    if msg.text == "Promocode kiritish":
        # print(msg.text)
        await state.set_state("promocode-state")
        await msg.answer("Promocode raqamini kiriting", reply_markup=back_btn())
        if msg.text == 'Back':
            await menu_handler(msg, state)
    if msg.text == 'Balansingizni korish':
        await state.finish()
        await msg.answer(f'Sizning balansingiz {get_balance(str(msg.from_user.id))}',
                         reply_markup=back_btn())
        if msg.text == 'Back':
            await menu_handler(msg, state)


@dp.message_handler(state="promocode-state")
async def promocode_handler(msg: types.Message, state: FSMContext):
    promocode = msg.text
    if not check_promocode(promocode):
        if msg.text == 'Back':
            await menu_handler(msg, state)
        else:
            await msg.answer('Bu promocode oldin activ bogan.')
    else:
        activated_promocode(promocode, msg.from_user.id)
        await msg.answer('Siz bu promocodni activ qildingiz.')
        if msg.text == 'Back':
            await menu_handler(msg, state)
    await state.finish()
