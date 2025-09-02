class Solution:
    def isPalindrome(self, s: str) -> bool:
        # turn lowercase
        s = s.lower()

        # remove all the nonalphanumeric characters
        clean_word = ""

        for ch in s:
            if ch.isalnum():
                clean_word += ch
        '''
        # use 2 pointer
        i = 0
        j = len(clean_word) - 1

        while i <= j:
            if clean_word[i] != clean_word[j]:
                return False
            i += 1
            j -= 1

        return True
                '''

        return clean_word ==  ''.join(reversed(clean_word))
 
