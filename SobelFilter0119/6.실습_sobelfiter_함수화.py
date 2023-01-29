import numpy as np
import matplotlib.pyp as plt
# step0 test 이미지 만들기
# def get_check_pattern_img():
#     white_patch = 1*np.ones(shape=(10, 10))
#     black_patch = 0*np.ones(shape=(10, 10))
#
#     img1 = np.hstack([white_patch, black_patch])
#     img2 = np.hstack([black_patch, white_patch])
#     img = np.vstack([img1, img2])
#
#     img = np.tile(img, reps=[2, 2])
#     return img
#
# # step2 soble fittering
#
# filter_ = np.array([[-1, 0, 1],
#                     [-2, 0, 2],
#                     [-1, 0, 1]])
#
# F = filter_.shape[0]
# H_ = H - F + 1
# W_ = W - F + 1
#
# for h_idx in range(H_)