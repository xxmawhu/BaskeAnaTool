from Bes import subjobs
j = subjobs.subjobs()
options = "OPTINS"
j.setbody(options)
dirList = ["/bes3fs/offline/data/664p03/psip/09mc/dst",
           "/bes3fs/offline/data/664p03/psip/12mc/dst"]
j.setjobnum(100)
j.setjobname("jobs_")
j.setInputDstDir(dirList[0])
j.setjobpath("test")
j.setrootpath("the_root_path")
j.jobs()
