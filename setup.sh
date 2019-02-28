BaskDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=${BaskDIR}:$PYTHONPATH
source ${BaskDIR}/cpplint/setup.sh
