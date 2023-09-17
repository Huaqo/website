from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from build import build

class Watcher(LoggingEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith((".md",".css",".html")):
            print("Rebuilding site")
            build()

if __name__ == "__main__":
    event_watcher = Watcher()
    observer = Observer()
    directories_to_watch = ['content', 'assets', 'templates']
    for directory in directories_to_watch:
        observer.schedule(event_watcher, path=directory, recursive=True)
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
            
    finally:
        observer.stop()
        observer.join()