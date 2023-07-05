#check is the number is palindrome
def is_palindrome(a):
    n = a
    i = 0
    while n != 0:
        n = n // 10
        i = i + 1
    n = a
    rev = 0
    while i != 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10
        i = i - 1
    if a == rev:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")