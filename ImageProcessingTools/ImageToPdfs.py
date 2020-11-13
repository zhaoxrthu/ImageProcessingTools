from PIL import Image, ImageFile
import sys, os, shutil, gc, time
import natsort
ImageFile.LOAD_TRUNCATED_IMAGES = True
class itp():
    def __init__(self, pwd):
        self.pwd = pwd
        self.srcPath = pwd + "//Source"
        self.fnsPath = pwd + "//Finish"
        self.resPath = pwd + "//Result"
        self.logPath = pwd + "//Result//log.txt"
        self.foldList = []
        self.SuccedList, self.FailedList = [], []
        self.t0 = time.time()
        self.srcSize, self.resSize = 0, 0
        self.log = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.t0))]
        print("-" * 61)
        print("Turn Images to Pdf......")
        self.log.append("Turn Images to Pdf......")
        self.prefix = raw_input("Input The Prefix: ")

    def run(self):
        self.createTables()
        print("The Source Folder Has %d Folder(s)" % (len(self.foldList)))
        for i, name in enumerate(self.foldList):
            print("\r\tTuring %s[%d/%d]......" % (name, i + 1, len(self.foldList)))
            self.t = time.time()
            try:
                imageList, sumSize = self.loadImages(self.srcPath + "//" + name)
                if len(imageList) > 0:
                    self.writeImagesToPdf(imageList, name, sumSize)
                    self.SuccedList.append(name)
                    self.log.append(name + ":")
            except Exception as e:
                ex_type, ex_val, ex_stack = sys.exc_info()
                print(ex_type)
                print(ex_val)
                self.FailedList.append(name)
                if os.path.exists(self.srcPath + "//" + name):
                    os.remove(self.srcPath + "//" + name)
            del imageList
            gc.collect()
        self.moveAndLog()

    def createTables(self):
        for name in os.listdir(self.srcPath):
            if os.path.isdir(self.srcPath + "//" + name):
                self.foldList.append(name)

    def loadImages(self, fdPath):
        name = fdPath.split("//")[-1]
        picList, picNameList = [], []
        self.fp = []
        sumSize = 0
        try:
            for picName in os.listdir(fdPath):
                suffix = picName.split(".")[-1]
                if suffix.lower() in ["jpg", "jpeg", "png", "bmp"]:
                    picNameList.append(picName)
            picNameList = natsort.natsorted(picNameList)
        except:
            return []
        for picName in picNameList:
            fp = open(fdPath + "//" + picName, 'rb')
            img = Image.open(fp)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            picList.append(img)
            sumSize = sumSize + os.path.getsize(fdPath + "//" + picName)
            self.fp.append(fp)
        return picList, sumSize

    def writeImagesToPdf(self, imageList, name, sumSize):
        if os.path.isdir(self.resPath + "//pdf") == 0:
            os.mkdir(self.resPath + "//pdf")
        pathstr = self.resPath + "//pdf//" + self.prefix + name + '.pdf'
        try:
            imageList[0].save(pathstr, 'PDF', resolution = 100.0, 
                              save_all = True, append_images = imageList[1:])
            print('\tTurning ' + name + ' to a pdf succeed!')  
            flag, fileSize = True, os.path.getsize(pathstr)              
        except Exception as e:
            print("Save Error!")
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)
            print(ex_val)
            if os.path.exists(pathstr):
                os.remove(pathstr)
            print('Turning ' + name + ' to a pdf failed!')    
            flag, fileSize = False, 0.0
        str = "\tPic Num/Dir Size/Pdf Size/Time: %d/%fMb/%fMb/%fs" % \
                (len(imageList), sumSize/1048576.0, fileSize/1048576.0,time.time()-self.t)
        print(str)
        self.log.append(str)
        print('\n')
        for fp in self.fp:
            fp.close()

    def moveAndLog(self):
        timeStamp = time.strftime('%m%d%H%M', time.localtime(self.t0))
        os.mkdir(self.fnsPath + "//Source_%s" % (timeStamp))
        curStr = "Moving Finished Folders to //Finish//Source_%s" % (timeStamp)
        curFnsPath = self.fnsPath + "//Source_%s" % (timeStamp)
        print(curStr)
        self.log.append(curStr)
        logFile = open(self.logPath, "a+")
        for str in self.log:
            logFile.write(str + '\n')
        str = "Turning Situation: "
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