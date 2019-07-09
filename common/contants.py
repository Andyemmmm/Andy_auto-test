import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
case_file = os.path.join(base_dir, 'data', 'cases2.xlsx')

global_file = os.path.join(base_dir, 'config', 'global.conf')

online_file = os.path.join(base_dir, 'config', 'online.conf')

test_file = os.path.join(base_dir, 'config', 'test.conf')

log_dir = os.path.join(base_dir, 'log')
print(log_dir)
case_dir = os.path.join(base_dir, 'testcase')

report_dir = os.path.join(base_dir, 'reports')

