s = input("Enter a String: ")
s.strip()
mid = int((len(s) // 2)-1)
for i in range(mid):
    if s[mid+i]==s[mid-i]:
      pal = True
    else:
       pal = False
       break

if pal == True:
   print("Given string is palindrome")
else:
   print("Not palindrome")