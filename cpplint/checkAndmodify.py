import cpplint
import sys
import codecs
from commands import getoutput
import time
def Process(errlog):
    errNum = 0
    for line in errlog.split('\n')[::-1]:
        if 'Missing space after ,' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            command = '%d, %ds/,/, /g'%(linenum, linenum)
            getoutput('sed -i "%s" '%(command) + filename)
            errNum += 1

        elif 'Missing spaces around' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            ll = line.split()
            indx = ll.index("around")
            oper = ll[indx + 1]
            command = '%d, %ds/%s/ %s /g'%(linenum, linenum, oper, oper)
            getoutput('sed -i "%s" '%(command) + filename)
            errNum += 1

        elif 'Line ends in whitespace' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            command = 's/[ \t]*$//g'
            getoutput('sed -i "%s" '%(command) + filename)
            errNum += 1

        elif "No copyright" in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            copyright = "// Copyright (c) %d-%d-%d "%(time.localtime()[0:3])
            copyright += getoutput('echo $USER')
            command = "sed '1 i%s'"%(copyright)
            command += ' -i '+filename
            #print command
            getoutput(command)
            errNum += 1

        elif 'Should have a space between // and comment' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            command = r'%d, %ds/\/\//\/\/ /g'%(linenum, linenum)
            #print command
            getoutput('sed -i "%s" '%(command) + filename)
            errNum += 1

        elif 'Extra space before last semicolon.' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            command = r'%d, %ds/ ;/;/g'%(linenum, linenum)
            #print command
            getoutput('sed -i "%s" '%(command) + filename)
            errNum += 1

        elif 'Missing space before' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            ll = line.split()
            indx = ll.index("before")
            oper = ll[indx + 1]
            command = '%d, %ds/%s/ %s/g'%(linenum, linenum, oper, oper)
            #print command
            getoutput('sed -i "%s" '%(command) + filename)
            errNum += 1

        elif '{ should almost always be at the end' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            ll = line.split()
            #indx = ll.index("before")
            #oper = ll[indx + 1]
            command1 = '%d, %ds/$/ {/g'%(linenum-1, linenum-1)
            command2 = '%d, %ds/{/ /g'%(linenum, linenum)
            #print command1
            #print command2
            getoutput('sed -i "%s" '%(command1) + filename)
            getoutput('sed -i "%s" '%(command2) + filename)
            errNum += 1

        elif 'Redundant blank line' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            command1 = '%dd'%(linenum)
            #print command1
            getoutput('sed -i "%s" '%(command1) + filename)
            errNum += 1

        elif 'should be moved to the previous line' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            ll = line.split()
            indx = ll.index("should")
            oper = ll[indx - 1]
            #print "opera: ", oper
            command1 = '%d, %ds/$/ %s/g'%(linenum-1, linenum-1, oper)
            command2 = '%d, %ds/%s/ /g'%(linenum, linenum, oper)
            #print command1
            #print command2
            getoutput('sed -i "%s" '%(command1) + filename)
            getoutput('sed -i "%s" '%(command2) + filename)
            errNum += 1

        elif 'Line contains only semicolon' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            command1 = '%d, %ds/$/;/g'%(linenum-1, linenum-1)
            command2 = '%dd'%(linenum)
            # print command1
            # print command2
            getoutput('sed -i "%s" '%(command1) + filename)
            getoutput('sed -i "%s" '%(command2) + filename)
            errNum += 1

        elif 'Extra space before' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            ll = line.split()
            indx = ll.index("before")
            oper = ll[indx + 1]
            command = '%d, %ds/ %s/%s/g'%(linenum, linenum, oper, oper)
            getoutput('sed -i "%s" '%(command) + filename)
            errNum += 1

        elif 'Extra space after' in line:
            filename = line.split(':')[0]
            linenum = int(line.split(":")[1])
            ll = line.split()
            indx = ll.index("after")
            oper = ll[indx + 1]
            command = '%d, %ds/%s /%s/g'%(linenum, linenum, oper, oper)
            getoutput('sed -i "%s" '%(command) + filename)
            errNum += 1
    return errNum
    

def main():
    option=''
    for i in sys.argv[1:]:
        option += str(i)+' '
    while 1:
        errlog = getoutput("python cpplint.py "+option)
        errnum = Process(errlog)
        if errnum == 0:
            break
    print getoutput("python cpplint.py "+option)

if __name__ == '__main__':
    main()
