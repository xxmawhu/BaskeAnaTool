# BaskeAnaTool
## 如何安装
首先要从github上拷贝下来，只需要下面一个命令，因为服务器上有装好的git软件，不需要安装额外的软件。
```git clone https://github.com/xxmawhu/BaskeAnaTool.git```
如何使用
=====================================
使用只需要下列一个命令，不需要额外的要求。这是针对IHEP服务器设置的环境，个人电脑上不能保证能正常使用。

   `source setup.sh`


有哪些功能
=========

## 批量提交作业 "Hepsub"
### 两种典型的作业
常用的两种作业为：BOSS作业，Bash作业。前者用boss.condor提交，后者用hep_sub进行提交。这是IHEP服务器提供的两种接口。
Hepsub命令含有选项可以控制提交何种作业，包括
   * -txt
   * -sh

前者用来提交BOSS作业，后者用来提交Bash文件作业。交作业的时候请务必指定作业类型。建议养成一个好习惯，
不要所有的文件都没有后缀，不同类型的文件加上相应的后缀是大有裨益的。
更复杂的任务可以通过一下的选项实现，这些选项可以单个或多个一起使用。
#### 其他的选项
   * 指定文件或文件夹

     比如 `Hepsub -sh jobs`就是将文件夹`jobs`下面的所有文件都交到服务器运行；

     `Hepsub -txt jpsi_*`就是将所有的以`jspi`开头的文件交到服务器运行；
   * -r 递归的提交指明目录下的全部所需作业
    比如 `Hepsub -sh -r jobs`不仅把`jobs`下面的作业交到服务器，而且将子文件夹下及子子文件夹下的，依次类推；
    比如 `Hepsub -sh -r .`这`.`代表当前文件夹。
#### 指明提交作业的命令

    * sub='sub commands'

这个设计是考虑到服务器的接口有可能出现变化，也有可能是私人服务器的命令可能稍微不同，这样能最灵活的利用这套工具。
#### 指定作业的类型
作业的类型也可以自主定义

  * type='pdf, cxx, C'

其中文件类型用‘，’隔开。这是为了做初步筛选的方便，也是为了程序的运行方便，从实际运用来看，这项功能的使用频率很低。
#### 指定作业的执行方式
受服务器现在，只能用两种特定程序执行某项任务，包括`boss.exe`和`bash`，前者是进行数据分析的重要框架，后者是一种
比较通用的脚本语言，如果用户想使用`python`或者`root`，只能曲线救国。首先一个与之对于的Bash文件，在bash文件里指明
运行`python`程序等，比如
 ```bash
 #!/bin/usr/env root
 root -l -b -q fit.C 
```
这个脚本能够实现使用服务器运行`root`程序。
若按如下的方式指定运行作业的命令
* exe="command" 

那么这个系统会自动生成一个与之对应的bash脚本并提交到服务器。如果没有指定作业的运行方式，默认
`C`文件用`root`执行，`py`文件用`python`执行。

        
## 自动生成MC模拟文件并提交
对每个对撞能区，都有不同的命令来批量的生成模拟文件，并提交。每个命令都是有同一个
基类派生出来。对于暂时没有考虑到的模拟情况，我们设置了一个脚本，只有把任何一个模拟的
模板放进去，都会自动生成相应的命令。以Jpsi的模拟为例，典型的用法如下：
     SimJpsi [decay.card] [number of events]

第一个参数为模拟需要的卡片，第二个参数为期望模型的事例数。
除了模拟为，还有如下的默认命令:
* Sim3770 
* SimNewJpsi
* SimJpsi
* Sim4180

### 添加新的模拟类型
需要准备好模拟和重建样板，比如: template/simExample.txt 和
template/recExample.txt, 在SimAndRec下，修改gen.py
```python
name = "Example"
simff="template/simExample.txt"
recff="template/recExample.txt"
import Gen
g = Gen.process(name, simff, recff)
g.Make()
```

执行gen.py即可。需要注意一点，模板之中不能出现断行。

### 有问题？
请邮件联系maxx@ihep.ac.cn
