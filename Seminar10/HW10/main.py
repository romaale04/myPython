from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from loguru import logger
from config import BOT_TOKEN

play_field = [
    [
        InlineKeyboardButton("1", callback_data="num:1"),
        InlineKeyboardButton("2", callback_data="num:2"),
        InlineKeyboardButton("3", callback_data="num:3"),
    ],
    [
        InlineKeyboardButton("4", callback_data="num:4"),
        InlineKeyboardButton("5", callback_data="num:5"),
        InlineKeyboardButton("6", callback_data="num:6"),
    ],
    [
        InlineKeyboardButton("7", callback_data="num:7"),
        InlineKeyboardButton("8", callback_data="num:8"),
        InlineKeyboardButton("9", callback_data="num:9"),
    ],
]

action_callback = CallbackData("num", "item_name")
free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
counter = 0


def check_win(choice):
    if choice[0] == choice[1] == choice[2] or \
            choice[3] == choice[4] == choice[5] or \
            choice[5] == choice[6] == choice[7] or \
            choice[0] == choice[3] == choice[6] or \
            choice[1] == choice[4] == choice[7] or \
            choice[2] == choice[5] == choice[8] or \
            choice[0] == choice[4] == choice[8] or \
            choice[6] == choice[4] == choice[2]:
        return 1
    else:
        return False


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logger.add('log_info.log', format="{time} - {level} - {message}", level='DEBUG')
print("The server is running")


@dp.message_handler(commands=['start'])
async def start(message: Message):
    logger.info("Старт новой игры")
    await message.reply("Добро пожаловать в игру крестики-нолики\n"
                        "Для начала игры нажмите - /start_game\n"
                        "Для остановки игры нажмите - /stop_game")


@dp.message_handler(commands=['start_game'])
async def show_field(message: Message):
    global play_field
    play_field = [
        [
            InlineKeyboardButton("1", callback_data="num:1"),
            InlineKeyboardButton("2", callback_data="num:2"),
            InlineKeyboardButton("3", callback_data="num:3"),
        ],
        [
            InlineKeyboardButton("4", callback_data="num:4"),
            InlineKeyboardButton("5", callback_data="num:5"),
            InlineKeyboardButton("6", callback_data="num:6"),
        ],
        [
            InlineKeyboardButton("7", callback_data="num:7"),
            InlineKeyboardButton("8", callback_data="num:8"),
            InlineKeyboardButton("9", callback_data="num:9"),
        ],
    ]
    field = InlineKeyboardMarkup(inline_keyboard=play_field)
    await message.reply(f'Первый ход {chr(10060)}\n'
                        'Сделайте ход', reply_markup=field)


@dp.callback_query_handler(action_callback.filter())
async def num_choice(callback: CallbackQuery, callback_data: dict):
    global free_choice
    global play_field
    global counter
    await callback.answer(cache_time=1)
    data = callback_data['item_name']
    if data in free_choice:
        if data == '1':
            if counter % 2:
                play_field[0][0] = InlineKeyboardButton(chr(11093), callback_data='num:1')
                free_choice[0] = 'O'
                move = chr(10060)
            else:
                play_field[0][0] = InlineKeyboardButton(chr(10060), callback_data='num:1')
                free_choice[0] = 'X'
                move = chr(11093)
        elif data == '2':
            if counter % 2:
                play_field[0][1] = InlineKeyboardButton(chr(11093), callback_data='num:2')
                free_choice[1] = 'O'
                move = chr(10060)
            else:
                play_field[0][1] = InlineKeyboardButton(chr(10060), callback_data='num:2')
                free_choice[1] = 'X'
                move = chr(11093)
        elif data == '3':
            if counter % 2:
                play_field[0][2] = InlineKeyboardButton(chr(11093), callback_data='num:3')
                free_choice[2] = 'O'
                move = chr(10060)
            else:
                play_field[0][2] = InlineKeyboardButton(chr(10060), callback_data='num:3')
                free_choice[2] = 'X'
                move = chr(11093)
        elif data == '4':
            if counter % 2:
                play_field[1][0] = InlineKeyboardButton(chr(11093), callback_data='num:4')
                free_choice[3] = 'O'
                move = chr(10060)
            else:
                play_field[1][0] = InlineKeyboardButton(chr(10060), callback_data='num:4')
                free_choice[3] = 'X'
                move = chr(11093)
        elif data == '5':
            if counter % 2:
                play_field[1][1] = InlineKeyboardButton(chr(11093), callback_data='num:5')
                free_choice[4] = 'O'
                move = chr(10060)
            else:
                play_field[1][1] = InlineKeyboardButton(chr(10060), callback_data='num:5')
                free_choice[4] = 'X'
                move = chr(11093)
        elif data == '6':
            if counter % 2:
                play_field[1][2] = InlineKeyboardButton(chr(11093), callback_data='num:6')
                free_choice[5] = 'O'
                move = chr(10060)
            else:
                play_field[1][2] = InlineKeyboardButton(chr(10060), callback_data='num:6')
                free_choice[5] = 'X'
                move = chr(11093)
        elif data == '7':
            if counter % 2:
                play_field[2][0] = InlineKeyboardButton(chr(11093), callback_data='num:7')
                free_choice[6] = 'O'
                move = chr(10060)
            else:
                play_field[2][0] = InlineKeyboardButton(chr(10060), callback_data='num:7')
                free_choice[6] = 'X'
                move = chr(11093)
        elif data == '8':
            if counter % 2:
                play_field[2][1] = InlineKeyboardButton(chr(11093), callback_data='num:8')
                free_choice[7] = 'O'
                move = chr(10060)
            else:
                play_field[2][1] = InlineKeyboardButton(chr(10060), callback_data='num:8')
                free_choice[7] = 'X'
                move = chr(11093)
        elif data == '9':
            if counter % 2:
                play_field[2][2] = InlineKeyboardButton(chr(11093), callback_data='num:9')
                free_choice[8] = 'O'
                move = chr(10060)
            else:
                play_field[2][2] = InlineKeyboardButton(chr(10060), callback_data='num:9')
                free_choice[8] = 'X'
                move = chr(11093)
        counter += 1
        logger.info(f'Игрок ввел {data}')
        if counter > 3:
            winner = check_win(free_choice)
            if winner == 1 and counter % 2 != 0:
                free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                counter = 0
                logger.info(f'Победа игрока - {chr(10060)}')
                await callback.message.answer(f"ПОБЕДА {chr(10060)}")
                await callback.answer()
            elif winner == 1 and counter % 2 == 0:
                free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                counter = 0
                logger.info(f'Победа игрока - {chr(11093)}')
                await callback.message.answer(f"ПОБЕДА {chr(11093)}")
                await callback.answer()
        if counter == 8:
            free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            counter = 0
            await callback.message.answer(f"Никто не смог победить!!!!!")
            await callback.answer()
        field = InlineKeyboardMarkup(inline_keyboard=play_field)
        await callback.message.edit_text(f'Теперь ходит {move}', reply_markup=field)
        await callback.answer()
    else:
        logger.debug('Выбрана занятая клетка')
        field = InlineKeyboardMarkup(inline_keyboard=play_field)
        await callback.message.edit_text(f'Это поле уже занято, надо выбрать другое', reply_markup=field)
        await callback.answer()


@dp.message_handler(commands=['stop_game'])
async def stop_game(message: Message):
    await message.answer(f'{message.from_user.first_name}, '
                         f'До новых встреч')
    global free_choice
    global counter
    logger.info('Игрок остановил игру')
    free_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    counter = 0


@dp.message_handler()
async def echo(message: Message):
    global play_field
    logger.debug('Не правильный выбор')
    field = InlineKeyboardMarkup(inline_keyboard=play_field)
    await message.answer(f'{message.from_user.first_name}, '
                         f'Внимательнее выбирайте поле', reply_markup=field)


executor.start_polling(dp)