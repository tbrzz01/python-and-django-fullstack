import re

patterns = ['term1', 'term2']

text = 'this is a string with term1, not not the other!'

for pattern in patterns:
    print('Im seraching for: ' + pattern)
    match = re.search('term1', pattern)

    print(match)



print(re.findall('match', 'test phrase match in match middle'))


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('searching for pattern {}'.format(pat))
        print(re.findall(pat, phrase))
        print('\n')


test_phrase = 'sdsd..sdsdsdsds.ddsdsdsd.'

# one or more
test_patterns = ['s[sd]+']

multi_re_find(test_patterns, test_phrase)

test_phrase = 'this is a string! but it has punctuation. How can we remove it?'

# exclusion
test_patterns = ['[^!.?]+']

multi_re_find(test_patterns, test_phrase)
