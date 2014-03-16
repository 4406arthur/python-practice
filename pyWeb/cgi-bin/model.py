#! /usr/local/bin/python3

import glob
import pickle
import yate
def get_file_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data)
    except:
        print ("block A error")


def writeList(file_list):
    all_img = {}
    for each_item in file_list:
        stream = get_file_data(each_item)
        all_img[each_item] = stream
    with open('all_list.pickle','wb') as wf:
        pickle.dump(all_img,wf)
    return (all_img)

def get_img():
    all_img ={}
    with open('all_list.pickle','rb') as rf:
        all_img = pickle.load(rf)
    return (all_img)


"""data_files = glob.glob("data/*.txt")
data = writeList(data_files)


num = len(data_files)
print (num)
print (data_files)
print (data)"""
