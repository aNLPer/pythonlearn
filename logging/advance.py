"""
记录器:暴露了应用程序代码直接使用的接口
处理器:将日志记录（由记录器创建）发送到适当的目标
过滤器:提供了更精细的附加功能，用于确定要输出的日志记录
格式器:指定最终输出中日志记录的样式.
这四者存在一个层级关系
"""
import logging
# create logger
logger = logging.getLogger('simple_example') # 创建logger
logger.setLevel(logging.DEBUG) # 设置logger等级
# create console handler and set level to debug
ch = logging.StreamHandler() # 创建handler
ch.setLevel(logging.DEBUG) # 创建handler处理等级
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')