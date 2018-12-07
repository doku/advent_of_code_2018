import re
import datetime
import pandas as pd

data = []
with open("day4.input") as f:
    for l in f:
        data.append(l.strip())
    #data = f.read()


f = []
for d in data:
    g = re.match(r"\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)$", d)

    #print(g.group(0), g.group(1) , g.group(2), g.group(3), g.group(4), g.group(5), g.group(6))
    #print(datetime.datetime(int(g.group(1)), int(g.group(2)), int(g.group(3)), int(g.group(4)), int(g.group(5))))
    f.append((datetime.datetime(int(g.group(1)), int(g.group(2)), int(g.group(3)), int(g.group(4)), int(g.group(5))), g.group(6)) )

#print(pd.DataFrame(f))

df = pd.DataFrame(f, columns=["dates", "value"]) 
#print(df)

#print(df.head(5))
df = df.sort_values("dates")
#print(df)


for i, r in df.iterrows():
    print(r)


#print(data








