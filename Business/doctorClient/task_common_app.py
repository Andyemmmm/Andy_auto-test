#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2020/2/12 21:55
# @File     : task_common_app.py
# @Software : aiwen_ui

from Business.base_url import aiwen_app, app_name


def is_install(driver):
    # 判断是否安装APP
    wallpaper = driver.is_app_installed(app_name)
    if wallpaper:
        pass

    else:
        driver.install_app(aiwen_app)
