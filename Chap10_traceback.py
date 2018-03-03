"""
导入traceback模块， 将反向追踪的字符串写入文本文件
"""

import traceback
try:
    raise Exception('This is a exception message !')
except:
    errorfile = open('errorInfo.txt', 'w')
    errorfile.write(traceback.format_exc())
    errorfile.close()
    print('The traceback information is written to errorInfo.txt.')
