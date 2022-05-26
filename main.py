# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


    
def find_anagrams(strings1, string2):
    
    stings1 = ("hello")
    string2 = ("racecar")

    # check if the length is same
    if (len(strings1)) == (len(string2)):
        #sort the strings
        sorted_string1 = sorted(strings1)
        sorted_string2 = sorted(strings2)

        if(sorted_string1 == sorted_string2):
            return True
    else:
        return False
print(find_anagrams("hello","racecar"))
