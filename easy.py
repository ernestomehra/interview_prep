Question 1:
""" Find the index of the element in an array whose left and right sums are equal. """

def find_mid(arr):
  for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i+1:]):
      return i 
      
      
Question 2: 
""" The string should be compressed such that the consecutive duplicates of characters are replaced with a single character. 
Example , for "aaabbccdee", the compressed string will be "abcde" """

def compress_string(s):
  interim_s = list(set(s))
  return ''.join(sorted(interim_s))
  

Question 3: 
""" Check if two strings are anagrams or not? """

def validate_anagram(s1, s2):
  d1, d2 = {}, {}
  for char in s1:
    if char not in d1.keys():
      d1[char] = 1
    else:
      d1[char] += 1

  for char in s2:
    if char not in d2.keys():
      d2[char] = 1
    else:
      d2[char] += 1
  
  if d1 == d2:
    return True
  else: 
    return False
    
 
