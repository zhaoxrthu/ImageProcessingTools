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
  
![界面图片](https://github.com/zhaoxrthu/ImageProcessingTools/tree/main/dist/interface.png) 
 
&emsp;&emsp;若当前路径下无相应文件夹，程序将自动创建./Source/, ./Result/, ./Finish/ 三个文件夹，分别用于存放待处理的资源、存放处理结果、存放处理成功后的源文件。  

# 2.1 台词截图拼接






