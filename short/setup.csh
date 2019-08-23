#得到当前脚本的绝对路径
set called=($_) 
if("$called" != " ") then 
	set script_dir=`readlink -f $called[2]` 
else 
	set script_dir=`readlink -f $0` 
endif 

setenv SHORTDIR `dirname $script_dir`

setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:/scratchfs/bes/sunhk/6.6.4.p01/libssl/usr/lib
setenv Hepsub 'python2 ${SHORTDIR}/hepsubnew.py'
setenv Heprm 'python2 ${SHORTDIR}/Heprm.py'
setenv Hep_q 'python2 ${SHORTDIR}/Hep_q.py'
setenv CheckBossJob 'python2 ${SHORTDIR}/error.py'
setenv CheckThenSub 'python2 ${SHORTDIR}/hepsuberror.py'
setenv Error 'python2 ${SHORTDIR}/error.py'
setenv SubError 'python2 ${SHORTDIR}/hepsuberror.py'
setenv Unrun 'python2 ${SHORTDIR}/unrun.py'
setenv Runnow 'python2 ${SHORTDIR}/runnow.py'
