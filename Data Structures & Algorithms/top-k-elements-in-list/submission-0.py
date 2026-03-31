class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        result = [];
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse = True)
        
        for i in sorted_dict:
            k -=1 
            result.append(i[0])
            if k <= 0:
                break
        return result