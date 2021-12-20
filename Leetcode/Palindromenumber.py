def isPalindrome(x: int) -> bool:
        x=str(x)
        return x[::]==x[::-1]

x=121
isPalindrome(x)