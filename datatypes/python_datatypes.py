def python_list():
    list_int = [3,4,5,6,1,2]
    # add single element
    list_int.append(7)
    # add multiple element
    list_int.extend([8,9])
    # list_int.extend([[10,11]])
    print(list_int)
    # return first appearance
    idx =  list_int.index(8)
    print(idx)
    # find max,min, len
    print(max(list_int),min(list_int),len(list_int))
    # compare two list
    # list_int2 = [1,2]
    print(type(list_int))
    # get sum of list
    print(sum(list_int))

def python_tuple():
    sample_tuple = (0,2,3,0)
    sample_tuple2 = (False,False)
    sample_tuple3 = (1,2,3,1)
    print(max(sample_tuple), min(sample_tuple),len(sample_tuple))
    print(sum(sample_tuple))
    print(sample_tuple.count(1))
    # if any of the item is true/valid it returns True
    print(any(sample_tuple))
    print(any(sample_tuple2))
    # if all items are true then it returns True
    print(all(sample_tuple3))
    # get index
    print(sample_tuple.index(2))

def python_dict():
    veg_dict  = {"potato":'50KG',"tomato":'70KG'}
    print(veg_dict.keys())
    print(veg_dict.values())
    # remove element with specified key
    veg_dict.pop('tomato')
    print("After removing key", veg_dict)
    # add new key
    veg_dict['Gauliflower'] = "10KG"
    print("After adding key : ",veg_dict)
    # pop the last item 
    veg_dict.popitem()
    print("After poping last itme : ", veg_dict)
    # add/update a key with default
    veg_dict.setdefault("carrot","5G")
    print(veg_dict)
    # return tuple for each key, value pair
    print(veg_dict.items())
    # clear the data in dict
    # veg_dict.clear()
    # print("After clearing dict data : ", veg_dict)
    print(veg_dict.fromkeys(['potato']))
    print(veg_dict)

def python_sets():
    temp = set()
    temp.add(1)
    temp.clear()
    print(temp)
    # difference
    A = {10, 20, 30, 40, 80}
    B = {100, 30, 80, 40, 60}
    print(A -B, B - A)
    # intersect
    print(A.intersection(B))
    # symmetric diff skip common ele on both sets & return the rest.
    print(A.symmetric_difference(B))
    # union
    print(A.union(B))
    # pop an element
    A.pop()
    print(A)

# python_list()
# python_tuple()
python_dict()
# python_sets()