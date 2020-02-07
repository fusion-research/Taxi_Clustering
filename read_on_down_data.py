# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
from shapely.geometry import Point
import geopandas as gpd

on_down_path = "./on_down_dataset"

def cheack_nan(arr):
    for i in range(len(arr)):
        sample = arr[i]
        for j in range(len(sample)):
            if np.isnan(sample[j]):
                print(i)


def read_data(base_dir):
    """
    :param base_dir:
    :return:
    """
    on_dir = os.path.join(on_down_path, "on")
    down_dir = os.path.join(on_down_path, "down")
    on_flag = down_flag = 0

    on_names = os.listdir(on_dir)
    down_names = os.listdir(down_dir)

    path1 = os.path.join(down_dir, down_names[0])
    qqq = pd.read_csv(path1).values
    qqqq = qqq[:, 1:].astype(float)
    on_arr = np.zeros(qqqq.shape)
    for on_name in on_names:
        if on_name == ".DS_Store":
            pass
        else:
            on_path = os.path.join(on_dir, on_name)
            tmp = pd.read_csv(on_path).values
            tmp1 = tmp[:, 1:].astype(float)
            if on_flag == 0:
                on_arr = tmp1
                on_flag = 1
            else:
                on_arr = np.vstack((on_arr, tmp1))

    path2 = os.path.join(down_dir, down_names[0])
    ppp = pd.read_csv(path2).values
    pppp = ppp[:, 1:].astype(float)
    down_arr = np.zeros(pppp.shape)
    for down_name in down_names:
        if down_name == ".DS_Store":
            pass
        else:
            # print("down_name: ", down_name)
            down_path = os.path.join(down_dir, down_name)
            tmp = pd.read_csv(down_path).values
            tmp1 = tmp[:, 1:].astype(float)
            # cheack_nan(tmp1)
            if down_flag == 0:
                down_arr = tmp1
                down_flag = 1
            else:
                down_arr = np.vstack((down_arr, tmp1))

    # 随机各选取30%数据
    on_index_arr = np.arange(on_arr.shape[0])
    down_index_arr = np.arange(down_arr.shape[0])
    rdn = np.random.RandomState(666)
    rdn.shuffle(on_index_arr)
    rdn.shuffle(down_index_arr)

    return on_arr[on_index_arr[0:int(0.01*len(on_index_arr))]], down_arr[down_index_arr[0:int(0.01*len(down_index_arr))]]


def point_2_pts(arr):
    """
    :param arr:
    :return:
    """
    pts = gpd.GeoSeries([Point(x, y) for x, y in zip(arr[:, 0], arr[:, 1])])
    return pts


def main():
    read_data(on_down_path)


if __name__ == '__main__':
    main()



