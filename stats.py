def get_num_words(text):
    text_as_list = text.split()
    return len(text_as_list)

def get_num_char(text):
    low_text = text.lower()
    dic = {}
    for c in low_text:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] +=1
    return dic

#test=get_num_char("abc")
#print(test)
def sort_on(items):
    return items["num"]

def get_sorted_dict(dic):
    list = []
    for entry in dic:
        if entry.isalpha()==True:
            temp_dic={"char": entry, "num": dic[entry]}
            list.append(temp_dic)
    list.sort(reverse=True,key=sort_on)
    return list


##test_list=[{"char": "a", "num": 10},{"char": "b", "num": 20}]
##print("This is a test")
##print(test_list)
##print("This is a test 2")
##print(test_list[1]["char"],": ",test_list[1]["num"])