import csv


def read_fromm_csv():
    """从csv文件中读取数据，读取后的数据形式为嵌套列表"""
    examplefile = open('Test\\example.csv', 'r')
    examplereader = csv.reader(examplefile)
    exampledata = list(examplereader)
    print(type(exampledata))
    for data in exampledata:
        print(type(data))
        print(data)


def write2csv():
    """输出数据到csv文件"""
    outputfile = open('output.csv', 'w', newline='')    # 添加参数newline='',否则输出的文件行距为两倍
    outputwriter = csv.writer(outputfile)
    outputwriter.writerow(['spam', 'eggs', 'bacon', 'ham'])         # writerow()方法的参数为一个列表
    outputwriter.writerow(['Hello， world', 'eggs', 'bacon', 'ham'])      # Writer对象会自动转义逗号，不必自己处理
    outputwriter.writerow([1, 2, 3, 141592, 4])
    outputfile.close()


def change_delimiter_lineterminator():
    """csv文件默认分隔符为,，默认行终止符为\n。 使用delimiter和lineterminator参数可以改变分隔符和行终止符"""
    outputfile = open('Test\\delimiter_lineterminator.csv', 'w', newline='')
    outputwriter = csv.writer(outputfile, delimiter='\t', lineterminator='\n\n')
    outputwriter.writerow(['apples', 'oranges', 'grapes'])
    outputwriter.writerow(['eggs', 'eggs', 'eggs', 'eggs'])
    outputwriter.writerow(['spam', 'spam', 'spam', 'spam'])
    outputfile.close()


if __name__ == '__main__':
    change_delimiter_lineterminator()
