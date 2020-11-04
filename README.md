ImageProcessingTools
==========================================================
一个小工具，目前实现的功能包括：  
&emsp;&emsp;①台词截图拼接；  
&emsp;&emsp;②横向图片拼接；  
&emsp;&emsp;③批量解压缩；  
&emsp;&emsp;④图片转pdf文件。  

# 1.运行方法

&emsp;&emsp;可选择直接运行可执行文件(Windows, 64bit)或通过调用python脚本。

## 1.1 直接运行
 
&emsp;&emsp;Windows下可直接运行./dist/下的可执行文件[Main.exe](https://github.com/zhaoxrthu/ImageProcessingTools/blob/main/dist/Main.exe)。

## 1.2 调用python

&emsp;&emsp;基于Python 2.7编写，可执行下列conda命令创建Python环境并安装依赖：

    conda create -n Py27v python=2.7
    conda activate Py27v
    conda install -n Py27v pillow=6.2.1 natsort

&emsp;&emsp;或直接导入conda配置文件[Env_Py27v.yaml](https://github.com/zhaoxrthu/ImageProcessingTools/blob/main/Env_Py27v.yaml)(Windows10, 64bit, 另包括打包工具pyinstaller)。

# 2. 功能

&emsp;&emsp;运行exe文件(或调用Python脚本)，可得到下列界面：
  
![](https://github.com/zhaoxrthu/ImageProcessingTools/blob/main/dist/Pictures/interface.png) 
 
&emsp;&emsp;若当前路径下无相应文件夹，程序将自动创建./Source/, ./Result/, ./Finish/ 三个文件夹，分别用于存放待处理的资源、存放处理结果、存放处理成功后的源文件。 

&emsp;&emsp;使用[1]~[4]键选择不同的功能，使用[q]键退出。 

# 2.1 台词截图拼接

&emsp;&emsp;输入[1]选择台词截图拼接功能。输入一个小数(0~1, 默认值为0.15)表示台词高度占整个图片的比值, 既拼接过程中除封面图(第一张)外其他图片保留的高度：

![](https://github.com/zhaoxrthu/ImageProcessingTools/blob/main/dist/interface_func1.png)

&emsp;&emsp;程序将遍历./Source/文件夹下的所有图片(支持png、jpg、jpeg、bmp格式)并进行拼接，获得如下的长图：

![](https://github.com/zhaoxrthu/ImageProcessingTools/blob/main/dist/MergeResult_11032148.jpg)

&emsp;&emsp;拼接成功后结果存储为./Result/MergeResult_${TimeStamp}$.jpg，源文件统一移动到./Finish/Source_${TimeStamp}$文件夹内，程序日志写入./Result/log.txt中。

# 2.2 横向图片拼接
&emsp;&emsp;输入[2]选择横向图片拼接功能。程序将遍历./Source/文件夹下的所有图片(支持png、jpg、jpeg、bmp格式)并进行拼接，获得如下的图片：

![](https://github.com/zhaoxrthu/ImageProcessingTools/blob/main/dist/MosaicResult_10311430.jpg)

&emsp;&emsp;拼接成功后结果存储为./Result/MosaicResult_${TimeStamp}$.jpg，源文件统一移动到./Finish/Source_${TimeStamp}$文件夹内，程序日志写入./Result/log.txt中。

# 2.3 批量解压缩
&emsp;&emsp;输入[3]选择批量解压缩功能。程序将遍历./Source/文件夹下的所有压缩包(目前仅支持.zip文件)，逐一解压到./Result/文件夹下。解压成功的压缩包移动到./Finish/Source_${TimeStamp}$文件夹内，程序日志写入./Result/log.txt中。

# 2.4 图片转pdf文件
&emsp;&emsp;输入[4]选择图片转pdf文件功能。程序将遍历./Source/文件夹下的所有有图片(支持png、jpg、jpeg、bmp格式))的文件夹，将其逐一压制为pdf文件。程序会对单个文件夹下的图片按文件名进行自然排序，可输入命名前缀(默认为空值)：

![](https://github.com/zhaoxrthu/ImageProcessingTools/blob/main/dist/interface_func4.png)

![](https://github.com/zhaoxrthu/ImageProcessingTools/blob/main/dist/Pic2PdfResult_11041716.png)

&emsp;&emsp;压制后的pdf文件将命名为${命名前缀}$${文件夹名}$.pdf并保存到./Result/pdf/文件夹下，源文件统一移动到./Finish/Source_${TimeStamp}$文件夹内，程序日志写入./Result/log.txt中。








