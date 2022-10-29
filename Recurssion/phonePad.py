def permutationPad(digits):
    if len(digits)==1:
        print(digits)
        return
    pad("",digits)


def pad(p,up):

    if not up:
        print(p)
        return

    digit = int(up[0])
    i= (digit-1)*3
    #print(i)
    while i<digit*3:
        #ch = chr(ord('a'+i))
        ch = chr(ord('a') + i)
        pad(p+ch,up[1:])
        i+=1


class Solution:
    def letterCombinations(self, digits: str):
        digits = "12"
        return self.pad("", digits)

    def pad(self, p, up):

        if not up:
            lst = []
            # print(p)
            lst.append(p)
            return lst

        digit = int(up[0])  # - '0' # this will convert '2' into 2
        i = (digit - 1) * 3
        ans = []
        while i < digit * 3:
            ch = chr(ord('a') + i)
            # ch = chr(('a' + i))
            # print(ch,'-',p)
            ans.extend(self.pad(p + ch, up[1:]))
            i += 1

        return ans


permutationPad("12")

def padcheck(p,up):
    if not up :
        lst =[]
        lst.append(p)
        return lst

    digit = int(up[0])
    i = (digit-1)*3
    ans = []
    while i<digit*3:
        ch = chr(ord('a')+i)
        ans.extend(padcheck(p+ch,up[1:]))
        i+=1

    return ans