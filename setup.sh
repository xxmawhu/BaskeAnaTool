export PATH=/afs/ihep.ac.cn/soft/common/python27_sl65/bin:$PATH
BaskDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=${BaskDIR}:$PYTHONPATH
source ${BaskDIR}/cpplint/setup.sh
source ${BaskDIR}/short/setup.sh
source ${BaskDIR}/SimAndRec/setup.sh
