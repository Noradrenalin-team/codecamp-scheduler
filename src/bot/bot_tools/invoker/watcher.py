import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import importlib
import threading
import sys


class CodeChangeHandler(FileSystemEventHandler):
    """A handler for code changes."""

    def __init__(self, moduls: list[str]):
        super().__init__()
        self.moduls = []

        for module in moduls:
            self.moduls.append(__import__(module))

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".py"):
            print("Reloading bot...")
            for module in self.moduls:
                sys.modules[module.__name__] = importlib.reload(module)
                # получаем подмодули
                for submodule in module.__dict__.values():
                    if isinstance(submodule, type(module)):
                        sys.modules[submodule.__name__] = importlib.reload(submodule)

            print("Bot reloaded!")


def start_watcher(to_watche: dict[str, list[str]]):
    """Starts a watcher for the given module and paths."""

    paths = {}
    for module, path in to_watche.items():
        for p in path:
            if p in paths:
                paths[p].append(module)
            else:
                paths[p] = [module]


    for path, modules in paths.items():
        event_handler = CodeChangeHandler(moduls=modules)
        observer = Observer()
        observer.schedule(event_handler, path=path, recursive=True)
        observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping watcher...")
        observer.stop()

    observer.join()


def start_watcher_thread(
    to_watche: dict[str, list[str]], start=True
) -> threading.Thread:
    """Starts a watcher thread for the given module and paths. Returns the thread object."""

    thread = threading.Thread(target=start_watcher, args=(to_watche,), daemon=True)
    if start:
        thread.start()

        print("Watcher started!")

    return thread
