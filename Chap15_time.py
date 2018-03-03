"""回顾Python当中的时间函数"""
import datetime
import time


def get_datetime():
    """获取datetime对象，和datetime对象的属性"""
    now = datetime.datetime.now()
    print('数据类型为：%s' % (type(now)))
    print(now)
    dt = datetime.datetime(2018, 2, 7, 23, 34, 10)
    print('数据类型为：%s' % (type(now)))
    print(dt)
    print(dt.year)      # int
    print(dt.month)
    print(dt.day)


def change2datetime():
    """将unix纪元时间戳转换为datetime对象"""
    print(datetime.datetime.fromtimestamp(1000000))
    print(datetime.datetime.fromtimestamp(time.time()))
    print(time.time())
    print(time.asctime())


def compare_datetime():
    """可以通过比较datetime对象来判断哪个时间在前。时间越靠后值越大"""
    time_2015 = datetime.datetime(2015, 1, 5, 0, 0, 0)
    time_2016 = datetime.datetime(2016, 1, 5, 0, 0 ,0)
    print(time_2016 > time_2015)


def get_timedelta():
    """获取delta数据类型，delta对象的属性，及其属性的对象类型"""
    delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
    print('delta', type(delta), delta)
    print(type(delta.days), type(delta.seconds), type(delta.microseconds))      # int
    print(delta.days, delta.seconds, delta.microseconds)
    print('delta.total_seconds()', type(delta.total_seconds()), delta.total_seconds())      # float


def compute_time():
    """
    datetime.datetime + datetime.delta,
    datetime.datetime +/- datetime.delta * int
    date模块会自动处理闰年因素和其他棘手的细节
    """
    pass


def suspend_to_specific_time():
    """将程序暂停至特定日期"""
    specific_time = datetime.datetime(2018, 3, 5, 3, 5, 6)
    if datetime.datetime.now() < specific_time:
        time.sleep(1)


def datetime2string():
    """datetime类型对人类不是很友好可读， 多以datetime模块提供了格式化datetime对象的方法strftime()"""
    oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
    print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
    print(oct21st.strftime('%I:%M %p'))
    print(oct21st.strftime('%j of %Y'))


def string2datetime():
    """将符合指定格式的字符串转化为datetime对象，使用strptime()方法"""
    dt = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
    print(type(dt), dt)


if __name__ == '__main__':
    get_datetime()
