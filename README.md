# BaskeAnaTool

如何使用
=====================================
使用只需要下列一个命令，不需要额外的要求。

   `source ./setup.sh`


有哪些功能
=========

## 批量提交作业 ``Hepsub''
### 两种典型的作业
常用的两种作业为：BOSS作业，Bash作业。前者用boss.condor提交，后者用hep_sub进行提交。
Hepsub有选项可以控制提交何种作业
   * -txt
   * -sh

前者用来提交BOSS作业，后者用来提交Bash文件作业。更复杂的任务可以通过一下的选项实现，
这些选项可以单个或多个一起使用。
#### 其他的开关
   * 指定文件或文件夹
     比如 Hepsub -sh jobs 
     Hepsub -txt jpsi_*
   * -r 递归的提交指明目录下的全部所需作业
    比如 Hepsub -sh -r jobs
    比如 Hepsub -sh -r .
#### 指明提交作业的命令
    * sub='sub commands'
#### 指定作业的类型
作业的类型也可以自主定义
  * type='pdf, cxx, C'
    其中文件类型用‘，’隔开
#### 指定作业的执行方式
受服务器现在，现有用特定程序执行某项任务，只能曲线救国。首先一个与之对于的Bash
    文件会自动生成，这个Bash文件将把文件的执行方式写入，如入
    root -l -b -q fit.C 
    随后这个Bash文件将被提交，间接实现用‘root’执行此文件。
    *exe="command" 这个选项会指定执行方式


        
### B) make jobs, only the reconstruction and simulation jobs can be made
	usage:
        SimJpsi [decay.card] [number of events]
    
    different type
        Sim3770 
        SimNewJpsi
        SimJpsi
        Sim4180

