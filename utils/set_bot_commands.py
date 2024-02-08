from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("command", "Command"),
            types.BotCommand("ro", "Read Only"),
            types.BotCommand("unro", "Unban Read Only"),
        ]
    )
