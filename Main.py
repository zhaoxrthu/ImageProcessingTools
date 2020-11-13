import os, sys
import ImageProcessingTools.MovieLinesSplicing as iMLS
import ImageProcessingTools.SceneryMosaic as iSCM
import ImageProcessingTools.UnzipFiles as iUZF
import ImageProcessingTools.ImageToPdfs as iITP
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
for w in ["//Source", "//Finish", "//Result"]:
    if os.path.isdir(pwd + w) == 0:
        os.mkdir(pwd + w)
while True:
    print(cover)
    func = raw_input()
    if func == '1':  
        obj = iMLS.mls(pwd)
    elif func == '2':
        obj = iSCM.scm(pwd)
    elif func == '3':
        obj = iUZF.uzf(pwd)
    elif func == '4':
        obj = iITP.itp(pwd)
    elif func == 'q':   
        break
    else:   
        print("Illegal Input!")
        continue
    obj.run()
    func = raw_input()
print("Quit.")
func = raw_input()