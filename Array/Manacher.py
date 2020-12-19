def manachersAlgorithm(s,N):
    str = getModifiedString(s, N)
    len = (2 * N) + 1
    P = [0] * len
    c = 0; #stores the center of the longest palindromic substring until now
    r = 0; #stores the right boundary of the longest palindromic substring until now
    maxLen = 0;
    for i in range(len):
        #get mirror index of i
        mirror = (2 * c) - i;
        
        #see if the mirror of i is expanding beyond the left boundary of current longest palindrome at center c
        #if it is, then take r - i as P[i]
        #else take P[mirror] as P[i]
        if (i < r): 
            P[i] = min(r - i, P[mirror])
        
        #expand at i
        a = i + (1 + P[i]);
        b = i - (1 + P[i]);
        while (a < len and b >= 0 and str[a] == str[b]):
            P[i] += 1;
            a += 1;
            b -= 1;
        
        #check if the expanded palindrome at i is expanding beyond the right boundary of current longest palindrome at center c
        #if it is, the new center is i
        if (i + P[i] > r):
            c = i;
            r = i + P[i];
            
            if(P[i] > maxLen): #update maxlen
                maxLen = P[i];
    return maxLen;

def getModifiedString(s, N):
    news = ''
    for i in range(N):
        news += "#"
        news += s[i]
    news += '#'
    return news