""" Contains the Invoker class, which is used to run the bot in development mode. """

import sys
import json
import importlib
import asyncio

from .watcher import start_watcher_thread
from .updater import TelegramUpdater, check_updates_whitelist


class Invoker:
    """Invoker class to run the bot in development mode.

    Args:
    :param bot_handler: The path to the bot handler module.
    :param bot_token: The bot token.
    :param async_mode: Whether to run the bot in async mode or not.

    Methods:
    :method add_watcher: Adds a watcher to the invoker. The watcher will reload the bot when a file is changed.
    :method filter: Adds a filter to the invoker. The filter will only allow the given types of updates to be processed.
    :method whitelist_add: Adds a user ID to the whitelist. Only users in the whitelist will be able to use the bot.
    :method start: Start polling the bot.


    Example:
    ```python
    invoker = Invoker("src.handler.main", bot_token="yourToken", async_mode=True)

    invoker.add_watcher("src", ["src"])
    invoker.filter("message", "photo", "document", "audio", "voice", "video")
    invoker.whitelist_add(123456789)  # Your user ID here

    if __name__ == "__main__":
        invoker.start()

    ```


    """

    def __init__(self, bot_handler: str, bot_token: str, async_mode: bool = False):
        self.bot_handler = bot_handler
        self.bot_token = bot_token
        self.async_mode = async_mode

        self.watchers = {}
        self.filters = []
        self.whitelist = []

    def add_watcher(self, module_name: str, paths: list = None):
        """Adds a watcher to the invoker. The watcher will reload the bot when a file is changed.

        Args:
        :param module_name: The name of the module to watch.
        :param paths: The paths to watch.

        """

        paths = ["."] if not paths else paths

        if module_name in self.watchers:
            self.watchers[module_name].append(paths)
        else:
            self.watchers[module_name] = paths

    def filter(self, *args):
        """Adds a filter to the invoker. The filter will only allow the given types of updates to be processed.

        Args:
        :param args: The types of updates to filter.

        """

        self.filters.extend(args)

    def whitelist_add(self, user_id: int):
        """Adds a user ID to the whitelist. Only users in the whitelist will be able to use the bot.

        Args:
        :param user_id: The user ID to add to the whitelist.

        """

        self.whitelist.append(user_id)

    def start(self):
        """Start polling the bot."""

        def handler(update):
            # код обработки обновлений

            update_ = {"body": json.dumps(update)}

            type_ = list(update.keys())[1]

            if type_ not in self.filters and self.filters:
                return

            if self.whitelist:
                if not check_updates_whitelist(update, self.whitelist, type_):
                    return

            module_name, function_name = self.bot_handler.rsplit(".", 1)

            module = sys.modules.get(module_name)
            if module is None:
                module = importlib.import_module(module_name)
                sys.modules[module_name] = module
            function = getattr(module, function_name)

            if self.async_mode:
                asyncio.get_event_loop().run_until_complete(function(update_, {}))
            else:
                function(update_, {})

        t = start_watcher_thread(self.watchers, start=False) if self.watchers else None

        with TelegramUpdater(self.bot_token, t) as updater:
            updater.start_polling(handler)
