import matplotlib.pyplot as plt
import numpy as np
#获取数据和标签
def get_data(path):
    train_data = []
    train_labels = []
    test_labels = []
    with open(path) as ifile:
        for line in ifile:
            tokens = line.strip().split(' ')
            tmp_data = [int(tk) for tk in tokens[:-1]]
            tmp_label = tokens[-1]
            #设置胖瘦正常的标签，
            if tmp_label == 'fat':
                label = [1,0,0]
            elif tmp_label == 'normal':
                label = [0,1,0]
            elif tmp_label == 'thin':
                label = [0,0,1]
            train_data.append(tmp_data)
            train_labels.append(label)
            test_labels.append(tmp_label)

    return train_data, train_labels, test_labels
data_path = './bmi.txt'
train_data, train_labels, test_labels = get_data(data_path)

print(train_data)
print(train_labels)
print(test_labels)

train_data = np.array(train_data)
x = train_data[:,0]
y = train_data[:,1]
print(x)
print(y)
for indx in range(1000):
    if (test_labels[indx] == "fat"):
        plt.scatter(x[indx], y[indx], c='red', marker='.')
    elif (test_labels[indx] == "thin"):
        plt.scatter(x[indx], y[indx], c='blue', marker='.')
    elif (test_labels[indx] == "normal"):
        plt.scatter(x[indx], y[indx], c='green', marker='.')
# plt.scatter(x, y, c='red', marker='.')
plt.show()
