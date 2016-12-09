# coding = UTF-8
#!/usr/bin/python
###############################
#Author:wangxin               #
#Date  :20161209              #
#Descri:Computational process #
#       efficiency from       #
#        process logs         #
###############################

from __future__ import division                 #import division module for floating point operation later                   
import re                                       #import re module for regular later in function count_eff
#import sys

def len_file(filename):                         #define len_file function to count number of lines of a file and return the number as an inter
    f = open(filename)                          #open file as an object
    lines = int(len(f.readlines()))             #changing type from string to inter
    f.close()                                   #close file to free memory
    return lines                                #return values
    

def int_str(str_val):                           #define int_str function to deal with changing element of a list from type string to inter after readlines()
    tmp_lis = []                                #define tmp_lis before using it 
    for x in str_val :                          #ergodic a list
        x = x.strip('=')                        #remove "="
        tmp_lis.append(int(x))                  #create a new list after changing element into inter
    return tmp_lis                              #return the list

def count_eff():                                #define count_eff function to compute the efficiency of bdssrv
    a = f.next()                                #start to read a single line of a log file and create an object for later compute
    pat_arq = re.compile('ARQ')                 #define pattern to deal with the line contains string "ARQ" 
    pat_aoq = re.compile('AOQ')                 #define pattern to deal with the line contains string "AOQ" 

    arq_eff = 0                                 #define variable before using it later
    aoq_eff = 0

    arq_sta = 0
    aoq_sta = 0
    lin_dat1 = re.findall(pat_arq,a)            #begin to match each line and return values as a list to lin_dat1 for lines contain "ARQ" 
    
    if lin_dat1 :
        num_dat1 = re.findall(r'=\d+',a)
        num_dat1 = int_str(num_dat1)
        arq_val = num_dat1[2]
        arq_sta = num_dat1[0]

        a= f.next()
        lin_dat2 = re.findall(pat_aoq,a)        #IF ARQ MATCHED ,begin to match each line and return values as a list to lin_dat1 for lines contain "AOQ" 
        if lin_dat2 :
            num_dat2 = re.findall(r'=\d+',a)
            num_dat2 = int_str(num_dat2)
            aoq_val = num_dat2[2]
            aoq_sta = num_dat2[0]
##[2016-12-08 00:47:47.321 <NOTICE>] : beginTime=20161208004643, endTime=20161208004747, totaltime=64, processed ARQ totalNum=15 avg time=21812    @<FUNC: AbmSrvInterface::ARQProcess()>
##[2016-12-08 00:48:34.680 <NOTICE>] : beginTime=20161208004731, endTime=20161208004834, totaltime=63, processed AOQ totalNum=13 avg time=6583    @<FUNC: AbmSrvInterface::AOQProcess()>

            tot_tme = aoq_val/2 + arq_val/2
            arq_eff = num_dat1[3]* num_dat1[4]/tot_tme/1000000
            aoq_eff = num_dat2[3]* num_dat2[4]/tot_tme/1000000
        
        return [arq_eff,aoq_eff,arq_sta,aoq_sta]

def main(filename):
    a = len_file(filename)
    for x in range(int(a/2)):
        rest = count_eff()
        if rest and (rest[0] != 0):
            print "ARQ :",rest[0],"\t","ARQ :",rest[1],"\t ARQ START TIME:",rest[2],"\t ARQ START TIME:",rest[3]
            
if __name__ == '__main__' :
#    filename =raw_input('Plz input file name:')
    filename = sys.argv[1]                      #asssign the first argment value to filename 
    f = open(filename)                          #open file as an object
    main(filename)                              #run main function
    
