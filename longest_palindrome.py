def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(longest):
                longest = s[i:j]
    return longest

input_str = "babad"
longest_palin = longest_palindrome(input_str)
print(longest_palin)
