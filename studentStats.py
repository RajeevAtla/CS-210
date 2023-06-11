import numpy as np
import numpy.lib.recfunctions as rfn

arr = np.zeros(4, dtype={'names': ('name', 'age', 'major', 'gpa'),
'formats': ('U50', 'i4', 'U4', 'f8')})

f1 = open("roster2.dat", 'r')
data = f1.read()
f1.close()

data = data.split('\n')

data2 = []
for person in data:
    data2.append(person.split(','))


for index, value in np.ndenumerate(arr):
    row_num = index[0]
    data2[row_num][0] = str(data2[row_num][0])
    data2[row_num][1] = int(data2[row_num][1])
    data2[row_num][2] = str(data2[row_num][2])
    data2[row_num][3] = float(data2[row_num][3])

    arr[index] = data2[row_num]

print(arr)


"""
data2 = np.array(data2)
print(data2)
data2[:, 0] = data2[:, 0].astype('U50')
data2[:, 1] = data2[:, 1].astype('i4')
data2[:, 2] = data2[:, 2].astype('U4')
data2[:, 3] = data2[:, 0].astype('f8')

# arr = np.ndarray(buffer = data3, dtype=[('name', '<U50'), ('age', '<i4'), ('major', '<U4'), ('gpa', '<f8')], shape = data3.shape)
#dt = {'names': ('name', 'age', 'major', 'gpa')}
#arr.dtype = dt

#arr.names = ['name', 'age', 'major', 'gpa']
#arr.astype(['U50', 'i4', 'U4', 'f8'])
"""
