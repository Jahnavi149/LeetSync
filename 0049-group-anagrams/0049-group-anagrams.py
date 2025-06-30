class Solution:
    def Counter(self, s: str):
        char_dict = {}
        for i in range(26):
            char_dict[chr(ord('a') + i)] = 0
        for ch in s:
            char_dict[ch] += 1
        return char_dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for x in strs:
            x_dict = self.Counter(x)
            x_dict_str = str(x_dict)
            if x_dict_str in anagrams_dict:
                anagrams_dict[x_dict_str].append(x)
            else:
                anagrams_dict[x_dict_str] = [x]
        output = []
        for counter_str in anagrams_dict:
            output.append(anagrams_dict[counter_str])
        return list(anagrams_dict.values())