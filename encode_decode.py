from roman import roman
import string
alphabetic = string.ascii_lowercase

word = input("enter word:")
result = ''
for ch in word:
    for i in range(len(alphabetic)):
        if ch == alphabetic[i]:
            result += f"{roman(i+1)} "
            break
print(result)

enter = input("enter word(space after any NUMBER):")
enter = enter.upper()
decode = enter.split()
print(decode)
result = ''
for ch in decode:
    for i in range(1,len(alphabetic)+1):
        if ch == roman(i):
            result += f"{alphabetic[i-1]}"
print(result)
