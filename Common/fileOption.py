# !/user/bin/env python

import os


class File_option:
    @staticmethod
    def file_mkdir(filepath):
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        else:
            print("{}目录已存在，不需要再次创建".format(filepath))

