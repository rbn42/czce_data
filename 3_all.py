import glob
import os.path
path = './1/tc/*.txt'
files = glob.glob(path)
files.sort()
for f in files:
    _,d=os.path.split(f)
    d=d[:8]
    high_all, low_all, start_all, end_all, vol_all = 0, 0, 0, 0, 0
    for line in open(f, encoding='gbk'):
        if line.startswith('TC'):
            item = line.split(',')
            start, high, low, end, _, _, _, vol = item[2:10]
            name=item[0]
            print(d,name,start,high,low,end,vol)
