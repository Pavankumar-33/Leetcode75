# 345. Reverse Vowels of a String
# Easy
# Topics
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = set("aeiouAEIOU")
    s = list(s)
    res = ""
    flag = []

    for i in range(len(s)):
        if s[i] not in vowels:
            i += 1
        else:
            flag.append(s[i])
            i += 1

    for i in range(len(s)):
        for j in range(len(flag)-1, 0):
            if s[i] not in vowels:
                res += s[i]
                i += 1
            else:
                res += flag[j]
                j -= 1

    return res

print(reverseVowels('hellow'))
print("done")