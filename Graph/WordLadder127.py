import collections
#https://www.youtube.com/watch?v=ZVJ3asMoZ18&ab_channel=TECHDOSE
#https://www.youtube.com/watch?v=h9iTnkgv05E&ab_channel=NeetCode
beginWord = "hit"
wordList = ["hot","dot","dog","lot","log","cog"]
endWord = "cog"
nei = collections.defaultdict(list)
dic = {}

wordList.append(beginWord)

for word in wordList:
    for j in range(len(word)):
        pattern = word[:j]+"*"+word[j+1:]
        nei[pattern].append(word)
        #dic[pattern]=[word]
        dic.setdefault(pattern, []).append(word)

print(nei)
print("\n")
print(dic)
"""
We will be using the BFS to find the shortest path because in graph we have exponential no of unique paths 
between two nodes we can use DFS in trees because each node has unique paths between nodes
"""

def findShortestPath(beginWord,endWord,wordList):
    if endWord not in wordList:
        return 0

    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j+1:]
            nei[pattern].append(word)

    print(nei)

    q = collections.deque([beginWord])
    visit = set([beginWord])
    res = 1

    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res

            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                for neiword in nei[pattern]:
                    if neiword not in visit:
                        visit.add(neiword)
                        q.append(neiword)
        res+=1

    return 0

print(findShortestPath(beginWord,endWord,wordList))

