# Use this file with rarechar.txt file in the folder...

# method one
import collections
import pprint
file_input = input('File Name: ')
with open(file_input, 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
print(value)

# method two
#data=open(pathfile,"r").read()
#tab=[]
#for car in data:
#    if tab.count(car)==0:
#        tab.append(car)
#print(tab)
