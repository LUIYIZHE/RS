
old_source = 'https://pypi.org/'
new_source = 'https://pypi.douban.com/simple'

pyt_path = r'Z:\Program Files\开发工具\pytools\Lib\site-packages\pip\_internal\models\index.py'
py7_path = r'Z:\Program Files\python3.7\Lib\site-packages\pip\_internal\models\index.py'
py8_path = r'Z:\Program Files\python3.8\Lib\site-packages\pip\_internal\models\index.py'
path = [pyt_path,py7_path,py8_path]

def change_source(path):
    with open(path,'r+') as fio:
        read = fio.read()
        write = read.replace(old_source,new_source,1)
        fio.seek(0)
        fio.write(write)

if __name__ == '__main__':
    for x in path:
        change_source(x)


    
