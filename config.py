# coding=utf-8
import configparser
import os


class Config(object):
    @staticmethod
    def config():
        """
        根据配置文件中的各种配置参数转换为字典并返回
        字典的键名型如：DB_host：DB为配置文件中的段名称，host为具体的配置项名称
        :return:
        """
        config = configparser.ConfigParser()
        path = os.path.dirname(os.path.abspath(__file__))
        config.read(path + '/config.cfg')
        settings = {}
        sections = config.sections()
        for s in sections:
            items = config.items(s)
            settings[s] = {}
            for i in items:
                key = i[0]
                settings[s][key] = config.get(s, key)
        settings['db'].update(settings[settings['base']['db']])
        del settings['dev_db']
        return settings


if __name__ == '__main__':
    pass
