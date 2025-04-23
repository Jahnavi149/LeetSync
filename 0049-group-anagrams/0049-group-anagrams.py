class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for x in strs:
            counter = [0]*26
            for char in x:
                counter[ord(char) - ord('a')] += 1
            str_counter = str(counter)
            print(str_counter)
            if str_counter in anagram_dict:
                anagram_dict[str_counter].append(x)
            else:
                anagram_dict[str_counter] = [x]
        result = []
        for key in anagram_dict:
            result.append(anagram_dict[key])
        return result



        