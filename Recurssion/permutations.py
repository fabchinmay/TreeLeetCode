def findPermutations(p,up):
    if not up:
        print(p)
        return
    ch = up[0]
    i=0
    # for i in range(len(p)+1):
    #     f = up[0:i]
    #     s = up[i:len(p)]
    #     findPermutations(f+ch+s,up[1:])
    while i<=len(p):
        f = p[0:i]
        s = p[i:len(p)]
        findPermutations(f+ch+s,up[1:])
        i+=1

def permutations(p, up):
    if not up:
        print(p)
        return
    ch = up[0]
    i = 0
    while i <= len(p):
        f = p[0:i]
        s = p[i:len(p)]
        permutations(f + ch + s, up[1:])
        i += 1

def permutationsList(p, up):
    if not up:
        list = []
        list.append(p)
        return list
    ch = up[0]

    # local to this call
    ans = []

    i = 0
    #print(len(p),'-',p,'-',ch)
    while i <= len(p):
        f = p[0:i]
        s = p[i:len(p)]
        ans.extend(permutationsList(f + ch + s, up[1:]))
        #print(ans)
        i += 1
    return ans


st= "abc"

#findPermutations("",st)

print(permutationsList("",st))

#permutations("",st)

