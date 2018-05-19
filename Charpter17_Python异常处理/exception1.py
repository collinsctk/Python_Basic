def find_index(obj, index):
    print(obj[index])

if __name__ == '__main__':
    import re
    try:
        find_index('qytang', 'cisco')
    except IndexError:
        print('索引错误，可能是索引值超出范围！')
    except TypeError as e:
        if re.match(".*'int' object is not subscriptable", str(e)):
            print('整数对象是不支持索引的')
        elif re.match(".*string indices must be integers", str(e)):
            print('索引必须是整数对象')
        else:
            print('其他索引错误',e)
    else:
        print('没有任何错误发生！')
    finally:
        print('这个总是要打印的！')