import re

## 1.1 Is Unique
def isUnique(string):
  set_string = set()
  for i in string:
    if i in dict:
      return False
    else:
      set_string.add(i)
  return True

## 1.2 Check Permutation
def checkPermutation(string_one,string_two):
  dict_one =  getSet(string_one)
  dict_two = getSet(string_two)
  return dict_one == dict_two

def getSet(string):
  dict = {}
  for i in string:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  return dict

## 1.3 Urlify
def urlify (string):
  string = string.strip()
  return re.sub(' +', '%20', string)

## 1.4 Palindrome Permutation 
def palindromePer (string):
  string = re.sub(' ', '', string)
  string = string.lower()
  dict = {}
  for i in string:
    dict[i] = dict[i] + 1 if i in dict else  1
  middle = False
  for key,value in dict.items():
    if value % 2 == 1:
      if middle:
        return False
      middle = True
  return True

## 1.5 One Away
def oneAway (string_one,string_two):
  dict_one = getSet(string_one)
  dict_two = getSet(string_two)
  changeUsed = False
  for key, value in dict_one.items():
    if key in dict_two:
      dict_two[key] -= 1
    else:
      if changeUsed:
        return False
      changeUsed = True

## 1.6 String Compression
def stringCompression(string):
  result = ''
  count = 0
  cur_char = ''
  pre_char = ''
  changed = False
  for i in range(len(string)):
    cur_char = string[i]
    if i == 0:
      pre_char = string[i]
      count = 1
    else:
      if cur_char == pre_char:
        count += 1
      else:
        if count != 1:
          changed = True
        result += pre_char + str(count)
        count = 1
        pre_char = cur_char
  result +=pre_char +'1'
  return result if changed else string
