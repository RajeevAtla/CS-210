import pandas as pd

f1 = open("roster1.dat", 'r')
data = f1.read()
f1.close()

data = data.split('\n')

data2 = []
for person in data:
    data2.append(person.split(','))
data2.pop()

data = pd.DataFrame(data2, columns = ['Name', 'Major', 'GPA', 'Credits'])
data = data.astype({'GPA' : 'float', 'Credits' : 'float'})

count = data.groupby('Major').count()['Name'].rename('Count')
avgs = data.groupby('Major')[['GPA', 'Credits']].mean()
result = count.to_frame().join(avgs, on='Major')
majors = result.index.values


f2 = open("roster1.out", 'w')
s = ""
for major in majors:
    s += major
    s += ','
    s += result.loc[major]['GPA'].astype('str')
    s += ','
    s += result.loc[major]['Credits'].astype('str')
    s += ','
    s += result.loc[major]['Count'].astype('str')
    s += '\n'
    f2.write(s)

f2.close()
