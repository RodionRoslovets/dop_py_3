from functools import reduce
import re

def parseLine(line):
    match = re.search(r'\d+', line)
    if match:
        num = int(match.group())
        text = line[match.end():].strip()
        return (num, text)
    else:
        return None

def printText(acc, cur):
    if acc is None:
        print(cur[1])
        return cur[0]
    elif cur[0] > acc:
        print(cur[1])
        return cur[0]
    else:
        return acc

with open('file.txt', 'r') as f:
    lines = f.readlines()

data = list(filter(lambda x: x is not None, map(parseLine, lines)))

reduce(printText, data, None)

f.close()