class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for x in strs:
            counter = [0]*26
            for char in x:
                counter[ord(char) - ord('a')] += 1
            if tuple(counter) in anagram_dict:
                anagram_dict[tuple(counter)].append(x)
            else:
                anagram_dict[tuple(counter)] = [x]
        return list(anagram_dict.values())



        