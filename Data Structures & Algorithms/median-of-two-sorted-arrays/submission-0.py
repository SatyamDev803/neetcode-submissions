class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left_size = (m + n + 1) // 2

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            j = left_size - i

            nums1_left = -math.inf if i == 0 else nums1[i-1]
            nums1_right = math.inf if i == m else nums1[i]

            nums2_left = -math.inf if j == 0 else nums2[j-1]
            nums2_right = math.inf if j == n else nums2[j]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    left_max = max(nums1_left, nums2_left)
                    right_min = min(nums1_right, nums2_right)

                    return (left_max + right_min) / 2
                
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1