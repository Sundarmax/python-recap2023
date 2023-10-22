import re

pattern = '^a...s$' # any 5 letters starting with a and ending with 5.
test_string =  'abyss'
# [] - specifies a set of char you wish to match

def test_regex(search_pattern, source_string):
    result = re.match(search_pattern, source_string)
    if result: # it doesn't return bool value
        print('The given string is : ', source_string)
        print('Search successful for the given pattern : ', search_pattern)
    else:
        print('Search unsucessful.')

# test_regex(pattern,test_string)
# test_regex('[abc]',test_string)
# test_regex('[xyz]',test_string)
# test_regex('[add]',test_string) # if it matches the any one of char in the list with given string
# test_regex('[^cdx]',test_string) # any of char except those in the list
# test_regex('[^0-9]', test_string) # any except those digits 
# test_regex('^a',test_string) # if it's startwith a
# test_regex('^x', test_string)
# test_regex('s$', test_string) # it it's endswith s
# test_regex('.',test_string)
# test_regex('.','\n')
# test_regex('aby*s',test_string)
# test_regex('ab*s', test_string)
# test_regex('a*s', 'aas') # find zero or more occurance on left
# test_regex('a*s', 's')
# test_regex('a+s','s') # find one or more occurence on left
# test_regex('aby?s',test_string) # zero or one occurence on left side of ? sympol
