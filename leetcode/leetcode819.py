import re
from collections import defaultdict
from operator import itemgetter

class Solution:
    def mostCommonWorld(self, paragraph:str, banned:list[str])->str:
        
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        for word in words:
            if word not in banned_words:
                word_count[word] +=1 

        return max(word_count.items(), key=itemgetter(1))[0]