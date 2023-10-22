import copy

# we use copy module of python for shallow and deep copy opertions. .
# copy.copy(x)
# copy.deepcopy(x)

def shallow_copy():
    # creates independent object with same content
    old_list = [[1,2,3], [4,5,6], [7,8,9]]
    new_list = copy.copy(old_list)
    print(id(old_list),id(new_list))
    # adding new item to old list to check if it reflects to new list or not
    old_list.append([4,4,5])
    # case - I # no impact on original list
    print(old_list,new_list)
    # case - II # when  you make a chaneges in nested object you have an impact in copied list & vice versa
    # add changes to new nested object using shallow copy
    new_list[1][1] = 'AA'
    print(old_list,new_list)

def deep_copy():
    # creates independent copy of original object and all it's nested obejects.
    old_list = [[1,2,3], [4,5,6], [7,8,9]]
    new_list = copy.deepcopy(old_list)
    print(id(old_list),id(new_list))
    # add changes to nested object in new_list you can see there is no impact.
    new_list[1][1] = 'AA'
    print(old_list,new_list)

shallow_copy()
deep_copy()