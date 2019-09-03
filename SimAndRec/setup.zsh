SIMANDRECDIR="$(realpath "$( dirname "$0" )")";

echo "NUMFILE='$SIMANDRECDIR/.NUM'" > $SIMANDRECDIR/NUM.py
alias Sim3770="python ${SIMANDRECDIR}/init3770.py"
alias SimNewJpsi="python ${SIMANDRECDIR}/initNewJpsi.py"
alias SimJpsi="python ${SIMANDRECDIR}/initJpsi.py"
alias Sim4600="python ${SIMANDRECDIR}/init4600.py"
alias SimXYZ="python ${SIMANDRECDIR}/initXYZ.py"
alias SimPPLL="python ${SIMANDRECDIR}/initPPLL.py"
alias SimPsi2S="python ${SIMANDRECDIR}/initPsi2S.py"
