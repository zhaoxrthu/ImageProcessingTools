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
                mrgImage.paste(curIm.crop((0, cvrH, L, H)), (0, upH, L, upH + strH))
                fp.close()
                upH = upH + strH
            self.resImg = mrgImage
        except Exception as e:
            ex_type, ex_val, ex_stack = sys.exc_info()
            print(ex_type)
            print(ex_val)
        return

