import os,filecmp,subprocess,sys,time

'''
1 - TLE
2 - RTE
3 - AC
4 - WA
'''

def run_prog(ipf_path,expopf_path,progf_path,errorf_path,opf_path,timelimit):
    if not os.path.exists('media/submission/output'):
        os.makedirs('media/submission/output')
    if not os.path.exists('media/submission/error'):
        os.makedirs('media/submission/error')

    file=progf_path
    tle=0
    fin=open(ipf_path,'r')
    fout=open(opf_path,'w')
    ferr=open(errorf_path,'w')
    try:
        timeStarted = time.time()
        program=subprocess.Popen(['python',file], bufsize=0, stdin=fin, stdout=fout,stderr=ferr)    
        program.wait(timeout=timelimit)
    except subprocess.TimeoutExpired:
        tle=1
    program.kill()
    run_time=time.time()-timeStarted
    fin.close()
    fout.close()
    ferr.close()
    if tle==1:
        return(["TLE",run_time])
        sys.exit()
    else:
        result=verdict(expopf_path,opf_path,errorf_path)
        return([result,run_time])


def compare(path_1,path_2): #preliminary judgement
    line1 = line2 = True
    with open(path_1, 'r') as f1, open(path_2, 'r') as f2:
        while line1 and line2:
            line1 = f1.readline()
            line2 = f2.readline()
            if line1 != line2:
                return False
    return True

def verdict(expopf_path,opf_path,errorf_path):
    if os.stat(errorf_path).st_size != 0:
        return("RTE")
    else:
        result=compare(expopf_path, opf_path)
        if result:
            return("AC")
        else:
            return("WA")