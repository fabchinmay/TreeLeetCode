def throwDice(p,target):
    if target==0:
        print(p)
        return
    i=1
    while i<=6 and i<=target:
        #print(i,'-',target,'-',p)
        throwDice(p+str(i),target-i)
        i+=1

throwDice("",4)

