# -*- coding: utf-8 -*-

from read_on_down_data import *
from gps_cluster import cluster
from draw_shp import draw
import matplotlib.pyplot as plt
import numpy as np

shenzhen_data_dir = "./Shenzhen"
on_down_path = "./on_down_dataset"
colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "blanchedalmond", "blueviolet",
          "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson",
          "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen",
          "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkturquoise", "darkviolet",
          "deeppink", "deepskyblue", "dimgray", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro"]


def draw_on_cluster(pts, labels, base_pts, line_pts, m_makersize):
    """
    :param pts:
    :param labels:
    :param base_shp:
    :param m_makersize:
    :return:
    """
    index_0 = []
    index_1 = []
    index_2 = []
    index_3 = []
    index_4 = []
    index_5 = []
    index_6 = []
    index_7 = []
    index_8 = []
    index_9 = []
    index_10 = []
    index_11 = []
    index_12 = []
    index_13 = []
    index_14 = []
    index_15 = []
    index_16 = []
    index_17 = []
    index_18 = []
    index_19 = []
    index_20 = []
    index_21 = []
    index_22 = []
    index_23 = []
    index_24 = []
    index_25 = []
    index_25 = []
    index_26 = []
    index_27 = []
    index_28 = []
    index_29 = []
    index_30 = []
    index_31 = []
    labels = labels + 1
    for i in range(len(labels)):
        if labels[i] == 0:
            index_0.append(i)
        elif labels[i] == 1:
            index_1.append(i)
        elif labels[i] == 2:
            index_2.append(i)
        elif labels[i] == 3:
            index_3.append(i)
        elif labels[i] == 4:
            index_4.append(i)
        elif labels[i] == 5:
            index_5.append(i)
        elif labels[i] == 6:
            index_6.append(i)
        elif labels[i] == 7:
            index_7.append(i)
        elif labels[i] == 8:
            index_8.append(i)
        elif labels[i] == 9:
            index_9.append(i)
        elif labels[i] == 10:
            index_10.append(i)
        elif labels[i] == 11:
            index_11.append(i)
        elif labels[i] == 12:
            index_12.append(i)
        elif labels[i] == 13:
            index_13.append(i)
        elif labels[i] == 14:
            index_14.append(i)
        elif labels[i] == 15:
            index_15.append(i)
        elif labels[i] == 16:
            index_16.append(i)
        elif labels[i] == 17:
            index_17.append(i)
        elif labels[i] == 18:
            index_18.append(i)
        elif labels[i] == 19:
            index_19.append(i)
        elif labels[i] == 20:
            index_20.append(i)
        elif labels[i] == 21:
            index_21.append(i)
        elif labels[i] == 22:
            index_22.append(i)
        elif labels[i] == 23:
            index_23.append(i)
        elif labels[i] == 24:
            index_24.append(i)
        elif labels[i] == 25:
            index_25.append(i)
        elif labels[i] == 26:
            index_26.append(i)
        elif labels[i] == 27:
            index_27.append(i)
        elif labels[i] == 28:
            index_28.append(i)
        elif labels[i] == 29:
            index_29.append(i)
        elif labels[i] == 30:
            index_30.append(i)
        elif labels[i] == 31:
            index_31.append(i)
    base_shp = base_pts.plot(color="gray")
    # line_shp = line_pts.plot(color="darkgray", ax=base_shp)
    shp0 = pts[index_0].plot(color=colors[0], markersize=m_makersize, ax=base_shp)
    shp1 = pts[index_1].plot(color=colors[1], markersize=m_makersize, ax=shp0)
    shp2 = pts[index_2].plot(color=colors[2], markersize=m_makersize, ax=shp1)
    shp3 = pts[index_3].plot(color=colors[3], markersize=m_makersize, ax=shp2)
    shp4 = pts[index_4].plot(color=colors[4], markersize=m_makersize, ax=shp3)
    shp5 = pts[index_5].plot(color=colors[5], markersize=m_makersize, ax=shp4)
    shp6 = pts[index_6].plot(color=colors[6], markersize=m_makersize, ax=shp5)
    shp7 = pts[index_7].plot(color=colors[7], markersize=m_makersize, ax=shp6)
    shp8 = pts[index_8].plot(color=colors[8], markersize=m_makersize, ax=shp7)
    shp9 = pts[index_9].plot(color=colors[9], markersize=m_makersize, ax=shp8)
    shp10 = pts[index_10].plot(color=colors[10], markersize=m_makersize, ax=shp9)
    shp11 = pts[index_11].plot(color=colors[11], markersize=m_makersize, ax=shp10)
    shp12 = pts[index_12].plot(color=colors[12], markersize=m_makersize, ax=shp11)
    shp13 = pts[index_13].plot(color=colors[13], markersize=m_makersize, ax=shp12)
    shp14 = pts[index_14].plot(color=colors[14], markersize=m_makersize, ax=shp13)
    shp15 = pts[index_15].plot(color=colors[15], markersize=m_makersize, ax=shp14)
    shp16 = pts[index_16].plot(color=colors[16], markersize=m_makersize, ax=shp15)
    shp17 = pts[index_17].plot(color=colors[17], markersize=m_makersize, ax=shp16)
    shp18 = pts[index_18].plot(color=colors[18], markersize=m_makersize, ax=shp17)
    shp19 = pts[index_19].plot(color=colors[19], markersize=m_makersize, ax=shp18)
    shp20 = pts[index_20].plot(color=colors[20], markersize=m_makersize, ax=shp19)
    shp21 = pts[index_21].plot(color=colors[21], markersize=m_makersize, ax=shp20)
    shp22 = pts[index_22].plot(color=colors[22], markersize=m_makersize, ax=shp21)
    shp23 = pts[index_23].plot(color=colors[23], markersize=m_makersize, ax=shp22)
    shp24 = pts[index_24].plot(color=colors[24], markersize=m_makersize, ax=shp23)
    shp25 = pts[index_25].plot(color=colors[25], markersize=m_makersize, ax=shp24)
    shp26 = pts[index_26].plot(color=colors[26], markersize=m_makersize, ax=shp25)
    shp27 = pts[index_27].plot(color=colors[27], markersize=m_makersize, ax=shp26)
    shp28 = pts[index_28].plot(color=colors[28], markersize=m_makersize, ax=shp27)
    shp29 = pts[index_29].plot(color=colors[29], markersize=m_makersize, ax=shp28)
    shp30 = pts[index_30].plot(color=colors[30], markersize=m_makersize, ax=shp29)
    pts[index_31].plot(color=colors[31], markersize=m_makersize, ax=shp30)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Cluster result of distribution of Taxi pick-up GPS position in Shenzhen")


def draw_down_cluster(pts, labels, base_pts, line_pts, m_makersize):
    """
    :param arr:
    :param labels:
    :param base_shp:
    :param m_makersize:
    :return:
    """
    index_0 = []
    index_1 = []
    index_2 = []
    index_3 = []
    index_4 = []
    index_5 = []
    index_6 = []
    index_7 = []
    index_8 = []
    index_9 = []
    index_10 = []
    index_11 = []
    index_12 = []
    index_13 = []
    index_14 = []
    index_15 = []
    index_16 = []
    index_17 = []
    index_18 = []
    index_19 = []
    index_20 = []
    index_21 = []
    index_22 = []
    index_23 = []
    index_24 = []
    index_25 = []
    index_25 = []
    index_26 = []
    index_27 = []
    index_28 = []
    index_29 = []
    index_30 = []
    labels = labels + 1
    # print(len(labels))
    # print(labels[7])
    # print(labels[8])
    for i in range(len(labels)):
        if labels[i] == 0:
            index_0.append(i)
        elif labels[i] == 1:
            index_1.append(i)
        elif labels[i] == 2:
            index_2.append(i)
        elif labels[i] == 3:
            index_3.append(i)
        elif labels[i] == 4:
            index_4.append(i)
        elif labels[i] == 5:
            index_5.append(i)
        elif labels[i] == 6:
            index_6.append(i)
        elif labels[i] == 7:
            index_7.append(i)
        elif labels[i] == 8:
            index_8.append(i)
        elif labels[i] == 9:
            index_9.append(i)
        elif labels[i] == 10:
            index_10.append(i)
        elif labels[i] == 11:
            index_11.append(i)
        elif labels[i] == 12:
            index_12.append(i)
        elif labels[i] == 13:
            index_13.append(i)
        elif labels[i] == 14:
            index_14.append(i)
        elif labels[i] == 15:
            index_15.append(i)
        elif labels[i] == 16:
            index_16.append(i)
        elif labels[i] == 17:
            index_17.append(i)
        elif labels[i] == 18:
            index_18.append(i)
        elif labels[i] == 19:
            index_19.append(i)
        elif labels[i] == 20:
            index_20.append(i)
        elif labels[i] == 21:
            index_21.append(i)
        elif labels[i] == 22:
            index_22.append(i)
        elif labels[i] == 23:
            index_23.append(i)
        elif labels[i] == 24:
            index_24.append(i)
        elif labels[i] == 25:
            index_25.append(i)
        elif labels[i] == 26:
            index_26.append(i)
        elif labels[i] == 27:
            index_27.append(i)
        elif labels[i] == 28:
            index_28.append(i)
        elif labels[i] == 29:
            index_29.append(i)
        elif labels[i] == 30:
            index_30.append(i)
    base_shp = base_pts.plot(color="gray")
    # line_shp = line_pts.plot(color="darkgray", ax=base_shp)
    shp0 = pts[index_0].plot(color=colors[0], markersize=m_makersize, ax=base_shp)
    shp1 = pts[index_1].plot(color=colors[1], markersize=m_makersize, ax=shp0)
    shp2 = pts[index_2].plot(color=colors[2], markersize=m_makersize, ax=shp1)
    shp3 = pts[index_3].plot(color=colors[3], markersize=m_makersize, ax=shp2)
    shp4 = pts[index_4].plot(color=colors[4], markersize=m_makersize, ax=shp3)
    shp5 = pts[index_5].plot(color=colors[5], markersize=m_makersize, ax=shp4)
    shp6 = pts[index_6].plot(color=colors[6], markersize=m_makersize, ax=shp5)
    shp7 = pts[index_7].plot(color=colors[7], markersize=m_makersize, ax=shp6)
    shp8 = pts[index_8].plot(color=colors[8], markersize=m_makersize, ax=shp7)
    shp9 = pts[index_9].plot(color=colors[9], markersize=m_makersize, ax=shp8)
    shp10 = pts[index_10].plot(color=colors[10], markersize=m_makersize, ax=shp9)
    shp11 = pts[index_11].plot(color=colors[11], markersize=m_makersize, ax=shp10)
    shp12 = pts[index_12].plot(color=colors[12], markersize=m_makersize, ax=shp11)
    shp13 = pts[index_13].plot(color=colors[13], markersize=m_makersize, ax=shp12)
    shp14 = pts[index_14].plot(color=colors[14], markersize=m_makersize, ax=shp13)
    shp15 = pts[index_15].plot(color=colors[15], markersize=m_makersize, ax=shp14)
    shp16 = pts[index_16].plot(color=colors[16], markersize=m_makersize, ax=shp15)
    shp17 = pts[index_17].plot(color=colors[17], markersize=m_makersize, ax=shp16)
    shp18 = pts[index_18].plot(color=colors[18], markersize=m_makersize, ax=shp17)
    shp19 = pts[index_19].plot(color=colors[19], markersize=m_makersize, ax=shp18)
    shp20 = pts[index_20].plot(color=colors[20], markersize=m_makersize, ax=shp19)
    shp21 = pts[index_21].plot(color=colors[21], markersize=m_makersize, ax=shp20)
    shp22 = pts[index_22].plot(color=colors[22], markersize=m_makersize, ax=shp21)
    shp23 = pts[index_23].plot(color=colors[23], markersize=m_makersize, ax=shp22)
    shp24 = pts[index_24].plot(color=colors[24], markersize=m_makersize, ax=shp23)
    shp25 = pts[index_25].plot(color=colors[25], markersize=m_makersize, ax=shp24)
    shp26 = pts[index_26].plot(color=colors[26], markersize=m_makersize, ax=shp25)
    shp27 = pts[index_27].plot(color=colors[27], markersize=m_makersize, ax=shp26)
    shp28 = pts[index_28].plot(color=colors[28], markersize=m_makersize, ax=shp27)
    shp29 = pts[index_29].plot(color=colors[29], markersize=m_makersize, ax=shp28)
    pts[index_30].plot(color=colors[30], markersize=m_makersize, ax=shp29)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Cluster result of distribution of taxi drop-off GPS position in Shenzhen")


def draw_shenzhen_distribution(pts1, pts2, base_pts, line_pts):
    """
    :param pts1:
    :param pts2:
    :param base_shp:
    :return:
    """
    plt.rc("figure", figsize=(20, 10))
    base_shp = base_pts.plot(color="gray")
    # line_shp = line_pts.plot(color="darkgray", ax=base_shp)
    on_shp = pts1.plot(color="red", markersize=2., label="pick-up", ax=base_shp)
    pts2.plot(color="blue", markersize=2., label="drop-off", ax=on_shp)
    plt.legend()
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Distribution of Taxi GPS position in Shenzhen")


def main():
    """
    :return:
    """
    shp_dir = os.path.join(shenzhen_data_dir, "shenzhen.shp")
    link_dir = os.path.join(shenzhen_data_dir, "shenzhen-link.shp")
    shenzhen = gpd.GeoDataFrame.from_file(shp_dir, encoding="gb18030")
    line = gpd.GeoDataFrame.from_file(link_dir, encoding="gb18030")

    on_arr, down_arr = read_data(on_down_path)
    # base_map1 = draw(shenzhen_data_dir)
    # base_map2 = draw(shenzhen_data_dir)
    # base_map3 = draw(shenzhen_data_dir)

    on_pts = point_2_pts(on_arr)
    down_pts = point_2_pts(down_arr)
    draw_shenzhen_distribution(on_pts, down_pts, shenzhen, line)

    on_labels = cluster(0.005, 10, on_arr)
    print("on: there are {} clusters".format(len(set(on_labels))))
    down_labels = cluster(0.005, 10, down_arr)
    print("down: there are {} clusters".format(len(set(down_labels))))

    draw_on_cluster(on_pts, on_labels, shenzhen, line, 3)
    draw_down_cluster(down_pts, down_labels, shenzhen, line, 3)

    plt.show()


if __name__ == '__main__':
    main()