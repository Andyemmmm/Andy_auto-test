import time
import os
import random


def get_time_stamp(days, flag=1):
    '''
    返回时间戳
    :param days:如果是1，代表返回昨天的时间戳，如果是2，代表返回是前天的时间戳，以此类推
    :param flag:1-指定的那一天零点时间戳，2-指定的那一天最后一秒的时间戳
    :return:
    '''
    localtime = time.localtime()
    format_time = str(localtime[0]) + '-' + str(localtime[1]) + '-' + str(localtime[2]) + ' '
    start = format_time + '0:0:0'
    end = format_time + '23:59:59'
    yesterday_s_array = time.strptime(start, '%Y-%m-%d %H:%M:%S')
    yesterday_e_array = time.strptime(end, '%Y-%m-%d %H:%M:%S')
    timestamp = 0
    if flag == 1:
        timestamp = int(time.mktime(yesterday_s_array)) - 24 * 60 * 60 * int(days)
    if flag == 2:
        timestamp = int(time.mktime(yesterday_e_array)) - 24 * 60 * 60 * int(days)
    return timestamp


def make_dir(path):
    '''
    创建指定的目录并返回，失败则返回False
    :return:
    '''
    try:
        if os.path.exists(path) is False:
            os.makedirs(path)
            return path
    except:
        return False


def get_user_agent(path=None):
    """
    随机返回一个浏览器头
    :param path:
    :return:
    """
    if path is None:
        path = os.path.dirname(os.path.abspath(__file__)) + '/driver/lib/user_agent.txt'
    f = open(path, 'r')
    lines = f.read()
    lines = lines.splitlines()
    agent = []
    for line in lines:
        agent.append(line)
    agent = random.choice(agent)
    length = len(agent)
    agent = agent[1:length - 1]
    return agent
