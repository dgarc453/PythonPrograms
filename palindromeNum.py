def isPalindrome(x):
    """
        :type x: int
        :rtype: bool
        """
    strX = str(x)
    return strX == strX[::-1]


print(isPalindrome(12))
