import datetime
day = datetime.date(2013, 11, 5)
while day<datetime.date(2015,6,5):
    day+=datetime.timedelta(days=1)
    day_str=day.strftime('%Y%m%d')
    year_str=day.strftime('%Y')
    url='http://www.czce.com.cn/portal/exchange/%s/datadaily/%sTC.txt'%(year_str,day_str)
    print(url)
