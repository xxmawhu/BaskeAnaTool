SHORTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/scratchfs/bes/sunhk/6.6.4.p01/libssl/usr/lib
alias Hepsub='python2 ${SHORTDIR}/hepsubnew.py'
alias Heprm='python2 ${SHORTDIR}/Heprm.py'
alias Hep_q='python2 ${SHORTDIR}/Hep_q.py'
alias CheckBossJob='python2 ${SHORTDIR}/error.py'
alias CheckThenSub='python2 ${SHORTDIR}/hepsuberror.py'
alias Error='python2 ${SHORTDIR}/error.py'
alias SubError='python2 ${SHORTDIR}/hepsuberror.py'
alias Unrun='python2 ${SHORTDIR}/unrun.py'
alias Runnow='python2 ${SHORTDIR}/runnow.py'
