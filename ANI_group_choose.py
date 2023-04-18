

dict_qr = {}
dict_ani = {}
with open(r'test_ani_result.txt') as fin :
    for line in fin:
        part = line.strip().split('\t')
        query = part [0]
        name_part = query.strip().split('/')
        name = name_part[5]
        ref = part [1]
        ani = part [2]
        if name not in dict_ani:
            dict_ani[name] = []
            dict_ani[name].append(ani)
        else:
            dict_ani[name].append(ani)


        if name not in dict_qr:
            dict_qr[name] = []
            dict_qr[name].append(ref)
        else:
            dict_qr[name].append(ref)
    #print(dict_qr)
    #print(dict_ani)
    for key in dict_ani:
        i = dict_ani[key].index(max(dict_ani[key]))
        print(key,end="\t")
        print(dict_qr[key][i],end="\t")
        print(max(dict_ani[key]),end="\n")



#print(dict_ani)
#print(dict_qr)
#print(dict_ani[name].index(max(dict_ani[name])))