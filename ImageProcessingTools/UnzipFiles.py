import sys, os, shutil, gc, time
import zipfile
class uzf():
    def __init__(self, pwd):
        self.pwd = pwd
        self.srcPath = pwd + "//Source"
        self.fnsPath = pwd + "//Finish"
        self.resPath = pwd + "//Result"
        self.logPath = pwd + "//Result//log.txt"
        self.RarList, self.ZipList = [], []
        self.SuccedList, self.FailedList = [], []
        self.t0 = time.time()
        self.log = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.t0))]
        print("-" * 61)
        print("Unzip Files......")
        self.log.append("Unzip Files......")

    def run(self):
        self.createTables()
        self.deCompression()
        self.moveAndLog()

    def createTables(self):
        for name in os.listdir(self.srcPath):
            _ , type= os.path.splitext(name)
            if type in ['.rar','.RAR',]:
                self.RarList.append(name)
            if type in ['.zip','.ZIP',]:
                self.ZipList.append(name)
        str = 'The Source Folder Has %d Rar File(s) and %d Zip File(s)'\
            %(len(self.RarList),len(self.ZipList))
        print(str)
        self.log.append(str)

    def deCompression(self):
        for name in self.ZipList:
            try:
                if os.path.isdir(self.resPath) == 0:
                    os.mkdir(self.resPath)
                fz = zipfile.ZipFile(self.srcPath +'//' + name, 'r')
                for file in fz.namelist():
                    fz.extract(file, self.resPath)
                self.SuccedList.append(name)      
                print(name + ' unzip successd!')
            except:
                self.FailedList.append(name)
                print(name + ' unzip failed')
        str1 = 'Unrar/Unzip is over!'
        str2 = 'Successed/Failed files: %d/%d'%\
            (len(self.SuccedList),len(self.FailedList))
        print(str1)
        self.log.append(str1)
        print(str2)
        self.log.append(str2)

    def moveAndLog(self):
        timeStamp = time.strftime('%m%d%H%M', time.localtime(self.t0))
        os.mkdir(self.fnsPath + "//Source_%s" % (timeStamp))
        curStr = "Moving Zipfiles to //Finish//Source_%s" % (timeStamp)
        curFnsPath = self.fnsPath + "//Source_%s" % (timeStamp)
        print(curStr)
        self.log.append(curStr)
        logFile = open(self.logPath, "a+")
        for str in self.log:
            logFile.write(str + '\n')
        logFile.write('\n')
        str = "Decompression Situation: "
        print(str)
        logFile.write(str + '\n')
        for name in self.SuccedList:
            str = 'S: ' + name
            print(str)
            logFile.write(str + '\n')
        for name in self.FailedList:
            str = 'F: ' + name
            print(str)
            logFile.write(str + '\n')
        logFile.close()
        for name in self.SuccedList:
            try:
                shutil.move(self.srcPath + "//" + name, curFnsPath + "//" + name)
            except Exception as e:
                ex_type, ex_val, ex_stack = sys.exc_info()
                print(ex_type)
                print(ex_val)