
def filter_function(lambda1,array):
    s = lambda1(array)
    return s
def lambda1(array):
 for s in array :
    if " "in s :
       array.remove(s)     
 for s in array:
    if s[0]=='a' :
       array.remove(s)     
 for s in array :
    if len(s)<5 :
       array.remove(s)     
 for s in array:
    if s[0]=='a' :
       array.remove(s)  
 return array
s = ["as7","dsbjccnj","abxx","sdjj vdsdj","svnksjvkjsvjksv","134234","qnn","abdhfuishdfi","a123","aeniwefnwuin"]
print(filter_function(lambda1,s))