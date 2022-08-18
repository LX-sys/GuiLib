# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
# monitor_status = requests.post("http://panda.vqmjc.cc/panda_api/assist/monitor_task_status", headers={
#         "MachineCode": "3e35a16a8de511eb86b01c1b0dac0807",
#         "Content-Type": "application/raw"
#     })
# print(monitor_status.text)
ss = requests.post("http://panda.vqmjc.cc/")

print(ss.text)