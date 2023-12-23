class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # We are using a two pointer technique. Make three auxilary pointers, 
        # i : end of non-zero elements of the first array
        # j : end of non-zero elements of the second array
        # k : end of first array's inplace elements
        
        i, j, k = m-1, n-1, m+n-1
        
        
        # Swap on the basis of comparison

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        