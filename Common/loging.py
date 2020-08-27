import logging
from common.config import ReadConfig
from common import contants
class Log:

    def __init__(self,logger):
        self.logger= logger#读取配置文件
        self.set_level=ReadConfig().get('LOG','setlevel')
        self.filename=ReadConfig().get('LOG','filename')
        self.formatter=ReadConfig().get('LOG','formatter')

    def log_system(self,level,msg):
        #新建一个日志收集器
        log=logging.getLogger(self.logger)
        #定义收集的日志级别
        log.setLevel(self.set_level)
        #定义日志的格式
        fm=logging.Formatter(self.formatter)
        #新建一个日志输出器
        sc=logging.StreamHandler()
        #定义输出的级别
        sc.setLevel(self.set_level)
        #传入输出格式
        sc.setFormatter(fm)
        #新建一个输出的文件
        fh=logging.FileHandler(contants.log_dir + '\case.log',encoding='utf-8')
        #写入文件日志级别
        fh.setLevel('INFO')
        #写入的格式
        fh.setFormatter(fm)
        # 对接 日志收集器与输出渠道 进行对接
        log.addHandler(sc)
        log.addHandler(fh)
        if level=='DEBUG':
            log.debug(msg)
        elif level=='INFO':
            log.info(msg)
        elif level=='WARNING':
            log.warning(msg)
        elif level=='ERROR':
            log.error(msg)
        else:
            log.critical(msg)
        log.removeHandler(sc)
        log.removeHandler(fh)
    def debug(self,msg):
        self.log_system('DEBUG',msg)

    def info(self,msg):
        self.log_system('INFO',msg)

    def warning(self,msg):
        self.log_system('WARNING',msg)

    def error(self,msg):
        self.log_system('ERROR',msg)

    def critical(self,msg):
        self.log_system('CRITICAL',msg)
