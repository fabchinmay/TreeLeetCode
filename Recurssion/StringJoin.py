def stJoin(strJn,start):
    if start==len(strJn):
        return ""
    if strJn[start]=='a':
        return stJoin(strJn,start+1)
    else:
        return strJn[start]+stJoin(strJn,start+1)

def skipApple(AppStr,start):
    if start==len(AppStr):
        return ""

    # print(start,"-",AppStr[start:])

    if AppStr.startswith("apple",start):
        # print("Here")
        return skipApple(AppStr,start+5)
    else:
        return AppStr[start]+skipApple(AppStr,start+1)

AppStr="bcdappleefg"

print(skipApple(AppStr,0))


print(stJoin("baccad",0))
