#得到当前脚本的绝对路径
set called=($_) 
if("$called" != " ") then 
	set script_dir=`readlink -f $called[2]` 
else 
	set script_dir=`readlink -f $0` 
endif 

set BaskDIR=`dirname $script_dir`

setenv PYTHONPATH ${BaskDIR}:$PYTHONPATH
#source ${BaskDIR}/cpplint/setup.sh
source ${BaskDIR}/short/setup.csh
source ${BaskDIR}/SimAndRec/setup.csh
