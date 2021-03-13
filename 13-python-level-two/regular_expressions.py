import re  # module for regular expressions

patterns = ['term1', 'term2']

text = "This is a string with term1, not the other!"

""" for pattern in patterns:
    print("I'm searching for " + pattern)

    if re.search(pattern, text):
        print("Match!")
    else:
        print("Not a match") """

match = re.search('term1', text)

print(type(match))
print(match.start())  # error when it wasn't found!

split_term = '@'
email = 'user@gmail.com'
match = re.split(split_term, email)
print(type(match))
print(match)

print(re.findall('match', 'test phrase match i match middle'))  # len gives


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print(f"Searching for pattern {pat}")
        print(re.findall(pat, phrase))
        print('\n')


# repetition
# * means repeated 0 or more times
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_phrase2 = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = ['sd*',  # * means repeated 0 or more times
                 'sd+',  # + means repeated 1 or more times
                 'sd?',  # ? means repeated 0 or 1 times
                 'sd{3}',  # s followed by 3 d
                 'sd{1,3}',  # s followed by 1 or 3 d
                 's[sd]+',  # s followed by s OR d
                 ]


multi_re_find(test_patterns, test_phrase)


test_patterns2 = ['[^!.?]+',  # ^ is used for exclusion
                  '[a-z]+',  # sequences of haracters
                  r'\d+',  # digits
                  ]

multi_re_find(test_patterns2, test_phrase2)

test_phrase3 = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns3 = [r'\d+',  # digits
                  r'\D+',  # non-digits
                  r'\s+',  # whitespace
                  r'\w+',  # alfa-numeric
                  r'\W+',  # non-alfa-numeric
                  ]
multi_re_find(test_patterns3, test_phrase3)
