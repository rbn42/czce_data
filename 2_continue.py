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
            vol = float(vol)
            vol_all += vol
            start_all += float(start) * vol
            high_all += float(high) * vol
            low_all += float(low) * vol  # 最高最低依然用权重算,不求极值
            end_all += float(end) * vol
    print(d,start_all / vol_all, high_all / vol_all,
          low_all / vol_all, end_all / vol_all, vol_all)
