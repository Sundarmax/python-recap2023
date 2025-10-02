string1 = 'bpple'
string2 = 'aanana'
if string1 == string2:
    print('The strings are equal')
elif string1 < string2:
    print('string1 comes before string2')
else:
    print('string2 comes before string1')

def stringFunc():
    str1 = "hello,world hello"
    start = "hello"
    end = "world"
    if str1.startswith(start):
        print(f"it starts with {start}")
    if str1.endswith(end):
        print(f"it ends with {end}")
    # check occurence of substring in string
    print(str1.count('hello'))

def stringFunc2():
    sentence = "This is an example sentence"
    idx = sentence.index("example")
    print(idx)
    try:
        idx = sentence.index("sentences")
    except ValueError:
        print("not found")

stringFunc()
# stringFunc2()
