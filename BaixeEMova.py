import sys 
import time
import random
import os 
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSytemEventHandler

from_dir = "C:/Users/???/dowloads"
to_dir = "C:/Users/???/Desktop/dowload_files"

dir_tree = {
"Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
"video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe','.mpv', '.mp4', '.m4v', '.avi', '.mov'],
“Document Files": [*.ppt', '.xls', '.xlsx', ".csv', '.pdf', '.txt'],
"Setup Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'],
}

 class FileMovementHandler(FileSystemEventHandler):
     def on created(self, event):
     name, extension = os.path.splitext(event.src path)

     time. sleep(1)

     for key, value in dir tree.items():
         time.sleep(1)

         if extension in value:
         file name - os.path.basename(event.src path)

         print("Foi feito o download de ...” + file name)


         path1l = from dir + '/* + file name
         path2 = to dir + '/' + key
         path3 = to dir + '/' + key + '/' + file name

        if os.path.exists(path2):
            print("Acessando destino existente...”)
            time. sleep(1)


            if os.path.exists(path3):
                print("O arquivo ja existe " + key + "....”)
                print("Renomeando arquivo como " + file name +"....”)

                new file name = os.path.splitext(file name)[0] + str(random.randint(0, 999)) + os.path.splitext(file name)[1]
                path4 = to dir + '/' + key + '/' + new file name

                print("Movendo "+ new file name + "...”)
                shutil.move(pathl, path4)
                time.sleep(1)
            else:
                print("Movendo " + file name + "....”)
                Shutil.move(path1l, path3)
                time.sleep(1)
        else:
            print("Criando novo destino...”)
            os. makedirs(path2)
            print("Movendo " + file name + "....”)
            shutil.move(pathl, path3)
            time. sleep(1)

 event handler = FileMovementHandler()

 observer = Observer()

 observer. schedule(event handler, from dir, recursive-True)

try:
    while True:
        time. sleep(2)
        print("Executando programa. ..”)
        except KeyboardInterrupt:
        print("Programa finalizado!”)
        observer.stop()
