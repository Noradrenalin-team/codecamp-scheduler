""" This is the main file to run the bot in development mode."""

import os

from bot_tools import Invoker

bot_token = "" # Your bot token here

invoker = Invoker(
    "bot.handler.main",
    bot_token=bot_token,
    async_mode=True,
)

invoker.add_watcher("bot", ["bot"])  # Следит за изменениями в папке bot и перезапускает бота

# invoker.whitelist_add(123)  # Your user ID here

os.environ["TOKEN"] = bot_token

if __name__ == "__main__":
    invoker.start()
