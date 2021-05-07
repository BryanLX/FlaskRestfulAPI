import re

## 1.1 Is Unique
def isUnique(string):
  dict = {}
  for i in string:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  for key, value in dict.items():
    if value > 1:
      return False
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

