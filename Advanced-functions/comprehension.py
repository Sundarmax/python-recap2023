# list comprehension
out = []

for i in range(10):
    if i % 2 == 0:
        out.append(i)

out2 = [i for i in range(10) if i % 2 ==0]

# dict comprehension

out3 = {i:i+1 for i in range(10) if i%2 == 0 }
print(out,out2,out3)
