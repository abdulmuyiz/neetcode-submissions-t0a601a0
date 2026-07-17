class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.insert(0, beginWord)
        d = {}
        for word in wordList:
            d[word] = []

        for i in range(len(wordList)):
            for j in range(i,len(wordList)):
                check = 0
                for k in range(len(wordList[i])):
                    if wordList[i][k] != wordList[j][k]:
                        check+=1
                if check == 1:
                    d[wordList[i]].append(wordList[j])
                    d[wordList[j]].append(wordList[i])
        res = 0

        visit = set()
        q = deque()
        q.append([1,beginWord])

        while q:
            print(q)
            for i in range(len(q)):
                l,word = q.popleft()
                visit.add(word)
                if word == endWord:
                    res = l
                    q = []
                    break
                for w in d[word]:
                    if w not in visit:
                        q.append([l+1,w])

        return res
                    


        