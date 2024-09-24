import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, restart_command):
        self.restart_command = restart_command
        self.process = None

    def on_modified(self, event):
        if not event.is_directory:
            print(f'Alteração detectada em {event.src_path}. Reiniciando a aplicação...')
            if self.process:
                self.process.terminate()  # Termina o processo atual
            self.process = subprocess.Popen(self.restart_command, shell=True, start_new_session=True)  # Reinicia a aplicação

def main():
    path_to_watch = "src"  # Caminho para monitorar, ajuste conforme necessário
    restart_command = "python3 src/app.py"  # Comando para reiniciar a aplicação

    event_handler = ChangeHandler(restart_command)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()