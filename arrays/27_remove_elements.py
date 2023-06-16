# https://leetcode.com/problems/remove-element/

class RemoveElements:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        buffer = list()
        for e in nums:
            if e != val:
                buffer.append(e)

        for p, e in enumerate(buffer):
            nums[p] = e

        return len(buffer)
 