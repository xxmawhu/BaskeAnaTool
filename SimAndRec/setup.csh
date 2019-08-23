#得到当前脚本的绝对路径
set called=($_) 
if("$called" != " ") then 
	set script_dir=`readlink -f $called[2]` 
else 
	set script_dir=`readlink -f $0` 
endif 

setenv SIMANDRECDIR `dirname $script_dir`
echo "NUMFILE='$SIMANDRECDIR/.NUM'" > $SIMANDRECDIR/NUM.py
setenv SimPsi2S "python ${SIMANDRECDIR}/initPsi2S.py"
setenv Sim3770 "python ${SIMANDRECDIR}/init3770.py"
setenv SimNewJpsi "python ${SIMANDRECDIR}/initNewJpsi.py"
setenv SimJpsi "python ${SIMANDRECDIR}/initJpsi.py"
setenv Sim4600 "python ${SIMANDRECDIR}/init4600.py"
setenv SimXYZ "python ${SIMANDRECDIR}/initXYZ.py"
setenv SimPPLL "python ${SIMANDRECDIR}/initPPLL.py"
setenv SimPsi2S "python ${SIMANDRECDIR}/initPsi2S.py"
