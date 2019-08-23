#得到当前脚本的绝对路径
set called=($_) 
if("$called" != " ") then 
	set script_dir=`readlink -f $called[2]` 
else 
	set script_dir=`readlink -f $0` 
endif 

set SHORTDIR=`dirname $script_dir`

setenv LD_LIBRARY_PATH $LD_LIBRARY_PATH:/scratchfs/bes/sunhk/6.6.4.p01/libssl/usr/lib
set Hepsub='python2 ${SHORTDIR}/hepsubnew.py'
set Heprm='python2 ${SHORTDIR}/Heprm.py'
set Hep_q='python2 ${SHORTDIR}/Hep_q.py'
set CheckBossJob='python2 ${SHORTDIR}/error.py'
set CheckThenSub='python2 ${SHORTDIR}/hepsuberror.py'
set Error='python2 ${SHORTDIR}/error.py'
set SubError='python2 ${SHORTDIR}/hepsuberror.py'
set Unrun='python2 ${SHORTDIR}/unrun.py'
set Runnow='python2 ${SHORTDIR}/runnow.py'
