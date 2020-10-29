import os, sys, shutil
import time
class mls():
    def __init__(self, pwd):
        self.pwd = pwd
        self.srcPath = pwd +"\\Source"
        self.t0 = time.time()
        self.log = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.t0))]
        print("-" * 60)
        print("Movie Lines Splicing......")
        self.log.append("Movie Lines Splicing......")
        try:
            self.r = input("Input the Height Ratio of the Dialogue(Default 0.15): ")
            self.r = self.r if 0 < self.r <= 1 else 0.15
        except:
            self.r = 0.15
        print("\tratie = %f" % self.r)
        self.log.append("\tratie = %f" % self.r)
    
    def run(self):
        self.loadFiles()
        self.MergePics()
        self.WriteFiles()

    def loadFiles(self):
    
        pass