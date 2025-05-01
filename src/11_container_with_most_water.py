class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Height is limited by the shorter line
            h = min(height[left], height[right])
            # Width is the distance between pointers
            w = right - left
            # Compute current area
            area = h * w
            # Update maximum if needed
            if area > max_area:
                max_area = area

            # Move the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
