import re
def regex_(pattern,string):
    patternRegex = re.compile(pattern)
    matched = patternRegex.search(string)
    print(matched.group()) if matched else print('NO MATCH')
def regex_2(pattern,string):
    patternRegex = re.compile(pattern)
    matched = patternRegex.findall(string)
    print(matched) if matched else print('NO MATCH')
def printline():
    print('-------------------------------')
#Optional matching with the question mark
bat_pattern = r'Bat(wo)?man'
t_string1 ='The Adventure of Batman'
t_string2 ='The Adventure of Batwoman'
regex_(bat_pattern,t_string1)
regex_(bat_pattern,t_string2)
printline()

#Matching zero or more with the Star
bat_pattern2 = r'Bat(wo)*man'
t_string3 = 'The Adventure of Batwowowoman'
regex_(bat_pattern2,t_string1)
regex_(bat_pattern2,t_string3)
printline()

#Matching zero or more with the Plus
bat_pattern3 = r'Bat(wo)+man'
regex_(bat_pattern3,t_string1)
regex_(bat_pattern3,t_string3)
printline()

#Matching specific repetition with Curly Brackets
ha_pattern = r'(ha){1}'
ha_pattern2 = r'(ha){2,3}'
ha_string = 'hahaha'
ha_string2 = 'hahah'
ha_string3 = 'ha'
regex_(ha_pattern,ha_string)
regex_(ha_pattern,ha_string2)
regex_(ha_pattern,ha_string3)
regex_(ha_pattern2,ha_string)
regex_(ha_pattern2,ha_string2)
regex_(ha_pattern2,ha_string3)
printline()

#Greedy and Nonegreedy
ha_pattern = r'(ha){2,3}'
ha_pattern2 = r'(ha){2,3}?'
ha_string = 'hahaha'
ha_string2 = 'hahah'
ha_string3 = 'ha'
regex_(ha_pattern,ha_string)
regex_(ha_pattern,ha_string2)
regex_(ha_pattern,ha_string3)
regex_(ha_pattern2,ha_string)
regex_(ha_pattern2,ha_string2)
regex_(ha_pattern2,ha_string3)
printline()

#Character Classes
xmas_pattern = r'\d+\s\w+'
xmas_string = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds'
regex_(xmas_pattern,xmas_string)
regex_2(xmas_pattern,xmas_string)
printline()

#Making my Own Character Class
vowelRegex = r'[aeiouAEIOU]'
vowelRegex2 = r'[^aeiouAEIOU]'
vowelSring = 'Robocop eats baby food, BABY FOOD.'
regex_2(vowelRegex,vowelSring)
regex_2(vowelRegex2,vowelSring)
printline()

#The Caret and Dollar Sign Characters
beginWithHello = r'^Hello'
begin_string = 'Hello world'
begin_string1 = 'He said hello'
regex_(beginWithHello,begin_string)
regex_(beginWithHello,begin_string1)
endsWithNumver = r'\d$'
end_string = 'Your number is 42'
end_string1 ='Your number is four'
regex_(endsWithNumver,end_string)
regex_(endsWithNumver,end_string1)
wholeStringRegex = r'^\d+$'
wholeString = '1234567'
wholeString1 = '123 34'
regex_(wholeStringRegex,wholeString)
regex_(wholeStringRegex,wholeString1)
printline()

atRegex = r'.at'
atString = 'The cat in the hat sat on the flat mat'
regex_2(atRegex,atString)
printline()

nameRegex = r'First Name:(.*) Last Name:(.*)'
nameSring = 'First Name: Al Last Name: Sweigart'
regex_(nameRegex,nameSring)
