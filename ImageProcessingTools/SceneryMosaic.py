import os, sys, shutil
import time
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
class scm():
    def __init__(self, pwd):
        self.pwd = pwd
        self.srcPath = pwd + "//Source"
        self.fnsPath = pwd + "//Finish"
        self.resPath = pwd + "//Result"
        self.logPath = pwd + "//Result//log.txt"
        self.t0 = time.time()
        self.picNum = 0
        self.srcSize, self.resSize = 0, 0
        self.log = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.t0))]
        print("-" * 61)
        print("Scenery Mosaic......")
        self.log.append("Scenery Mosaic ......")

    def run(self):
        self.loadFiles()
        self.WriteFiles()

    def loadFiles(self):
        print("Loading Pictures from: //Source")
        self.log.append("Loading Pictures from: //Source")
        picPaths = []
        if len(os.listdir(self.srcPath)) == 0:
            print("There is No Picture in the //Source.")
            self.log.append("There is No Picture in the //Source.")
            return
        for fileName in os.listdir(self.srcPath):
            fullPath = self.srcPath + '//' + fileName
            if os.path.isdir(fullPath):
                continue
            if fileName.split('.')[-1] in ['png', 'jpg', 'jpeg', 'bmp']:
                picPaths.append(fullPath)
                self.picNum = self.picNum + 1
        fp = open(picPaths[0],'rb')
        imgCover = Image.open(fp)
        L, H = imgCover.size[0], imgCover.size[1]
        unL = L // self.picNum
        L = unL * self.picNum
        fp.close()        
        scmImage = Image.new('RGB', (L, H))
        try:
            for i, picpath in enumerate(picPaths):
                curSize = os.path.getsize(picpath)
                logStr = "\t%s, %.1fkb" % (picpath.split("//")[-1], curSize/1024.0)
                print(logStr)
                self.log.append(logStr)
                fp = open(picpath,'rb')
                curIm = Image.open(fp)
                curL, curH = curIm.size[0], curIm.size[1]
                curunL = curL // self.picNum
                curL = curunL * self.picNum
                curIm = curIm.crop((curunL * i, 0, curunL * (i + 1), curH))
                scmImage.paste(curIm.resize((unL, H)), (unL * i, 0, unL * (i + 1), H))
                fp.close()
            self.resImg = scmImage
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)
            print(ex_val)
        return

    def WriteFiles(self):
        timeStamp = time.strftime('%m%d%H%M', time.localtime(self.t0))
        try:
            self.resImg.save(self.resPath + "//MosaicResult_" + timeStamp + '.jpg')
            curStr = "Saving Merged Pictures as //Result//MosaicResult_" + timeStamp + ".jpg"
            print(curStr)
            self.log.append(curStr)
            shutil.move(self.srcPath, self.fnsPath)
            oldName = self.fnsPath + "//Source"
            newName = self.fnsPath + "//Source_%s" % (timeStamp)
            os.rename(oldName, newName)
            os.mkdir(self.srcPath)
            curStr = "Moving Source Pictures to //Finish//Source_%s" % (timeStamp)
            print(curStr)
            self.log.append(curStr)
            logFile = open(self.logPath, "a+")
            for str in self.log:
                logFile.write(str + '\n')
            logFile.write('\n')
            logFile.close()
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)
            print(ex_val)

