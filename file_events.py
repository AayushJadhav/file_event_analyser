import os
import shutil
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

tracking_dir = "C:/Users/Ayush/Downloads"

class EventHandler (FileSystemEventHandler):
    def on_created(self, event):
        print(f"{event.src_path} has been created in downloads...")
    
    def on_moved(self, event):
        print(f"{event.src_path} has been moved from downloads...")
    
    def on_deleted(self, event):
        print(f"{event.src_path} has been deleted from downloads...")
    
    def on_modified(self, event):
        print(f"{event.src_path} has been modified in downloads...")

event_handler = EventHandler()

observer = Observer()

observer.schedule(event_handler, tracking_dir, True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopping...")
    observer.stop()