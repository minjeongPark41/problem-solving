import collections

def groupAnagrams(self, strs):
    anagrams = collections.defaultdict(list) # 디폴트값을 list로 줌

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())