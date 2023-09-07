import logging

"""
日志级别等级排序：critical > error > warning > info > debug 级别越高打印的日志越少，反之亦然，即
debug : 打印全部的日志( notset 等同于 debug )
info : 打印 info, warning, error, critical 级别的日志
warning : 打印 warning, error, critical 级别的日志
error : 打印 error, critical 级别的日志
critical : 打印 critical 级别
"""

def intro_logging():
    # 设置日志模块
    logging.basicConfig(
        level=logging.INFO, # 该参数控制记录日志的等级
        filename="./intro_test.log", #该参数指定日志输出文件，没有则打印到控制台
        filemode="w", # 该参数控制日志文件写入的模式
        format='%(asctime)s;%(levelname)s;%(message)s', # 该参数控制日志输出格式
    )
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')

intro_logging()

