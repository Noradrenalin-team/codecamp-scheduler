import requests
import time
import threading


class TelegramUpdater:
    def __init__(self, bot_token, watcher_thread: threading.Thread = None):
        self.bot_token = bot_token
        self.watcher_thread = watcher_thread

        self.webhook_url = None

    def __enter__(self):
        webhook = self.get_webhook_info()

        if webhook["ok"]:
            webhook = webhook["result"]
            if webhook.get("url"):
                self.webhook_url = webhook["url"]
                self.delete_webhook()

        if self.watcher_thread:
            self.watcher_thread.start()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # if self.watcher_thread:
        #     self.watcher_thread._stop()

        if self.webhook_url:
            self.set_webhook(self.webhook_url)

    def get_webhook_info(self):
        response = requests.get(
            f"https://api.telegram.org/bot{self.bot_token}/getWebhookInfo", timeout=35
        )
        return response.json()

    def delete_webhook(self):
        requests.get(
            f"https://api.telegram.org/bot{self.bot_token}/deleteWebhook", timeout=35
        )

    def set_webhook(self, webhook_url):
        requests.get(
            f"https://api.telegram.org/bot{self.bot_token}/setWebhook?url={webhook_url}",
            timeout=35,
        )

    def get_updates(self, offset=None, timeout=10):
        params = {"offset": offset, "timeout": timeout}
        response = requests.get(
            f"https://api.telegram.org/bot{self.bot_token}/getUpdates",
            params=params,
            timeout=35,
        )
        return response.json()

    def start_polling(self, handler):
        """Start polling the bot."""

        self.delete_webhook()

        try:
            offset = None
            while True:
                updates = self.get_updates(offset=offset)
                if updates["ok"]:
                    updates = updates["result"]
                    if updates:
                        for update in updates:
                            handler(update)
                            offset = update["update_id"] + 1
                else:
                    print(
                        "Error occurred while getting updates:", updates["description"]
                    )
                    break

                time.sleep(0.1)

        except Exception as e:
            print(e)


def check_updates_whitelist(update, whitelist, type_):
    """Проверяет, есть ли в списке разрешенных пользователей пользователь, отправивший сообщение.
    Если пользователь не найден, то возвращает False, иначе True."""

    if type_ == "message":
        user_id = update["message"]["from"]["id"]
    elif type_ == "callback_query":
        user_id = update["callback_query"]["from"]["id"]
    elif type_ == "inline_query":
        user_id = update["inline_query"]["from"]["id"]
    elif type_ == "chosen_inline_result":
        user_id = update["chosen_inline_result"]["from"]["id"]

    if user_id in whitelist:
        return True
    else:
        return False
