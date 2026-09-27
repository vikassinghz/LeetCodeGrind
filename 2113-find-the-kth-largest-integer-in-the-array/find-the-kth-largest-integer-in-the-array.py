class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:

        # nums.sort(key = int, reverse = True)

        # return nums[k - 1]        

        #OPTIMAL APPROACH

        heap = []

        for x in nums:
            heapq.heappush(heap, int(x))

            if len(heap) > k:
                heapq.heappop(heap)

        return (str(heap[0]))
