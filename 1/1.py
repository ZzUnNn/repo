def F(s):
 s = s.replace(" ","").lower()
 s2 = s[::-1]
 if(s == s2):
   return True
 else:
   return False
print(F(s = "12321"))
 