IMM = []
def combine(m, n):
    a = len(m)
    cc = ''
    count = 0
    for i in range(a):
        if(m[i] == n[i]):
            cc += m[i]
        elif(m[i] != n[i]):
            cc += '_'
            count += 1

    if(count > 1):
        return None
    else:
        return cc


def find_prime_implicants(data, IMM):
    while (True):
        newList = list(data)
        size = len(newList)
        IM = []
        im = []
        im2 = []
        mark = [0]*size
        m = 0
        for i in range(size):
            for j in range(i+1, size):
                c = combine(str(newList[i]), str(newList[j]) )
                if c != None:
                    im.append(str(c))
                    mark[i] = 1
                    mark[j] = 1
                else:
                    continue

        mark2 = [0]*len(im)
        for p in range(len(im)):
            for n in range(p+1, len(im)):
                if( p != n and mark2[n] == 0):
                    if( im[p] == im[n]):
                        mark2[n] = 1


        for r in range(len(im)):
            if(mark2[r] == 0):
                im2.append(im[r])

        for q in range(size):
            if( mark[q] == 0 ):
                IM.append( str(newList[q]) )
                m = m+1
        data = im2
        IMM+=IM
        if (m == size or size == 1):
            break;
    return IMM


minterms = set(['0000', '0001', '0010', '0011', '0110', '0111', '1000', '1001', '1011', '1111'])

print('PI(s):', find_prime_implicants(minterms, IMM))