zeroarr=lambda n:map(lambda a:0,range(0,n))

def choose(x):
    i=0
    while (x[i]==0) and (i<len(x)):
        i+=1
        if i<len(x):
            return i
        else:
            return -1

def Gauss_sol(A,b):
    
    # Check if matrix is square 
    # and if the ansver have same number of lines
    
    if (len(A) != len(A[0])) or (len(A) != len(b)):
        return None
    
    M = A[:]
    c = b[:]
    n = len(M)
    indices = zeroarr(n)
    
    for i in range(0,n):
        k = choose(M[i]);
    
        for j in filter(lambda a,b=i:a!=b,range(0,n)):
            c[j] -= float(c[i]) * float(M[j][k]) / float(M[i][k])
            M[j] = sub(M[j], mulbyn(M[i], float(M[j][k]) / float(M[i][k])))
            indices[i] = k    
            x = zeroarr(n)
    
    for i in range(0,n):
        x[i] = c[indices[i]]
    
    return x