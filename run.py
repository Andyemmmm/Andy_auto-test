"""统一运行入口"""
import argparse
import unittest
import HTMLReport
from EleganceReport import EleganceReport

from Common.tools.rw_ini import write_config

from Test_Suite.communityClient.用户中心 import suite_登录, suite_医生, suite_注册
from Test_Suite.communityClient.Application import suite_science_project, suite_network_bbs, suite_questionnaire, \
    suite_hospital, suite_doctor_class, suite_health_knowledge, suite_information, suite_健康科普
from Test_Suite.communityClient.Community import suite_community, suite_finance, suite_user, suite_setting, \
    suite_new_community, suite_bseting

# 从命令行读取参数修改配置文件
parser = argparse.ArgumentParser(
    description="运行测试"  # 用来说明这个程序在做什么
)
parser.add_argument("-name", dest="name",
                    choices={"chrome", "firefox", "ie"}, default=None,
                    help="浏览器名字")
args = parser.parse_args()

if args.name is not None:
    write_config("Config/browser.ini", "browser", "name", args.name)

suite = unittest.TestSuite()  # 总的测试套件

'''社区B端---登陆的测试套件'''
suite.addTests(suite_登录.login())
# suite.addTests(suite_登录.login_code())
suite.addTests(suite_登录.loginout())
suite.addTests(suite_登录.experience_community())
# suite.addTests(suite_注册.register())

'''社区B端---新建社区的测试套件'''
suite.addTests(suite_new_community.new_community_hoapital())
suite.addTests(suite_new_community.new_community_organization())
suite.addTests(suite_new_community.new_community_doctorteam())
suite.addTests(suite_new_community.new_community_project())
suite.addTests(suite_new_community.new_test_community_hoapital())
suite.addTests(suite_new_community.new_test_community_organization())
suite.addTests(suite_new_community.new_test_community_doctorteam())
suite.addTests(suite_new_community.new_test_community_project())

'''社区B端---首页模块的测试套件'''
# suite.addTests(suite_bseting.organization_update_name())
# suite.addTests(suite_bseting.Add_members())
# suite.addTests(suite_bseting.remove_members())
# suite.addTests(suite_bseting.update_personal())
# suite.addTests(suite_bseting.change_password())

'''社区B端---社区模块的测试套件 '''
# suite.addTests(suite_community.get_suite())

'''社区B端---医生模块的测试套件'''
# suite.addTests(suite_医生.doctor_invite())
# suite.addTests(suite_医生.label_management())

'''社区B端---用户模块的测试套件'''
# suite.addTests(suite_user.get_suite())

'''社区B端---财务模块的测试套件'''
# suite.addTests(suite_finance.get_suite())

'''社区B端---应用模块的测试套件'''
# suite.addTests(suite_健康科普.get_suite())
# suite.addTests(suite_science_project.get_suite())
# suite.addTests(suite_information.get_suite())
# suite.addTests(suite_health_knowledge.get_suite())
# suite.addTests(suite_doctor_class.get_suite())
# suite.addTests(suite_hospital.get_suite())
# suite.addTests(suite_questionnaire.get_suite())
# suite.addTests(suite_network_bbs.get_suite())

'''社区B端---设置模块的测试套件'''
# suite.addTests(suite_setting.add_members())
# suite.addTests(suite_setting.remove_members())
# suite.addTests(suite_setting.new_role())
# suite.addTests(suite_setting.del_role())

'''报告模板1'''
# HTMLReport.TestRunner(
#     title="社区B端自动化测试",
#     description="社区 web ui 自动化测试",
#     report_file_name="index",
#     thread_count=1
# ).run(suite)

'''报告模板2'''
result = EleganceReport(suite)
result.report(filename='测试报告', description='爱问后台测试报告', report_dir='report', theme='theme_memories')
