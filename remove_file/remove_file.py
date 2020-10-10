# @Time    : 2020/10/10 15:52
# @Author  : Leafage
# @File    : remove_file.py
# @Software: PyCharm
# @Describe: 删除指定目录及子目录中指定的文件格式
import os


def remove_file_in_dir(root_dir, delete_type):
    """
    删除目录及子目录中所有后缀在delete_type集合中的文件，慎重使用！！！
    :param root_dir: 想要删除文件的最高级目录
    :param delete_type: 删除的类型集合
    :return:
    """
    count = 0
    for home, dirs, files in os.walk(root_dir):
        for filename in files:
            if os.path.splitext(filename)[-1] in delete_type:
                delete_filename = os.path.join(home, filename)
                os.remove(delete_filename)
                count += 1
                print(os.path.join(home, filename) + " 已删除...")
    print('共计删除文件：{}'.format(count))


if __name__ == '__main__':
    remove_file_in_dir(r"H:\视频", ['.downloading', '.cfg'])