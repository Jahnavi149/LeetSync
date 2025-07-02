class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for x in nums:
            if x in nums_dict:
                nums_dict[x] += 1
            else:
                nums_dict[x] = 1
        min_heap = []
        for num in nums_dict:
            heappush(min_heap, (nums_dict[num], num))
            if len(min_heap) > k:
                heappop(min_heap)
        freq_ele = []
        for tup in min_heap:
            freq, ele = tup
            freq_ele.append(ele)
        return freq_ele

        
        