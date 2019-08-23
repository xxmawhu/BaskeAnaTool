#得到当前脚本的绝对路径
set called=($_) 
if("$called" != " ") then 
	set BasketAnaTool_dir=`readlink -f $called[2]` 
else 
	set BasketAnaTool_dir=`readlink -f $0` 
endif 

setenv BaskDIR `dirname $BasketAnaTool_dir`

setenv PYTHONPATH ${BaskDIR}:$PYTHONPATH
#source ${BaskDIR}/cpplint/setup.sh

cd ${BaskDIR}/SimAndRec && source setup.csh && cd -
cd ${BaskDIR}/short/ && source setup.csh && cd -
