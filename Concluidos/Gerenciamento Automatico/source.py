import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
rodando = True
tmpx = 60
git_ignore = ['.git/', '*/.git/*', '.git/*']


class MeuManipulador(PatternMatchingEventHandler):

    

    def __init__(self):
        super().__init__(
            ignore_patterns = git_ignore,
            ignore_directories = False
)
        self.tmprd = True
        self.tmp = tmpx
        self.last = time.time()
        self.a = 0

    def timecheck(self):
        timepss = time.time() - self.last
        if self.tmprd == True:
            return True
        if timepss <= tmpx:
            self.tmprd = True
            return True
        else: 
            return False
        
    def gitcall(self):
    
        if self.timecheck() == True:
            try:
                subprocess.run(['git', 'add', '.'], check=True)
                msg = f"Autosave ({time.ctime()}): {self.a} changes"
                subprocess.run(["git", "commit", "-m", msg])
                subprocess.run(["git", "push"], check=True)
                self.tmprd = False
                self.last = time.time()
                self.a = 0
                return 0
            except subprocess.CalledProcessError as e:
                print(f"error on git: {e.stderr.strip()}")
                self.tmprd = True
                return -1
        else:
            return -2

    
    def on_modified (self, event):
        print(f"[{time.ctime()}] modified {event.src_path}")
        self.a += 1
        if self.a > 15: 
            self.gitcall()
    
    def on_moved (self, event):
        print(f"[{time.ctime()}] moved {event.src_path}")
        self.a += 1
        if self.a > 15: 
            self.gitcall()


    def on_deleted(self, event):
        print(f"[{time.ctime}] deleted on: {event.src_path}")
        self.a += 1
        if self.a > 15: 
            self.gitcall()

    def on_created (self, event):
        print(f"[{time.ctime}] created {event.src_path}")  
        self.a += 1
        if self.a > 15: 
            self.gitcall()
        

###############################################################################################


path = "."


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
