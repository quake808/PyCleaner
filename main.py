import pycleaner
from importlib import reload
from pyfiglet import Figlet

class Menu():
    def usermenu(self):
        menu = Menu()
        custom_fig = Figlet(font='slant')
        print(custom_fig.renderText('PyCleaner'))
        print("PyCleaner - софт, разработанный на Python для безопасной очистки вашей системы от мусора.")
        print("Разработчик - quake808@protonmail.com\n")
        clean = input("- Для очистки Temp-файлов напишите 'T' \n"
                      "- Для очистки кеша браузера напишите 'W' \n"
                      "- Для проверки диска и драйверов напишите 'D' \n"
                      "- Для полной очистки напишите 'A' \n\n"
                      "Ответ: ")
        if clean == 'T':
            pycleaner.tempclean.tempcleaner()
            reload(pycleaner)
            return menu.usermenu()
        if clean == 'W':
            pycleaner.tempclean.browsercleaner()
            reload(pycleaner)
            return menu.usermenu()
        if clean == 'A':
            pycleaner.tempclean.tempcleaner()
            reload(pycleaner)
            pycleaner.tempclean.browsercleaner()
            reload(pycleaner)
            return menu.usermenu()
        if clean == 'D':
            pycleaner.tempclean.drivercheck()
            reload(pycleaner)
            return menu.usermenu()

menu = Menu()

if __name__ == "__main__":
    menu.usermenu()
