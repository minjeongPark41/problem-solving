# import re

# def isPalindrome(self, s:str) -> bool:
#     s = s.lower()
#     s = re.sub('[^a-z0-9]', '', s)

#     return s == s[::-1]


# from collections import deque

# def isPalindrome(self, s:str) -> bool:
#     strs:Deque = collections.deque()

#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())

#     while len(strs)>1:
#         if strs.pop(0) != strs.pop():
#             return False

#     return True


# def isPalindrome(self, s:str) -> bool:
    # strs=[]
    # for char in s:
    #     if char.isalnum():
    #         strs.append(char.lower())

    # while len(strs)>1:
    #     if strs.pop(0) != strs.pop():
    #         return False

    # return True




# 3번째
def isPalindrome(self, s):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if(strs.pop(0) != strs.pop()):
            return False
    return True
    
    
        
"""_
주의사항
- 함수 안에서만 return 사용 가능
- isalnum()
- lower()
- pop() 
"""
    
