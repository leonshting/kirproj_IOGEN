

def fill_string(m,n):
    a = []
    if m==0:
        for i in range(0, n):
            a.append("-")
    else:
        a.append("|")
        for i in range(1, n):
            a.append("")
    return a

def fill_string2(m,n,pen):
    a = []
    if m==0:
        for i in range(0, n):
            a.append(str(i*pen))
    else:
        a.append(str(m*pen))
        for i in range(1, n):
            a.append("")
    return a

def init_path_mtx(m,n):
    b = [fill_string(i,n) for i in range(0,m)]
    return b

def init_score_mtx(m,n,pen):
    b = [fill_string2(i,n,pen) for i in range(0,m)]
    return b

def print_mtx(b):
    for i in range (len(b)):
        tmp = ""
        for j in range (len(b[i])):
            tmp += b[i][j] + "\t"
        print tmp + "\n"

print_mtx(init_path_mtx(4,4))
print_mtx(init_score_mtx(4,4,-6))