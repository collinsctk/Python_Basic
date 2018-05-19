def find_index(obj, index):
    print(obj[index])

if __name__ == '__main__':
    import re
    try:
        find_index('qytang', 'cisco')
#    except:               #它会捕获所有异常，even system exitcalls and Ctrl-C key combinations
#        pass
    except Exception:     #推荐捕获除了system exitcalls and Ctrl-C key combinations以外的异常
        pass
#    except Exception as e: #打印异常内容
#        print(e)
    else:
        print('没有任何错误发生！')
    finally:
        print('这个总是要打印的！')