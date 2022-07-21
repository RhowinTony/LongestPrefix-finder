
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


def prefix_finder(str):
    lcp = ""
    i = 0
    while i < minlen:
        char = str_list[0][i]
        for j in range(1,len(str_list)):
            if str_list[j][i] != char:
                return lcp
        lcp = lcp + char
        i +=1
    return lcp


str = input("Enter the strings ")
str_list = str.split()
if len(str_list) == 0:
     print("None")
minlen = (len(str_list[0]))
for _ in range(len(str_list)):
    minlen = min(len(str_list[_]), minlen)
output = prefix_finder(str_list)
print(f"The longest common prefix is {output}")


