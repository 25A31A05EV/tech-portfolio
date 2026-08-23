"""
LeetCode 49: Group Anagrams
Pattern: HashMap

Given an array of strings, group the anagrams together.
Anagrams are words made of the same letters in a different order.
"""

def groupAnagrams(strs):
    groups = {}  # key: sorted_word, value: list of original words

    for word in strs:
        key = ''.join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return list(groups.values())


# Test cases
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat','tea','ate'], ['tan','nat'], ['bat']]

print(groupAnagrams([""]))
# Output: [['']]

print(groupAnagrams(["a"]))
# Output: [['a']]