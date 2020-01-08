#export PATH=/afs/ihep.ac.cn/soft/common/python27_sl65/bin:$PATH
# status="$(git pull)"
cwd="$(pwd)"
BaskDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=${BaskDIR}:$PYTHONPATH

# please use this python
# this python version work well
source /workfs/bes/maxx/local/python-2.7.14/setup.sh

source ${BaskDIR}/short/setup.sh
cd ${BaskDIR}/SimAndRec 
#which python
#alias python="/besfs/users/lihb/software/SL6/python-2.7.16/bin/python"
python addSimor.py
cd ${cwd}
source ${BaskDIR}/SimAndRec/setup.sh

