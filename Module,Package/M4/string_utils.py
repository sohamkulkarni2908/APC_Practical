def vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count

def reverse(s):
    return s[::-1]

def palindrome(s):
    return s == s[::-1]

def words(s):
    return len(s.split())

def remove_spaces(s):
    return s.replace(" ", "")