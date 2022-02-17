for i in range(len(s)):
    for j in range(len(s)):
        for x in range(len(s)):
            for y in range(len(s)):
                for k in range(len(s)):
                    for l in range(len(s)):
                        c = s[i]
                        d = s[j]
                        a = s[x]
                        b = s[y]
                        e = s[k]
                        f = s[l]
                        col1 = 1+c+10
                        col2 = 6+d+4
                        row1 = 1+a+b+6
                        row2 = 10+e+f+4
                        if(col1 == col2):
                            if(col1 == row1):
                                if(col1 == row2):
                                    if(c != d and c != a and c!=b and c != e and c!= f):
                                        if( d != a and d!= b and d != e and d != f):
                                            if(a != b and a!=e and a!=f):
                                                if(b!=e and b!=f):
                                                    if(e!=f):
                                                        print(c,d,a,b,e,f)
                            
