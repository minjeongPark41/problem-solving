import collections

# def groupAnagrams(self, strs):
#     anagrams = collections.defaultdict(list) # 디폴트값을 list로 줌

#     for word in strs:
#         # 정렬하여 딕셔너리에 추가
#         anagrams[''.join(sorted(word))].append(word)

#     return list(anagrams.values())

# defaultdict 설명 참고 : https://scribblinganything.tistory.com/12

# 다시
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()