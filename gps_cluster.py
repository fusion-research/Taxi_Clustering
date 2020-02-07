# -*- coding: utf-8 -*-

from read_on_down_data import *
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

on_down_path = "./on_down_dataset"

def cluster(m_eps, m_samples, arr):
    """
    :param m_eps:
    :param m_samples:
    :param arr:
    :return:
    """
    dbscan = DBSCAN(eps=m_eps, min_samples=m_samples, n_jobs=4, metric="euclidean", algorithm="auto").fit(arr)
    m_labels = dbscan.labels_
    return m_labels


def main():
    """
    :return:
    """
    on_arr, down_arr = read_data(on_down_path)
    cluster(0.005, 10, on_arr)
    cluster(0.005, 10, down_arr)
    plt.show()

if __name__ == '__main__':
    main()
