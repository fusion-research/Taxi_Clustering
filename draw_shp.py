# -*- coding: utf-8 -*-

import geopandas as gpd
import os
import matplotlib.pyplot as plt

path = "./Shenzhen"

def draw(base_dir):
    """
    :param base_dir:
    :return:
    """
    shp_dir = os.path.join(base_dir, "shenzhen.shp")
    link_dir = os.path.join(base_dir, "shenzhen-link.shp")
    if not os.path.exists(shp_dir):
        print("base file is not exists...")
        exit(-1)
    shenzhen = gpd.GeoDataFrame.from_file(shp_dir, encoding="gb18030")
    line = gpd.GeoDataFrame.from_file(link_dir, encoding="gb18030")
    plt.rc("figure", figsize=(20, 10))
    base_shp = shenzhen.plot(color="gray")
    line_shp = line.plot(color="darkgray", ax=base_shp)
    return line_shp


def main():
    """
    :return:
    """
    draw(path)


if __name__ == '__main__':
    main()
