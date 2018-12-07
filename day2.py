from collections import Counter

with open("day2.input") as f:
    data = f.read()

two_counter = 0
three_counter = 0
serials = []
for l in data.split("\n"):
    #print(l + " ...")
    serials.append(l)
    c = Counter(l)
    #print(c)
    if 2 in c.values():
        #print(c.values())
        #print("two")
        two_counter += 1
    if 3 in c.values():
        #print("three")
        three_counter += 1
print(str(two_counter) + " " + str(three_counter) + " " + str(two_counter * three_counter))


def map_str_diff(str1, str2):
    return [i for i in zip(str1, str2) if i[0] != i[1] ]

#print(len(serials))
total_len = len(serials)
for i in range(total_len):
    for j in range(i+1, total_len):
        diff_list = map_str_diff(serials[i], serials[j])
        if len(diff_list) == 1:
            print(diff_list, serials[i], serials[j], "".join([i[0] for i in zip(serials[i], serials[j]) if i[0] == i[1]]) )
            break





