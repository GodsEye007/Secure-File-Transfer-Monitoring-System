import time
import hashlib
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

LOG_FILE = "logs/file_activity.log"
SENSITIVE_DIR = os.path.abspath("sensitive")

def calculate_hash(filepath):
    try:
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return "N/A"

class FileMonitor(FileSystemEventHandler):

    def log_event(self, event_type, path):

        # Ignore log file itself
        if "logs/file_activity.log" in path:
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_hash = calculate_hash(path)

        alert = ""
        if path.startswith(SENSITIVE_DIR):
            alert = "⚠️ ALERT: Sensitive file activity detected!"

        log_entry = f"[{timestamp}] {event_type} - {path} | HASH: {file_hash} {alert}\n"

        with open(LOG_FILE, "a") as log:
            log.write(log_entry)

        print(log_entry.strip())

    def on_created(self, event):
        if not event.is_directory:
            self.log_event("CREATED", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.log_event("MODIFIED", event.src_path)

    def on_deleted(self, event):
        self.log_event("DELETED", event.src_path)

    def on_moved(self, event):
        self.log_event("MOVED", f"{event.src_path} -> {event.dest_path}")

if __name__ == "__main__":
    path = os.path.abspath(".")
    event_handler = FileMonitor()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("🔍 Monitoring started... Press CTRL+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
