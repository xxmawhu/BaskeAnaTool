#export PATH=/afs/ihep.ac.cn/soft/common/python27_sl65/bin:$PATH
BaskDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=${BaskDIR}:$PYTHONPATH
source /besfs/users/lihb/software/SL6/python-2.7.16/thispython.sh
source ${BaskDIR}/short/setup.sh
source ${BaskDIR}/SimAndRec/setup.sh

#use this python
source /workfs/bes/maxx/local/python-2.7.14/setup.sh
if [ -f ${BaskDIR}/bin/hep_sub  ] ;
then
    /bin/rm -f ${BaskDIR}/bin/hep_sub
fi
ln -s  ${BaskDIR}/short/hepsubnew.py ${BaskDIR}/bin/hep_sub
export PATH=$PATH:${BaskDIR}/bin
