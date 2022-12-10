import numpy as np
from matplotlib import pyplot as plt


def data_read(dir_path):
    with open(dir_path, "r") as f:
        raw_data = f.read()
        data = raw_data[1:-1].split(", ")  # [-1:1]是为了去除文件中的前后中括号"[]"
    return np.asfarray(data, float)

if __name__ == "__main__":
    train_loss_path = r"D:\sukkart\my projects\neural_network\train_acc.txt"  # 存储文件路径
    test_loss_path = r"D:\sukkart\my projects\neural_network\test_acc.txt"

    y_train_acc = data_read(train_loss_path)  # loss值，即y轴
    x_train_acc = range(len(y_train_acc))  # loss的数量，即x轴

    y_test_acc = data_read(test_loss_path)
    x_test_acc = range(len(y_test_acc))

    plt.figure()

    # 去除顶部和右边框框
    ax = plt.axes()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.xlabel('epoch')  # x轴标签
    plt.ylabel('accuracy')  # y轴标签

    # 以x_train_loss为横坐标，y_train_loss为纵坐标，曲线宽度为1，实线，增加标签，训练损失，
    # 默认颜色，如果想更改颜色，可以增加参数color='red',这是红色。
    plt.plot(x_train_acc, y_train_acc, color="blue", linewidth=1, label="train acc")
    plt.plot(x_test_acc, y_test_acc, color="red", linewidth=1, label="test acc")
    plt.legend()
    plt.title('Accuracy curve')
    plt.show()
