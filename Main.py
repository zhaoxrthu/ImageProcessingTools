import os, sys
import ImageProcessingTools.MovieLinesSplicing as iMLS
#from ImageProcessingTools import *
#from ImageProcessingTools import MovieLinesSplicing
#from ImageProcessingTools import MovieLinesSplicing as ipts.MLS
cover = """
#############################################################
#                 Image Processing Tools(v1.0)              #
#                                                  by Zhaoxr#
#Tools:                                                     #
#   1. Movie Lines Splicing                                 #
#   2. Scenery Mosaic                                       #
#   3. Unzip Files                                          #
#   4. Turn Pictures to Pdf.                                #
#                                                           #
#Print [1]-[4] to Choose a Function, and [q] to quit.       #
#############################################################
"""
pwd = os.getcwd()
while True:
    print(cover)
    func = raw_input()
    if func == '1':  
        obj = iMLS.mls(pwd)
    elif func == '2':   
        pass
    elif func == '3':   
        pass
    elif func == '4':   
        pass
    elif func == 'q':   
        break
    else:   
        print("Illegal Input!")
    obj.run()
print("Quit.")