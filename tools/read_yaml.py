# -*- coding:utf-8 -*-
import yaml
from config import BASE_PATH
import os


def read_yaml(filename):
    filepath = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(filepath, "r", encoding="utf-8") as f:
        arrs = []
        for data in yaml.safe_load(f).values():
            arrs.append(tuple(data.values()))
        return arrs

if __name__ == '__main__':
    print(read_yaml("pc_demo_detail.yaml"))