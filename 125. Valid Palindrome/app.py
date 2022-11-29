class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Input: a string
        Return: Boolean

        Filter:
        1. Convert all upper case to lower case
        2. remove all non alphabetic characters

        Palindrome Conditions:
        - Reads the same forwards and backwards

        """

        s = s.lower()  # convert all to lower case

        # if its [a-z] we combine it using the join
        word = "".join(ch for ch in s if ch.isalnum())
        reversed_word = list(word)
        reversed_word.reverse()
        reversed_word = "".join(reversed_word)
        if word == reversed_word:
            return True

        return False


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    assert (Solution().isPalindrome(s)) == True

    s = "race a car"
    assert (Solution().isPalindrome(s)) == False

    # note Solution() -> is initializing it
