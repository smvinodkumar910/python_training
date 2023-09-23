

import Hellow_world

import re

txt = "The rain in Spain"
x = re.search("ai", txt)

print(x.start())
print(x.end())
print(x)
print(x.group())
print(x.groups())
print(x.groupdict)


