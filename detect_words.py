# this program takes a string and count how many times a word occurs

str = 'it appears that the the appears the most in the sentence'
dict = {}
list = str.split(" ")
for word in list:
    if word in dict:
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1   # here we create a dictionary with the word as the key
                         # and the number of repeats as a value

for key, value in dict.items():
    print(f"\'{key}\' appears {value} time(s) in the string")
