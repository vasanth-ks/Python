''' Program to return all combinations of strings that could be formed 
    from numbers in a keypad '''

import string
num_letter = {2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}
letters = ''
numbers = 234567

num_list = []
###########################################################################################
#                       Input must be a number greater than 1                             #
###########################################################################################

assert (type(numbers) == int), "Cannot accept string"
assert (numbers > 1), "Input must be greater than 1"

####################################################################################################
# Function to convert a string into a dictionary containing the characters present in the string   #
#                      and the number of occurences of that character                              #
####################################################################################################
def strToDict(string):
    string_dict = {}
    for s in string:
        count = string_dict.get(s, 0)
        count += 1
        dict1 = {s : count}
        string_dict.update(dict1)
    return string_dict

####################################################################################################
#       Function to determine all possible combinations of a given string from a list of words     #
####################################################################################################
def wordMatches():
    ref_d = strToDict(letters)
    ref_keys = ref_d.keys()
    ref_copy = ref_d.copy()
    result = []

    for words in wordlist:
        ref_copy = ref_d.copy()
        words = words.lower()
        flag = True
        comp_d = strToDict(words)
        comp_keys = comp_d.keys()
        for c_keys in comp_keys:
            if c_keys in ref_keys: 
                ref_count = ref_copy.get(c_keys, 0)
                comp_count = comp_d.get(c_keys, 0)
                if(ref_count >= comp_count and ref_count > 0 ):
                    flag &= True
                    ref_count -= 1
                    ref_copy[c_keys] = ref_count
                else:
                    flag &= False
            else:
                flag &= False           
        if flag == True:
            result.append(words)      
    return result

####################################################################################################
#                 Function to form a string from the input number                                #
####################################################################################################        
def numberToChar(numbers): 
    letters = ''
    while(numbers > 0):
        n = (int)(numbers % 10)
        num_list.append(n)
        numbers = numbers / 10
    for num in num_list:
        letters = letters + num_letter.get(num, None)
    return letters


with open("E:/Academics/Programming_languages/Python/Python edx/words.txt", "r", 0) as fp:
    wordlist = fp.read().splitlines()
print str(len(wordlist)) + " words loaded"
fp.close()
letters = numberToChar(numbers)
matches = wordMatches()
print matches
print (str(len(matches)) + " matches found for " + "\"" + letters + "\"")
