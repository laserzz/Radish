import os
import time

from colorama import Fore
from utils.create import Create

class Radish:
    def run():
        print("Welcome To..")
        time.sleep(2)

        print(
        Fore.RED + 
        """
                                  ___                     ___        ___  
                                 (   )  .-.              (   )      (   ) 
         ___ .-.      .---.    .-.| |  ( __)     .--.     | | .-.    | |  
        (   )   \    / .-, \  /   \ |  (''")   /  _  \    | |/   \   | |  
         | ' .-. ;  (__) ; | |  .-. |   | |   . .' `. ;   |  .-. .   | |  
         |  / (___)   .'`  | | |  | |   | |   | '   | |   | |  | |   | |  
         | |         / .'| | | |  | |   | |   _\_`.(___)  | |  | |   | |  
         | |        | /  | | | |  | |   | |  (   ). '.    | |  | |   | |  
         | |        ; |  ; | | '  | |   | |   | |  `\ |   | |  | |   |_|  
         | |        ' `-'  | ' `-'  /   | |   ; '._,' '   | |  | |   .-.  
        (___)       `.__.'_.  `.__,'   (___)   '.___.'   (___)(___) (   ) 
                                                                     '-'  

        """
        )

        time.sleep(1)

        while True:
            udir = input("Enter a directory for setup. ")
            if not os.path.isdir(udir):
                print("Not a directory.")

            else:
                break

        folders = []

        while True:
            uf = input("Enter a subfolder to add.\nType e to exit.\n\nAlternatively, enter all subfolders, seperated by a comma then a space. ")
            
            if uf.lower() == 'e':
                break

            if ", " in uf.lower():
                for f in uf.split(", "):
                    folders.append(f)
                break

            folders.append(uf)

        ext = input("Enter a file extension. ")

        cre = Create(dirs=folders)

        cre.make_dirs(dir=udir)
        cre.make_base_files(dir=udir, ext=ext)

        print(Fore.GREEN + "All Done! Star me on GitHub if you found me useful. <3\n\nLink: https://github.com/laserzz/Radish" + Fore.RESET)
        time.sleep(1)

Radish.run()