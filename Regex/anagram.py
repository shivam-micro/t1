def anagram(str1,str2):
     if sorted(str1.lower()) == sorted(str2.lower()):
         print("Both are anagrams of each other")
     else:
         print("They are not !!")

anagram("naman", "manan")