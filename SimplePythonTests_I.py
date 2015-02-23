# Reverse string
def FirstReverse(str): 
  return ''.join(reversed(str))

# Factorial 
# example: num = 4 => answer = 4*3*2*1
def FirstFactorial(num): 
  if num <= 1:
    return 1
  return num * FirstFactorial(num-1)  

# find the longest word in a sentence
def LongestWord(sen):
  # code goes here
  symbols = ['!', '?', '&','(',')','$','@','#', '%','/',':',';','[',']','{','}','~' ]
  sen = ''.join([c for c in sen if c not in symbols])
  words = sen.split()
  longest = words[0]
  size = len(longest)
  for word in words:
    # keeps the first word if the size is same  
    if len(word) > size:
      size = len(word)
      longest = word

  return longest  

# letter changes
# algorithm steps:
# 1) a = b, b = c ... z = a 
# 2) make all vowels uppercase 
def LetterChanges(str): 
  # ascii tabel
  # A = 65		a = 97
  # Z = 90		z = 122
  alphabet = 'abcdefghijklmnopqrstuvwyxz'
  vowels = 'aeiou'
  newString = ''
  chars = list(str)
  for char in chars:
    if char in alphabet:
      # step 1)
      ascii = ord(char) + 1
      if ascii == 123:
        ascii = ascii - 26
      # step 2)
      if chr(ascii) in vowels:
        ascii = ascii - 32
      newString = newString + chr(ascii) 
    else: 
      newString = newString + char
  
  return newString

# add all numbers from 1 to given num
def SimpleAdding(num): 
  return (num * (num + 1)) / 2

# capitalize all first letters of each word in a string 
def LetterCapitalize(str): 
  # return srt.title() shows some incorrect test cases
  return ''.join([word[0].upper()+word[1:] for word in str.split()]) 

# check if any letter in a given string is surrounded by '+'
# examples:
# "=+d+u++=+d+=" returns true as a string
# "d+ff==+k+" returns false as a string
def SimpleSymbols(str): 
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  if str[0] in alphabet:
    return "false"
  if str[-1] in alphabet:
    return "false"
  for i in range(1, len(str)-1):
    if str[i] in alphabet:
      if str[i-1] != "+" or str[i+1] != "+":
        return "false"
    
  return "true"

# if num1 = num2 return -1, if num1 > num2 return false else true
def CheckNums(num1,num2): 
  return 'true' if num2 > num1 else 'false' if num1 > num2 else '-1'
    
# from given number calculate the hours and minutes 
# examples: num = 45 return 0:45; num = 126 return 2:6 
def TimeConvert(num): 
  return "0:" + str(num) if num < 60 else str(num / 60) + ":" + str(num % 60)

# sort the letters in a given string alphabetically 
def AlphabetSoup(str): 
  return ''.join(sorted(str)) 
  
# check if a given string contains 'a' and 'b' separated by presizely 3 characters 
def ABCheck(str): 
  for i,char in enumerate(str):
    if char == 'a':
      if i - 4 >= 0 and str[i-4] == 'b':
        return 'true' 
      if i + 4 < len(str) and str[i+4] == 'b':
        return 'true'
    
  return 'false'

# counts all vowels
def VowelCount(str): 
  vowels = 'aeiou'
  count = 0
  for char in str:
    if char.lower() in vowels:
      count += 1
  return count
    
# count the words in a string
def WordCount(str): 
  return len(str.split())   

# check if string is a palindrome ('eye', 'racecar')
def Palindrome(str): 
  forward = ''.join(str.split())
  backward = forward[::-1]
  #backward = ''
  #for char in forward:
  #  backward = char + backward
  if forward == backward:
    return 'true'
  else:
    return 'false'
    

  


# keep this function call here  
# to see how to enter arguments in Python scroll down
print FirstReverse(raw_input())
print FirstFactorial(raw_input())    
print LongestWord(raw_input())
print LetterChanges(raw_input())
print SimpleAdding(raw_input())
print LetterCapitalize(raw_input())
print SimpleSymbols(raw_input())
print CheckNums(raw_input())
print TimeConvert(raw_input())
print AlphabetSoup(raw_input())
print ABCheck(raw_input())
print VowelCount(raw_input())
print WordCount(raw_input())
print Palindrome(raw_input())
