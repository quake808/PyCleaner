import os
import glob

class TempCleaner():
    def __init__(self):
        # Корневая папка
        homepath = os.getenv('USERPROFILE')

        # Системный мусор.
        usertemp = glob.glob(homepath + "/AppData/Local/Temp/*")
        wintemp = glob.glob("/Windows/Temp/*")

        # Кеш браузеров.
        chromecache = glob.glob(homepath + "/AppData/Local/Google/Chrome/User Data/Default/Cache/Cache_Data/*")
        edgecache = glob.glob(homepath + "/AppData/Local/Microsoft/Edge/User Data/Default/Cache/Cache_Data/*")
        operacache = glob.glob(homepath + "/AppData/Local/Opera Software/Opera Stable/*")
        mozillacache = glob.glob(homepath + "/AppData/Local/Mozilla/Firefox/Profiles/*")

        # Путь к браузерам.
        chromepath = (homepath + "/AppData/Local/Google/Chrome/")
        edgepath = (homepath + "/AppData/Local/Microsoft/Edge/")
        operapath = (homepath + "/AppData/Local/Opera Software/")
        mozillapath = (homepath + "/AppData/Local/Mozilla/Firefox/")

        # Статистика чистки Temp-файлов.
        temp_success_counter = 0
        temp_failed_counter = 0
        temp_files_size = 0

        # Статистика чистки кеша браузера.
        web_success_counter = 0
        web_failed_counter = 0
        web_files_size = 0

        # Инициализируем переменные.
        self.usertemp = usertemp
        self.wintemp = wintemp

        self.chromecache = chromecache
        self.edgecache = edgecache
        self.operacache = operacache
        self.mozillacache = mozillacache

        self.chromepath = chromepath
        self.edgepath = edgepath
        self.operapath = operapath
        self.mozillapath = mozillapath

        self.temp_success_counter = temp_success_counter
        self.temp_failed_counter = temp_failed_counter
        self.temp_files_size = temp_files_size

        self.web_success_counter = web_success_counter
        self.web_failed_counter = web_failed_counter
        self.web_files_size = web_files_size

    def deletefunc(self, cache):
        for file in cache:
            # print(file)
            size = os.path.getsize(file) / (1024 * 1024)
            filesize = float('{:.3f}'.format(size))
            try:
                os.remove(file)
                # print("Deleted " + str(file))
                checker = True
                deleted_size = True
                if checker == True:
                    self.temp_success_counter += 1
                if deleted_size == True:
                    self.temp_files_size += filesize

            except OSError as e:
                # print("Error: %s : %s" % (file, e.strerror))
                checker = False
                if checker == False:
                    self.temp_failed_counter += 1

    def deletefuncweb(self, webcache):
        for file in webcache:
            # print(file)
            size = os.path.getsize(file) / (1024 * 1024)
            filesize = float('{:.3f}'.format(size))
            try:
                os.remove(file)
                # print("Deleted " + str(file))
                checker = True
                deleted_size = True
                if checker == True:
                    self.web_success_counter += 1
                if deleted_size == True:
                    self.web_files_size += filesize

            except OSError as e:
                # print("Error: %s : %s" % (file, e.strerror))
                checker = False
                if checker == False:
                    self.web_failed_counter += 1


    def tempcleaner(self):
        tempclean.deletefunc(self.usertemp)
        tempclean.deletefunc(self.wintemp)

        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print(f"Успешно очищено: {self.temp_success_counter} файлов.")
        print(f"Не удаленные, используемые системой файлы: {self.temp_failed_counter} файлов.")
        print(f"Освобождено места: {self.temp_files_size} MB")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")

    def browsercleaner(self):
        if os.path.exists(self.chromepath):
            tempclean.deletefuncweb(self.chromecache)
        else:
            print("\n- Chrome browser не найден!")

        if os.path.exists(self.edgepath):
            tempclean.deletefuncweb(self.edgecache)
        else:
            print("\n- Edge browser не найден!")

        if os.path.exists(self.operapath):
            tempclean.deletefuncweb(self.operacache)
        else:
            print("\n- Opera browser не найден!")

        if os.path.exists(self.mozillapath):
            tempclean.deletefuncweb(self.mozillacache)
        else:
            print("\n- Firefox browser не найден!")

        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print(f"Успешно очищено: {self.web_success_counter} файлов.")
        print(f"Не удаленные, используемые браузером файлы: {self.web_failed_counter} файлов.")
        print(f"Освобождено места: {self.web_files_size} MB")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")

    def drivercheck(self):
        disk = 'chkdsk'
        os.system(disk)

tempclean = TempCleaner()
