class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for st in strs:
            counter = [0]*26
            for ch in st:
                counter[ord(ch) - ord('a')] += 1
            counter_str = tuple(counter)
            if counter_str in anagrams_dict:
                anagrams_dict[counter_str].append(st)
            else:
                anagrams_dict[counter_str] = [st]
        return list(anagrams_dict.values())
        