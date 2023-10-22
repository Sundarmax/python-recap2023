
a  =[1,2,3]
a.append(5)
print("List after adding an item : ",a)
a.extend([6,7])
print("List after extending two elements : ",a)
a.extend('AB') # argument should be iterable.
print("List after extending string :",a)
a.extend(['CD'])
print("List after extending another list :",a)

