SIMANDRECDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SIMANDRECDIR ; python config.py ; 
alias Sim3770="python ${SIMANDRECDIR}/init3770.py"
alias SimNewJpsi="python ${SIMANDRECDIR}/initNewJpsi.py"
alias SimPsi2S="python ${SIMANDRECDIR}/initPsi2S.py"
alias SimJpsi="python ${SIMANDRECDIR}/initJpsi.py"
alias Sim4600="python ${SIMANDRECDIR}/init4600.py"
