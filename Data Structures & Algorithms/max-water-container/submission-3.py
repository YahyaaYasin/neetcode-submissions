class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_index = 0
        right_index = len(heights)-1

        final = 0

        while left_index < right_index:

            h = min(heights[left_index], heights[right_index])
            w = right_index - left_index

            curr_area = h * w

            if curr_area > final:
                final = curr_area 

            if heights[left_index] < heights[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return final
