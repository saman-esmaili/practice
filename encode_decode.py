from roman import roman
import string
alphabetic = string.ascii_lowercase

# word = input("enter word:")
# result = ''
# for ch in word:
#     for i in range(len(alphabetic)):
#         if ch == alphabetic[i]:
#             result += f"{roman(i+1)} "
#             break
# print(result)
#
# enter = input("enter word(space after any NUMBER):")
# enter = enter.upper()
# decode = enter.split()
# print(decode)
# result = ''
# for ch in decode:
#     for i in range(1,len(alphabetic)+1):
#         if ch == roman(i):
#             result += f"{alphabetic[i-1]}"
# print(result)

# word = "beez"
# result = ''
# for ch in word:
#     for i in range(len(alphabetic)):
#         if ch == alphabetic[i]:
#             val = len(alphabetic) - i
#             result += str(val)
# print(result)
#
# num = "24 21 21 0"
# decode = num.split()
#
# for n in decode:
#     for i in range(len(alphabetic)):
#         if n == f"{i}":
#             val = len(alphabetic)-1-i
#             print(alphabetic[val])
#             break