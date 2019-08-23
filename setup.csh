#得到当前脚本的绝对路径
set called=($_) 
if("$called" != " ") then 
	set BasketAnaTool_dir=`readlink -f $called[2]` 
else 
	set BasketAnaTool_dir=`readlink -f $0` 
endif 

setenv BaskDIR `dirname $BasketAnaTool_dir`

setenv PYTHONPATH ${BaskDIR}:$PYTHONPATH

source ${BaskDIR}/SimAndRec/setup.csh
source ${BaskDIR}/short/setup.csh
