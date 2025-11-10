import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

rodando = True

class MeuManipulador(FileSystemEventHandler):
    def __init__(self):
        self.a = 0
    
    def on_modified (self, event):
        print(f"[{time.ctime()}] modified {event.src_path}")
        self.a += 1
    def on_deleted(self, event):
        print(f"[{time.ctime}] deleted on: {event.src_path}")
        self.a += 1
    def on_created (self, event):
        print(f"[{time.ctime}] created {event.src_path}")  
        self.a += 1

###############################################################################################

path = "../.." 


event_handler = MeuManipulador()


observer = Observer()


observer.schedule(event_handler, path, recursive=True)


observer.start()

print(f"ativo em: {path}")


try:
    
    while rodando:
        
        time.sleep(1)


except KeyboardInterrupt:
    print(f"{event_handler.a} mudancas foram feitas")
    observer.stop()


observer.join()

print("finalizado.")