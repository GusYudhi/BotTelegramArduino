import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Initialize the bot
bot = Bot(token="7181750288:AAEsny_8Yxefryhbe3Z5-FW3qZB4X8AFzK0")
dp = Dispatcher(bot)

# Function to handle the /mulaiBot command
@dp.message_handler(commands=['mulaiBot'])
async def start(message: types.Message):
    await message.reply("Halo! Saya adalah bot dari TeamUno1. Bagaimana kabarmu? Sudah makan? Belum? Lapar dong.")
    await message.reply("Silahkan Ketik /mulaiUno untuk mengakses tombol")

# Function to handle the /mulaiUno command
@dp.message_handler(commands=['mulaiUno'])
async def opsi_uno(message: types.Message):
    # Create a keyboard with initial options
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Relay 1", callback_data="relay1"))
    keyboard.add(types.InlineKeyboardButton(text="Relay 2", callback_data="relay2"))
    keyboard.add(types.InlineKeyboardButton(text="Red Censor", callback_data="red_censor"))

    # Send a message with the initial options
    await message.reply("Pilih perangkat yang ingin diatur:", reply_markup=keyboard)

# Function to handle button clicks
@dp.callback_query_handler(lambda c: True)
async def handle_button_click(callback_query: types.CallbackQuery):
    # Get the data associated with the button clicked
    button_data = callback_query.data
    # Get the ID of the user who clicked the button
    user_id = callback_query.from_user.id

    if button_data == "relay1":
        # Create a keyboard with options for Relay 1
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Hidup", callback_data="relay1_hidup"))
        keyboard.add(types.InlineKeyboardButton(text="Mati", callback_data="relay1_mati"))

        # Send a message with the options for Relay 1
        await bot.send_message(user_id, "Pilih status untuk Relay 1:", reply_markup=keyboard)

    elif button_data == "relay2":
        # Create a keyboard with options for Relay 2
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Hidup", callback_data="relay2_hidup"))
        keyboard.add(types.InlineKeyboardButton(text="Mati", callback_data="relay2_mati"))

        # Send a message with the options for Relay 2
        await bot.send_message(user_id, "Pilih status untuk Relay 2:", reply_markup=keyboard)

    elif button_data == "red_censor":
        # Create a keyboard with options for Red Censor
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Hidup", callback_data="red_censor_hidup"))
        keyboard.add(types.InlineKeyboardButton(text="Mati", callback_data="red_censor_mati"))

        # Send a message with the options for Red Censor
        await bot.send_message(user_id, "Pilih status untuk Red Censor:", reply_markup=keyboard)

async def main():
    # Start polling for updates
    await dp.start_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
