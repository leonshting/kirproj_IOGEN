from pyfasta import Fasta
import sys

def fill_string(m,n,pen):
    a = []
    if m==0:
        for i in range(0, n):
            a.append((i*pen))
    else:
        a.append((m*pen))
        for i in range (1, n):
            a.append(0)
    return a

def nw_step(init_value, dx, dy, match, mismatch, gp, row1, row2, num1, num2):
    if (dx == 1 and dy == 1 ):
        return init_value + [match, mismatch][row1[num2+dy-1] != row2[num1+dx-1]]
    if (dx == 0 or dy == 0):
        return  init_value + gp

def fill_angle(match, mismatch, gp, a, num, row1, row2):
    for i in range(num, len(row1)):
        b = [nw_step(a[num-1][i],0,1,match,mismatch,gp,row1,row2,num-1,i),nw_step(a[num-1][i-1],1,1,match,mismatch,gp,row1,row2,num-1,i-1),nw_step(a[num][i-1],1,0,match,mismatch,gp,row1,row2,num,i-1)]
        a[num][i] = (max(b))
    for i in range(num, len(row2)):
        b = [nw_step(a[i-1][num],0,1,match,mismatch,gp,row1,row2,i-1,num),nw_step(a[i-1][num-1],1,1,match,mismatch,gp,row1,row2,i-1,num-1),nw_step(a[i][num-1],1,0,match,mismatch,gp,row1,row2,i,num-1)]
        a[i][num] = (max(b))


def init_score_mtx(m,n,pen):
    b = [fill_string(i,n,pen) for i in range(0,m)]
    return b

def print_mtx(b):
    for i in range (len(b)):
        tmp = ""
        for j in range (len(b[i])):
            tmp += str(b[i][j]) + "\t"
        print tmp + "\n"

def build_nw_mtx(match, mismatch, gp, row1, row2):
    len1 = len(row1)
    len2 = len(row2)
    a = init_score_mtx(len2, len1, gp)
    for i in range(1, min(len1, len2)):
        fill_angle(match, mismatch, gp, a, i, row1, row2)
    return a

def traceback(a, x1, x2, match, mismatch, gp, row1, row2):
    retval = []
    if(nw_step(a[x1-1][x2],0,1,match,mismatch,gp,row1,row2,x1-1,x2) == a[x1][x2]):
        retval = [0,1]
    elif(nw_step(a[x1][x2-1],1,0,match,mismatch,gp,row1,row2,x1,x2-1) == a[x1][x2]):
        retval = [1, 0]
    elif(nw_step(a[x1-1][x2-1],1,1,match,mismatch,gp,row1,row2,x1-1,x2-1) == a[x1][x2]):
        retval = [1, 1]
    return retval

f = Fasta(sys.argv[1])
g = Fasta(sys.argv[2])
nw = build_nw_mtx(4,-5,-2,f.values()[0],g.values()[0])
x = len(f.values()[0])-1
y = len(g.values()[0])-1
str1 = ""
str2 = ""
print_mtx(nw)
while x!=0 or y!=0:
    tmpl = traceback(nw, y, x, 4, -5, -2, f.values()[0],g.values()[0])
    if tmpl[0]==1 and tmpl[1]==1:
        str1 = f.values()[0][x-1] + str1
        str2 = g.values()[0][y-1] + str2
    elif tmpl[0]==0 and tmpl[1]==1:
        str1 = "-" + str1
        str2 = g.values()[0][y-1] + str2
    else:
        str1 = f.values()[0][x-1] + str1
        str2 = "-" + str2
    x -= tmpl[0]
    y -= tmpl[1]
    if(x==1 or y ==1 ):
        print "aaaaa"


print str1
print str2