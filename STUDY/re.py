import re
desti = 'cam:ep01sc03cam04s424e4255'
pattern = re.compile(r'\d')
m = pattern.search(desti)
m.group()