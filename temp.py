# -*- coding: utf-8 -*-

list_temp = []
dict_temp = {}
with open("flag.txt", "r") as f_in:
    for line in f_in:
        tag, prop = line.strip().split("\t")
        dict_temp[tag] = prop
f_in.close()

with open("dict.txt", "r") as f_in:
    for line in f_in:
        _, _, tag = line.strip().split(" ")
        list_temp.append(tag)
f_in.close()
list_temp = sorted(list(set(list_temp)), key=lambda l: l)

f_out = open("temp.out", "w")
for item in list_temp:
    f_out.write(item + "\t")
    if item in dict_temp:
        f_out.write(dict_temp[item])
    f_out.write("\n")
f_out.close()
