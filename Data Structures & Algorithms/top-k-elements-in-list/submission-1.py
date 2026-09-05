class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        freq_hash=defaultdict(int)

        for n in nums:
            freq_hash[n]+=1

        freq_list = []
        for i,v in freq_hash.items():
            freq_list.append([v,i])
        
        freq_list.sort(reverse=True)

        res =[]
        for f, n in freq_list:
            res.append(n)
            if len(res)==k:
                break
        return res
        
        