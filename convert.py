import json

content = open('demonyms.txt', 'r', encoding='utf8').read().split('\n')
content = [list(e.split(' - ') for e in row.split(' ---> ')) for row in content]

content_loc = [{loc: e[1]} for e in content for loc in e[0]]
content_gen = [{gen: e[0]} for e in content for gen in e[1]]


with open('countries.json', 'w') as outfile:
    json.dump(content_loc, outfile, indent=2, sort_keys=True)

with open('demonyms.json', 'w') as outfile:
    json.dump(content_gen, outfile, indent=2, sort_keys=True)
