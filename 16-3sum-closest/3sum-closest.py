class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        # Initialize with the first three numbers
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                # Update closest sum if current is nearer to target
                if abs(current - target) < abs(closest - target):
                    closest = current

                # Move pointers
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    # Exact match found
                    return current

        return closest