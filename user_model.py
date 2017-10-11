# -*- coding: utf-8 -*-

"""
User Model
"""

from data_process import User, process_product_info


def extract_features_from_product(products):
    """
    从商品中提取出人物特征：

    1. 综合特征(包含用户喜好、倾向)
    2. 用户消费水平
    3. 用户购物频率
    :param products:
    :return:
    """
    product_1 = products[0][0]#浏览的商品
    product_2 = products[1][0]#收藏
    product_3 = products[2][0]#加购
    product_4 = products[3][0]#购买

    feature = []
    return feature


def build_user_features(user, products_dict):

    """
    用户特征: 商品特征+固有特征 [商品成分分析] + [购物等级、贫富、孩子年龄，孩子性别]
    :return:
    """
    products = products_dict[user.id]
    #用户自己的信息构建的特征
    user_feature = [user.id, user.rank, user.hasbaby, user.baby_age, user.baby_gender]
    #根据用户买的商品的信息作为特征
    feature_from_product = extract_features_from_product(products)
    feature = user_feature + feature_from_product
    return feature



