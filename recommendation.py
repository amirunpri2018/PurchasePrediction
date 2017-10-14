# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')
import logging
import os.path
import sys
import multiprocessing
# from gensim.models.word2vec import LineSentence
# from gensim.models import Word2Vec
import numpy as np
from scipy.spatial.distance import cosine
from data_process import process_user_info
from behavior_analysis import process_user_behaviors, filter_time, write_to_file, date_to_timestamp
from product_analysis import get_similarity






# def similarity_embedding(embed_a, embed_b):
#     """
#     获得相似度 / embedding 特征
#     :param embed_a:
#     :param embed_b:
#     :return:
#     """
#     if __name__ == '__main__':
#         program=os.path.basename(sys.argv[0])
#         logger=logging.getLogger(program)
#         logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
#         logger.info('running %s'%' '.join(sys.argv))
#         fdir='Desktop/data/'
#         inp=fdir+'data.txt'
#         outp1=fdir+'text.model'
#         outp2=fdir+'text.vector'
#         model=Word2Vec(LineSentence(inp),size=400,window=5,min_count=5,workers=multiprocessing.cpu_count())
#         model.save(outp1)
#         mdoel.wv.save_word2vec_format(outp2,binary=False)
#
#     '''
#         calculate cosine
#
#     '''
#
#     return get_similarity(embed_a, embed_b)


def similarity_person_self(self_a, self_b):
    """
    固有特征
    :param self_a:
    :param self_b:
    :return:
    """
    self_a = np.array(self_a)
    self_b = np.array(self_b)
    return get_similarity(self_a, self_b)


def cf_product_based(all_products, user_product):

    """
    Collaborative Filtering: Product Based (基于商品的协同过滤推荐)
    :param all_products: 所有商品
    :param user_product: 用户已购买或者加购的商品
    :return:
    """

    pass


def cf_person_based(rank, user_dict):
    """
    基于人的协同过滤
    :rank: 选取rank名相似用户进行推荐
    :return:
    """
    def sim(person_a, person_b):

        return 0

    users = process_user_info()

    num_user = len(users)

    person_similarity_matrix = np.zeros((num_user, num_user))

    for i in range(num_user):
        for j in range(num_user):
            person_similarity_matrix[i][j] = sim(user_dict[users[i].user_id], user_dict[users[j].user_id])

    pass


def gen_recommendation_data1():

    predicted_data = []

    action_1 = process_user_behaviors('data/behaviors/action_1.txt')

    start_time = "2017-8-23 00:00:00"
    end_time = -1

    predicted_data += filter_time(action_1,  date_to_timestamp(start_time), end_time)

    print(len(predicted_data))

    action_2 = process_user_behaviors('data/behaviors/action_2.txt')

    start_time = "2017-8-19 00:00:00"
    end_time = -1

    predicted_data += filter_time(action_2, date_to_timestamp(start_time), end_time)
    print(len(predicted_data))

    action_3 = process_user_behaviors('data/behaviors/action_3.txt')

    start_time = "2017-8-18 00:00:00"
    end_time = -1

    predicted_data += filter_time(action_3,  date_to_timestamp(start_time), end_time)

    print(len(predicted_data))

    action_4 = process_user_behaviors('data/behaviors/action_4.txt')

    start_time = "2017-8-22 00:00:00"
    end_time = -1

    predicted_data += filter_time(action_4,  date_to_timestamp(start_time), end_time)

    print(len(predicted_data))

    write_to_file(predicted_data, 'data/predict.txt')


if __name__ == '__main__':

    #gen_recommendation_data()
