class SuperStr(str):
    def is_repeatance(self, string):
        if not string:
            return False
        repititions = len(self) // len(string)
        return self == string * repititions

    def is_palindrome(self):
        cleaned_str = ''.join(char.lower() for char in self if char.isalnum())
        return cleaned_str == cleaned_str[::-1]


string = SuperStr("abab")
print(string.is_repeatance("ab"))  # Вернет True , так как "ababab" может
# быть получена повторением "ab"
print(string.is_repeatance("abc"))  # Вернет False


string = SuperStr("A man, a plan, a canal, Panama,")
print(string.is_palindrome())  # Вернет True , так как строка палиндром
