class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        table = defaultdict(int)
        count = 0

        for a in nums1:
            for b in nums2:
                table[a + b] += 1

        for c in nums3:
            for d in nums4:
                count += table[-(c + d)]

        return count
