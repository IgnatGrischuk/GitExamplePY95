class SuperStr(str):
    def is_repeatance(self, string):
        if not string:
            return False
        repititions = len(self) // len(string)
        return self == string * repititions

    def is_palindrome(self):
        cleaned_str = ''.join(char.lower() for char in self)
        return cleaned_str == cleaned_str[::-1]


string = SuperStr("abab")

# Will return True as 'ababab' can be obtained by repeating 'ab'
print(string.is_repeatance("ab"))

# Will return False
print(string.is_repeatance("abc"))

# Will return True as the string is a palindrome
string = SuperStr("A man, a plan, a canal, Panama,")
print(string.is_palindrome())
