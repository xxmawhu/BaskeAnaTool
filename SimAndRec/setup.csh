#得到当前脚本的绝对路径
set called=($_) 
if("$called" != " ") then 
	set script_dir=`readlink -f $called[2]` 
else 
	set script_dir=`readlink -f $0` 
endif 

set SIMANDRECDIR=`dirname $script_dir`
echo "NUMFILE='$SIMANDRECDIR/.NUM'" > $SIMANDRECDIR/NUM.py
set SimPsi2S="python ${SIMANDRECDIR}/initPsi2S.py"
set Sim3770="python ${SIMANDRECDIR}/init3770.py"
set SimNewJpsi="python ${SIMANDRECDIR}/initNewJpsi.py"
set SimJpsi="python ${SIMANDRECDIR}/initJpsi.py"
set Sim4600="python ${SIMANDRECDIR}/init4600.py"
set SimXYZ="python ${SIMANDRECDIR}/initXYZ.py"
set SimPPLL="python ${SIMANDRECDIR}/initPPLL.py"
set SimPsi2S="python ${SIMANDRECDIR}/initPsi2S.py"
