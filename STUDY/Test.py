#import re
#import difflib
desti = 'cam:ep01sc03cam04s424e4255'.split()

#pattern = re.compile(r'\d')
#m = pattern.search(desti)
#m = pattern.findall(desti)

desti.remove('cam:ep01sc03cam04')
print(desti)
