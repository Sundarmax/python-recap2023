import pickle
# https://medium.com/analytics-vidhya/pickling-and-unpickling-in-python-explained-be546e604aae
# use case
# To save a program’s state data to disk so that it can carry on where it left off when restarted (persistence)

def pickling():
    data = {
        "name":"sundar",
        "age" : 1
    }
    filename ="test"
    out_file = open(filename, 'wb')
    # pickle.dump(object, file_obj, protocol)
    pickle.dump(data, out_file)

def unpickling():
    filename = "test"
    file_obj = open(filename,'rb')
    new_data = pickle.load(file_obj)
    file_obj.close()
    print(new_data)

#pickling()
unpickling()
