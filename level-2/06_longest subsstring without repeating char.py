class Solution(object):
     def lengthOfLongestSubstring(self, string):
        my_dict={}
        left=0
        right = 0
        maxi=0
        n = len(string)

        while right <n:
            if string[right]  in my_dict:
                left = max(left, my_dict[string[right]] + 1)
            my_dict[string[right]] = right
            maxi = max(maxi, right-left + 1)
            right += 1
        return maxi    
obj = Solution()

print(obj.lengthOfLongestSubstring("abcabcbb"))
print(obj.lengthOfLongestSubstring("bbbbb"))
print(obj.lengthOfLongestSubstring("pwwkew"))
print(obj.lengthOfLongestSubstring("")) 