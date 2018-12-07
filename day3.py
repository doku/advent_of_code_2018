
import re

"""

Our sponsors help make Advent of Code possible:
Alfie by Prodo - a more immediate, feedback-driven coding experience. Try our online JavaScript playground with Advent of Code!

--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?

Your puzzle answer was 105047.


"""






with open("day3.input") as f:
    data = f.read()

data_list = []
for l in data.split("\n"):
    if l != "":
        data_list.append(l)
    #print(l)

data_list_dic = []
for j in data_list:
    #print(j)
    match = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", j)
    #print(match.group(0), match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
    data_dic = {}
    data_dic["id"] = match.group(1)
    data_dic["shift"] = (int(match.group(2)), int(match.group(3)))
    data_dic["width"] = (int(match.group(4)), int(match.group(5)))
    data_dic["coord2"] = map(sum, zip(data_dic["shift"], data_dic["width"]))
    data_list_dic.append(data_dic)


data_matrics = [[0 for _ in range(1000)] for _ in range(1000)]

for data in data_list_dic:
    #print(data)
    for x in range(data["shift"][0], data["coord2"][0]):
        for y in range(data['shift'][1], data['coord2'][1]):
            data_matrics[x][y] = data_matrics[x][y] + 1
    

print(sum([sum([1 for i in row if i >= 2]) for row in data_matrics]))

"""

--- Part Two ---
Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?

"""

for data in data_list_dic:
    #print(data)
    flag = False
    for x in range(data["shift"][0], data["coord2"][0]):
        for y in range(data['shift'][1], data['coord2'][1]):
            # data_matrics[x][y] = data_matrics[x][y] + 1
            if data_matrics[x][y] != 1:
                flag = True
            if flag == True:
                break
        if flag == True:
            break
    if flag == False:
        print(data)
        







