import numpy as np 

multiplication_table = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [1, 0, 3, 2, 6, 7, 4, 5, 11, 10, 9, 8, 13, 12, 15, 14, 19, 18, 17, 16, 22, 23, 20, 21], [2, 3, 0, 1, 5, 4, 7, 6, 10, 11, 8, 9, 15, 14, 13, 12, 17, 16, 19, 18, 23, 22, 21, 20], [3, 2, 1, 0, 7, 6, 5, 4, 9, 8, 11, 10, 14, 15, 12, 13, 18, 19, 16, 17, 21, 20, 23, 22], [4, 5, 6, 7, 0, 1, 2, 3, 20, 21, 22, 23, 16, 17, 18, 19, 12, 13, 14, 15, 8, 9, 10, 11], [5, 4, 7, 6, 2, 3, 0, 1, 23, 22, 21, 20, 17, 16, 19, 18, 15, 14, 13, 12, 10, 11, 8, 9], [6, 7, 4, 5, 1, 0, 3, 2, 22, 23, 20, 21, 19, 18, 17, 16, 13, 12, 15, 14, 11, 10, 9, 8], [7, 6, 5, 4, 3, 2, 1, 0, 21, 20, 23, 22, 18, 19, 16, 17, 14, 15, 12, 13, 9, 8, 11, 10], [8, 9, 10, 11, 16, 17, 18, 19, 0, 1, 2, 3, 20, 21, 22, 23, 4, 5, 6, 7, 12, 13, 14, 15], [9, 8, 11, 10, 18, 19, 16, 17, 3, 2, 1, 0, 21, 20, 23, 22, 7, 6, 5, 4, 14, 15, 12, 13], [10, 11, 8, 9, 17, 16, 19, 18, 2, 3, 0, 1, 23, 22, 21, 20, 5, 4, 7, 6, 15, 14, 13, 12], [11, 10, 9, 8, 19, 18, 17, 16, 1, 0, 3, 2, 22, 23, 20, 21, 6, 7, 4, 5, 13, 12, 15, 14], [12, 13, 14, 15, 20, 21, 22, 23, 16, 17, 18, 19, 0, 1, 2, 3, 8, 9, 10, 11, 4, 5, 6, 7], [13, 12, 15, 14, 22, 23, 20, 21, 19, 18, 17, 16, 1, 0, 3, 2, 11, 10, 9, 8, 6, 7, 4, 5], [14, 15, 12, 13, 21, 20, 23, 22, 18, 19, 16, 17, 3, 2, 1, 0, 9, 8, 11, 10, 7, 6, 5, 4], [15, 14, 13, 12, 23, 22, 21, 20, 17, 16, 19, 18, 2, 3, 0, 1, 10, 11, 8, 9, 5, 4, 7, 6], [16, 17, 18, 19, 8, 9, 10, 11, 12, 13, 14, 15, 4, 5, 6, 7, 20, 21, 22, 23, 0, 1, 2, 3], [17, 16, 19, 18, 10, 11, 8, 9, 15, 14, 13, 12, 5, 4, 7, 6, 23, 22, 21, 20, 2, 3, 0, 1], [18, 19, 16, 17, 9, 8, 11, 10, 14, 15, 12, 13, 7, 6, 5, 4, 21, 20, 23, 22, 3, 2, 1, 0], [19, 18, 17, 16, 11, 10, 9, 8, 13, 12, 15, 14, 6, 7, 4, 5, 22, 23, 20, 21, 1, 0, 3, 2], [20, 21, 22, 23, 12, 13, 14, 15, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 16, 17, 18, 19], [21, 20, 23, 22, 14, 15, 12, 13, 7, 6, 5, 4, 9, 8, 11, 10, 3, 2, 1, 0, 18, 19, 16, 17], [22, 23, 20, 21, 13, 12, 15, 14, 6, 7, 4, 5, 11, 10, 9, 8, 1, 0, 3, 2, 19, 18, 17, 16], [23, 22, 21, 20, 15, 14, 13, 12, 5, 4, 7, 6, 10, 11, 8, 9, 2, 3, 0, 1, 17, 16, 19, 18]], dtype=int)
decomposition_table = ["XXXX", "XX", "ZZXX", "ZZ", "ZXX", "Z", "ZZZ", "XXZ", "XZX", "XZXXX", "XZZZX", "XXXZX", "XZZ", "ZZX", "XXX", "X", "ZZZX", "XXZX", "ZX", "ZXXX", "XXXZ", "XZZZ", "XZ", "XZXX"]
cz_table = np.array([[[[1, 0, 0], [1, 0, 0], [1, 0, 3], [1, 0, 3], [1, 0, 5], [1, 0, 5], [1, 0, 6], [1, 0, 6], [0, 3, 8], [0, 3, 8], [0, 0, 10], [0, 0, 10], [1, 0, 3], [1, 0, 3], [1, 0, 0], [1, 0, 0], [1, 0, 6], [1, 0, 6], [1, 0, 5], [1, 0, 5], [0, 0, 10], [0, 0, 10], [0, 3, 8], [0, 3, 8]], [[1, 0, 0], [1, 0, 0], [1, 0, 3], [1, 0, 3], [1, 0, 5], [1, 0, 5], [1, 0, 6], [1, 0, 6], [0, 2, 8], [0, 2, 8], [0, 0, 10], [0, 0, 10], [1, 0, 3], [1, 0, 3], [1, 0, 0], [1, 0, 0], [1, 0, 6], [1, 0, 6], [1, 0, 5], [1, 0, 5], [0, 0, 10], [0, 0, 10], [0, 2, 8], [0, 2, 8]], [[1, 3, 0], [1, 3, 0], [1, 2, 0], [1, 2, 0], [1, 0, 4], [1, 2, 6], [1, 2, 5], [1, 0, 7], [0, 0, 8], [0, 0, 8], [0, 2, 10], [0, 2, 10], [1, 0, 2], [1, 0, 2], [1, 0, 1], [1, 0, 1], [1, 0, 7], [1, 0, 7], [1, 0, 4], [1, 0, 4], [0, 2, 10], [0, 2, 10], [0, 0, 8], [0, 0, 8]], [[1, 3, 0], [1, 3, 0], [1, 0, 2], [1, 3, 3], [1, 0, 4], [1, 3, 5], [1, 3, 6], [1, 0, 7], [0, 0, 8], [0, 0, 8], [0, 3, 10], [0, 3, 10], [1, 0, 2], [1, 0, 2], [1, 0, 1], [1, 0, 1], [1, 0, 7], [1, 0, 7], [1, 0, 4], [1, 0, 4], [0, 3, 10], [0, 3, 10], [0, 0, 8], [0, 0, 8]], [[1, 5, 0], [1, 5, 0], [1, 4, 0], [1, 4, 0], [1, 19, 0], [1, 4, 6], [1, 4, 5], [1, 0, 17], [0, 6, 8], [0, 6, 8], [0, 4, 10], [0, 4, 10], [1, 0, 12], [1, 0, 12], [1, 0, 14], [1, 0, 14], [1, 0, 17], [1, 0, 17], [1, 0, 19], [1, 0, 19], [0, 4, 10], [0, 4, 10], [0, 6, 8], [0, 6, 8]], [[1, 5, 0], [1, 5, 0], [1, 6, 2], [1, 5, 3], [1, 6, 4], [1, 5, 5], [1, 5, 6], [1, 0, 17], [0, 6, 8], [0, 6, 8], [0, 5, 10], [0, 5, 10], [1, 0, 12], [1, 0, 12], [1, 0, 14], [1, 0, 14], [1, 0, 17], [1, 0, 17], [1, 0, 19], [1, 0, 19], [0, 5, 10], [0, 5, 10], [0, 6, 8], [0, 6, 8]], [[1, 6, 0], [1, 6, 0], [1, 5, 2], [1, 6, 3], [1, 5, 4], [1, 6, 5], [1, 6, 6], [1, 0, 16], [0, 5, 8], [0, 5, 8], [0, 6, 10], [0, 6, 10], [1, 0, 13], [1, 0, 13], [1, 0, 15], [1, 0, 15], [1, 0, 16], [1, 0, 16], [1, 0, 18], [1, 0, 18], [0, 6, 10], [0, 6, 10], [0, 5, 8], [0, 5, 8]], [[1, 6, 0], [1, 6, 0], [1, 7, 0], [1, 7, 0], [1, 17, 0], [1, 17, 0], [1, 16, 0], [1, 16, 0], [0, 4, 8], [0, 4, 8], [0, 6, 10], [0, 6, 10], [1, 0, 13], [1, 0, 13], [1, 0, 15], [1, 0, 15], [1, 0, 16], [1, 0, 16], [1, 0, 18], [1, 0, 18], [0, 6, 10], [0, 6, 10], [0, 4, 8], [0, 4, 8]], [[0, 8, 3], [0, 8, 2], [0, 8, 0], [0, 8, 0], [0, 8, 6], [0, 8, 6], [0, 8, 5], [0, 8, 4], [0, 8, 8], [0, 8, 8], [0, 8, 10], [0, 8, 10], [0, 8, 0], [0, 8, 0], [0, 8, 2], [0, 8, 2], [0, 8, 4], [0, 8, 4], [0, 8, 6], [0, 8, 6], [0, 8, 10], [0, 8, 10], [0, 8, 8], [0, 8, 8]], [[0, 8, 3], [0, 8, 2], [0, 8, 0], [0, 8, 0], [0, 8, 6], [0, 8, 6], [0, 8, 5], [0, 8, 4], [0, 8, 8], [0, 8, 8], [0, 8, 10], [0, 8, 10], [0, 8, 0], [0, 8, 0], [0, 8, 2], [0, 8, 2], [0, 8, 4], [0, 8, 4], [0, 8, 6], [0, 8, 6], [0, 8, 10], [0, 8, 10], [0, 8, 8], [0, 8, 8]], [[0, 10, 0], [0, 10, 0], [0, 10, 2], [0, 10, 3], [0, 10, 4], [0, 10, 5], [0, 10, 6], [0, 10, 6], [0, 10, 8], [0, 10, 8], [0, 10, 10], [0, 10, 10], [0, 10, 2], [0, 10, 2], [0, 10, 0], [0, 10, 0], [0, 10, 6], [0, 10, 6], [0, 10, 4], [0, 10, 4], [0, 10, 10], [0, 10, 10], [0, 10, 8], [0, 10, 8]], [[0, 10, 0], [0, 10, 0], [0, 10, 2], [0, 10, 3], [0, 10, 4], [0, 10, 5], [0, 10, 6], [0, 10, 6], [0, 10, 8], [0, 10, 8], [0, 10, 10], [0, 10, 10], [0, 10, 2], [0, 10, 2], [0, 10, 0], [0, 10, 0], [0, 10, 6], [0, 10, 6], [0, 10, 4], [0, 10, 4], [0, 10, 10], [0, 10, 10], [0, 10, 8], [0, 10, 8]], [[1, 3, 0], [1, 3, 0], [1, 2, 0], [1, 2, 0], [1, 12, 0], [1, 12, 0], [1, 13, 0], [1, 13, 0], [0, 0, 8], [0, 0, 8], [0, 2, 10], [0, 2, 10], [1, 2, 0], [1, 0, 2], [1, 0, 1], [1, 0, 1], [1, 0, 7], [1, 0, 7], [1, 0, 4], [1, 0, 4], [0, 2, 10], [0, 2, 10], [0, 0, 8], [0, 0, 8]], [[1, 3, 0], [1, 3, 0], [1, 2, 0], [1, 2, 0], [1, 12, 0], [1, 12, 0], [1, 13, 0], [1, 13, 0], [0, 0, 8], [0, 0, 8], [0, 2, 10], [0, 2, 10], [1, 2, 0], [1, 2, 0], [1, 0, 1], [1, 0, 1], [1, 0, 7], [1, 0, 7], [1, 0, 4], [1, 0, 4], [0, 2, 10], [0, 2, 10], [0, 0, 8], [0, 0, 8]], [[1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 14, 0], [1, 14, 0], [1, 15, 0], [1, 15, 0], [0, 2, 8], [0, 2, 8], [0, 0, 10], [0, 0, 10], [1, 1, 0], [1, 1, 0], [1, 0, 0], [1, 0, 0], [1, 0, 6], [1, 0, 6], [1, 0, 5], [1, 0, 5], [0, 0, 10], [0, 0, 10], [0, 2, 8], [0, 2, 8]], [[1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 14, 0], [1, 14, 0], [1, 15, 0], [1, 15, 0], [0, 2, 8], [0, 2, 8], [0, 0, 10], [0, 0, 10], [1, 1, 0], [1, 1, 0], [1, 0, 0], [1, 0, 0], [1, 0, 6], [1, 0, 6], [1, 0, 5], [1, 0, 5], [0, 0, 10], [0, 0, 10], [0, 2, 8], [0, 2, 8]], [[1, 6, 0], [1, 6, 0], [1, 7, 0], [1, 7, 0], [1, 17, 0], [1, 17, 0], [1, 16, 0], [1, 16, 0], [0, 4, 8], [0, 4, 8], [0, 6, 10], [0, 6, 10], [1, 7, 0], [1, 7, 0], [1, 6, 0], [1, 6, 0], [1, 16, 0], [1, 0, 16], [1, 0, 18], [1, 0, 18], [0, 6, 10], [0, 6, 10], [0, 4, 8], [0, 4, 8]], [[1, 6, 0], [1, 6, 0], [1, 7, 0], [1, 7, 0], [1, 17, 0], [1, 17, 0], [1, 16, 0], [1, 16, 0], [0, 4, 8], [0, 4, 8], [0, 6, 10], [0, 6, 10], [1, 7, 0], [1, 7, 0], [1, 6, 0], [1, 6, 0], [1, 16, 0], [1, 16, 0], [1, 0, 18], [1, 0, 18], [0, 6, 10], [0, 6, 10], [0, 4, 8], [0, 4, 8]], [[1, 5, 0], [1, 5, 0], [1, 4, 0], [1, 4, 0], [1, 19, 0], [1, 19, 0], [1, 18, 0], [1, 18, 0], [0, 6, 8], [0, 6, 8], [0, 4, 10], [0, 4, 10], [1, 4, 0], [1, 4, 0], [1, 5, 0], [1, 5, 0], [1, 18, 0], [1, 18, 0], [1, 19, 0], [1, 0, 19], [0, 4, 10], [0, 4, 10], [0, 6, 8], [0, 6, 8]], [[1, 5, 0], [1, 5, 0], [1, 4, 0], [1, 4, 0], [1, 19, 0], [1, 19, 0], [1, 18, 0], [1, 18, 0], [0, 6, 8], [0, 6, 8], [0, 4, 10], [0, 4, 10], [1, 4, 0], [1, 4, 0], [1, 5, 0], [1, 5, 0], [1, 18, 0], [1, 18, 0], [1, 19, 0], [1, 19, 0], [0, 4, 10], [0, 4, 10], [0, 6, 8], [0, 6, 8]], [[0, 10, 0], [0, 10, 0], [0, 10, 2], [0, 10, 3], [0, 10, 4], [0, 10, 5], [0, 10, 6], [0, 10, 6], [0, 10, 8], [0, 10, 8], [0, 10, 10], [0, 10, 10], [0, 10, 2], [0, 10, 2], [0, 10, 0], [0, 10, 0], [0, 10, 6], [0, 10, 6], [0, 10, 4], [0, 10, 4], [0, 10, 10], [0, 10, 10], [0, 10, 8], [0, 10, 8]], [[0, 10, 0], [0, 10, 0], [0, 10, 2], [0, 10, 3], [0, 10, 4], [0, 10, 5], [0, 10, 6], [0, 10, 6], [0, 10, 8], [0, 10, 8], [0, 10, 10], [0, 10, 10], [0, 10, 2], [0, 10, 2], [0, 10, 0], [0, 10, 0], [0, 10, 6], [0, 10, 6], [0, 10, 4], [0, 10, 4], [0, 10, 10], [0, 10, 10], [0, 10, 8], [0, 10, 8]], [[0, 8, 3], [0, 8, 2], [0, 8, 0], [0, 8, 0], [0, 8, 6], [0, 8, 6], [0, 8, 5], [0, 8, 4], [0, 8, 8], [0, 8, 8], [0, 8, 10], [0, 8, 10], [0, 8, 0], [0, 8, 0], [0, 8, 2], [0, 8, 2], [0, 8, 4], [0, 8, 4], [0, 8, 6], [0, 8, 6], [0, 8, 10], [0, 8, 10], [0, 8, 8], [0, 8, 8]], [[0, 8, 3], [0, 8, 2], [0, 8, 0], [0, 8, 0], [0, 8, 6], [0, 8, 6], [0, 8, 5], [0, 8, 4], [0, 8, 8], [0, 8, 8], [0, 8, 10], [0, 8, 10], [0, 8, 0], [0, 8, 0], [0, 8, 2], [0, 8, 2], [0, 8, 4], [0, 8, 4], [0, 8, 6], [0, 8, 6], [0, 8, 10], [0, 8, 10], [0, 8, 8], [0, 8, 8]]], [[[0, 0, 0], [0, 3, 0], [0, 3, 2], [0, 0, 3], [0, 3, 4], [0, 0, 5], [0, 0, 6], [0, 3, 6], [1, 0, 8], [1, 0, 9], [1, 0, 11], [1, 0, 10], [0, 5, 2], [0, 6, 2], [0, 5, 0], [0, 6, 0], [0, 6, 6], [0, 5, 6], [0, 6, 4], [0, 5, 4], [1, 0, 21], [1, 0, 20], [1, 0, 22], [1, 0, 23]], [[0, 0, 3], [0, 2, 2], [0, 2, 0], [0, 0, 0], [0, 2, 6], [0, 0, 6], [0, 0, 5], [0, 2, 4], [1, 0, 10], [1, 0, 11], [1, 0, 9], [1, 0, 8], [0, 6, 0], [0, 4, 0], [0, 6, 2], [0, 4, 2], [0, 4, 4], [0, 6, 4], [0, 4, 6], [0, 6, 6], [1, 0, 23], [1, 0, 22], [1, 0, 20], [1, 0, 21]], [[0, 2, 3], [0, 0, 2], [0, 0, 0], [0, 2, 0], [0, 0, 6], [0, 2, 6], [0, 2, 5], [0, 0, 4], [1, 0, 11], [1, 0, 10], [1, 0, 8], [1, 0, 9], [0, 4, 0], [0, 6, 0], [0, 4, 2], [0, 6, 2], [0, 6, 4], [0, 4, 4], [0, 6, 6], [0, 4, 6], [1, 0, 22], [1, 0, 23], [1, 0, 21], [1, 0, 20]], [[0, 3, 0], [0, 0, 0], [0, 0, 2], [0, 3, 3], [0, 0, 4], [0, 3, 5], [0, 3, 6], [0, 0, 6], [1, 0, 9], [1, 0, 8], [1, 0, 10], [1, 0, 11], [0, 6, 2], [0, 5, 2], [0, 6, 0], [0, 5, 0], [0, 5, 6], [0, 6, 6], [0, 5, 4], [0, 6, 4], [1, 0, 20], [1, 0, 21], [1, 0, 23], [1, 0, 22]], [[0, 4, 3], [0, 6, 2], [0, 6, 0], [0, 4, 0], [0, 6, 6], [0, 4, 6], [0, 4, 5], [0, 6, 4], [1, 0, 21], [1, 0, 20], [1, 0, 23], [1, 0, 22], [0, 0, 0], [0, 2, 0], [0, 0, 2], [0, 2, 2], [0, 2, 4], [0, 0, 4], [0, 2, 6], [0, 0, 6], [1, 0, 8], [1, 0, 9], [1, 0, 10], [1, 0, 11]], [[0, 5, 0], [0, 6, 0], [0, 6, 2], [0, 5, 3], [0, 6, 4], [0, 5, 5], [0, 5, 6], [0, 6, 6], [1, 0, 22], [1, 0, 23], [1, 0, 20], [1, 0, 21], [0, 3, 2], [0, 0, 2], [0, 3, 0], [0, 0, 0], [0, 0, 6], [0, 3, 6], [0, 0, 4], [0, 3, 4], [1, 0, 11], [1, 0, 10], [1, 0, 9], [1, 0, 8]], [[0, 6, 0], [0, 5, 0], [0, 5, 2], [0, 6, 3], [0, 5, 4], [0, 6, 5], [0, 6, 6], [0, 5, 6], [1, 0, 23], [1, 0, 22], [1, 0, 21], [1, 0, 20], [0, 0, 2], [0, 3, 2], [0, 0, 0], [0, 3, 0], [0, 3, 6], [0, 0, 6], [0, 3, 4], [0, 0, 4], [1, 0, 10], [1, 0, 11], [1, 0, 8], [1, 0, 9]], [[0, 6, 3], [0, 4, 2], [0, 4, 0], [0, 6, 0], [0, 4, 6], [0, 6, 6], [0, 6, 5], [0, 4, 4], [1, 0, 20], [1, 0, 21], [1, 0, 22], [1, 0, 23], [0, 2, 0], [0, 0, 0], [0, 2, 2], [0, 0, 2], [0, 0, 4], [0, 2, 4], [0, 0, 6], [0, 2, 6], [1, 0, 9], [1, 0, 8], [1, 0, 11], [1, 0, 10]], [[1, 8, 0], [1, 10, 0], [1, 11, 0], [1, 9, 0], [1, 21, 0], [1, 22, 0], [1, 23, 0], [1, 20, 0], [0, 0, 0], [0, 0, 2], [0, 2, 2], [0, 2, 0], [0, 6, 6], [0, 4, 4], [0, 6, 4], [0, 4, 6], [0, 4, 2], [0, 6, 0], [0, 4, 0], [0, 6, 2], [0, 2, 4], [0, 2, 6], [0, 0, 6], [0, 0, 4]], [[1, 9, 0], [1, 11, 0], [1, 10, 0], [1, 8, 0], [1, 20, 0], [1, 23, 0], [1, 22, 0], [1, 21, 0], [0, 2, 0], [0, 2, 2], [0, 0, 2], [0, 0, 0], [0, 4, 6], [0, 6, 4], [0, 4, 4], [0, 6, 6], [0, 6, 2], [0, 4, 0], [0, 6, 0], [0, 4, 2], [0, 0, 4], [0, 0, 6], [0, 2, 6], [0, 2, 4]], [[1, 11, 0], [1, 9, 0], [1, 8, 0], [1, 10, 0], [1, 23, 0], [1, 20, 0], [1, 21, 0], [1, 22, 0], [0, 2, 2], [0, 2, 0], [0, 0, 0], [0, 0, 2], [0, 6, 4], [0, 4, 6], [0, 6, 6], [0, 4, 4], [0, 4, 0], [0, 6, 2], [0, 4, 2], [0, 6, 0], [0, 0, 6], [0, 0, 4], [0, 2, 4], [0, 2, 6]], [[1, 10, 0], [1, 8, 0], [1, 9, 0], [1, 11, 0], [1, 22, 0], [1, 21, 0], [1, 20, 0], [1, 23, 0], [0, 0, 2], [0, 0, 0], [0, 2, 0], [0, 2, 2], [0, 4, 4], [0, 6, 6], [0, 4, 6], [0, 6, 4], [0, 6, 0], [0, 4, 2], [0, 6, 2], [0, 4, 0], [0, 2, 6], [0, 2, 4], [0, 0, 4], [0, 0, 6]], [[0, 2, 5], [0, 0, 6], [0, 0, 4], [0, 2, 6], [0, 0, 0], [0, 2, 3], [0, 2, 0], [0, 0, 2], [0, 6, 6], [0, 6, 4], [0, 4, 6], [0, 4, 4], [1, 21, 0], [1, 0, 22], [1, 0, 20], [1, 0, 23], [1, 0, 8], [1, 0, 11], [1, 0, 9], [1, 0, 10], [0, 4, 2], [0, 4, 0], [0, 6, 2], [0, 6, 0]], [[0, 2, 6], [0, 0, 4], [0, 0, 6], [0, 2, 5], [0, 0, 2], [0, 2, 0], [0, 2, 3], [0, 0, 0], [0, 4, 4], [0, 4, 6], [0, 6, 4], [0, 6, 6], [1, 22, 0], [1, 20, 0], [1, 0, 22], [1, 0, 21], [1, 0, 10], [1, 0, 9], [1, 0, 11], [1, 0, 8], [0, 6, 0], [0, 6, 2], [0, 4, 0], [0, 4, 2]], [[0, 0, 5], [0, 2, 6], [0, 2, 4], [0, 0, 6], [0, 2, 0], [0, 0, 3], [0, 0, 0], [0, 2, 2], [0, 4, 6], [0, 4, 4], [0, 6, 6], [0, 6, 4], [1, 20, 0], [1, 22, 0], [1, 21, 0], [1, 0, 22], [1, 0, 9], [1, 0, 10], [1, 0, 8], [1, 0, 11], [0, 6, 2], [0, 6, 0], [0, 4, 2], [0, 4, 0]], [[0, 0, 6], [0, 2, 4], [0, 2, 6], [0, 0, 5], [0, 2, 2], [0, 0, 0], [0, 0, 3], [0, 2, 0], [0, 6, 4], [0, 6, 6], [0, 4, 4], [0, 4, 6], [1, 23, 0], [1, 21, 0], [1, 22, 0], [1, 20, 0], [1, 0, 11], [1, 0, 8], [1, 0, 10], [1, 0, 9], [0, 4, 0], [0, 4, 2], [0, 6, 0], [0, 6, 2]], [[0, 6, 6], [0, 4, 4], [0, 4, 6], [0, 6, 5], [0, 4, 2], [0, 6, 0], [0, 6, 3], [0, 4, 0], [0, 2, 4], [0, 2, 6], [0, 0, 4], [0, 0, 6], [1, 8, 0], [1, 10, 0], [1, 9, 0], [1, 11, 0], [1, 21, 0], [1, 0, 23], [1, 0, 20], [1, 0, 22], [0, 0, 0], [0, 0, 2], [0, 2, 0], [0, 2, 2]], [[0, 6, 5], [0, 4, 6], [0, 4, 4], [0, 6, 6], [0, 4, 0], [0, 6, 3], [0, 6, 0], [0, 4, 2], [0, 0, 6], [0, 0, 4], [0, 2, 6], [0, 2, 4], [1, 11, 0], [1, 9, 0], [1, 10, 0], [1, 8, 0], [1, 23, 0], [1, 20, 0], [1, 0, 23], [1, 0, 21], [0, 2, 2], [0, 2, 0], [0, 0, 2], [0, 0, 0]], [[0, 4, 6], [0, 6, 4], [0, 6, 6], [0, 4, 5], [0, 6, 2], [0, 4, 0], [0, 4, 3], [0, 6, 0], [0, 0, 4], [0, 0, 6], [0, 2, 4], [0, 2, 6], [1, 9, 0], [1, 11, 0], [1, 8, 0], [1, 10, 0], [1, 20, 0], [1, 23, 0], [1, 21, 0], [1, 0, 23], [0, 2, 0], [0, 2, 2], [0, 0, 0], [0, 0, 2]], [[0, 4, 5], [0, 6, 6], [0, 6, 4], [0, 4, 6], [0, 6, 0], [0, 4, 3], [0, 4, 0], [0, 6, 2], [0, 2, 6], [0, 2, 4], [0, 0, 6], [0, 0, 4], [1, 10, 0], [1, 8, 0], [1, 11, 0], [1, 9, 0], [1, 22, 0], [1, 21, 0], [1, 23, 0], [1, 20, 0], [0, 0, 2], [0, 0, 0], [0, 2, 2], [0, 2, 0]], [[1, 21, 0], [1, 23, 0], [1, 22, 0], [1, 20, 0], [1, 8, 0], [1, 11, 0], [1, 10, 0], [1, 9, 0], [0, 4, 2], [0, 4, 0], [0, 6, 0], [0, 6, 2], [0, 2, 4], [0, 0, 6], [0, 2, 6], [0, 0, 4], [0, 0, 0], [0, 2, 2], [0, 0, 2], [0, 2, 0], [0, 6, 6], [0, 6, 4], [0, 4, 4], [0, 4, 6]], [[1, 20, 0], [1, 22, 0], [1, 23, 0], [1, 21, 0], [1, 9, 0], [1, 10, 0], [1, 11, 0], [1, 8, 0], [0, 6, 2], [0, 6, 0], [0, 4, 0], [0, 4, 2], [0, 0, 4], [0, 2, 6], [0, 0, 6], [0, 2, 4], [0, 2, 0], [0, 0, 2], [0, 2, 2], [0, 0, 0], [0, 4, 6], [0, 4, 4], [0, 6, 4], [0, 6, 6]], [[1, 22, 0], [1, 20, 0], [1, 21, 0], [1, 23, 0], [1, 10, 0], [1, 9, 0], [1, 8, 0], [1, 11, 0], [0, 6, 0], [0, 6, 2], [0, 4, 2], [0, 4, 0], [0, 2, 6], [0, 0, 4], [0, 2, 4], [0, 0, 6], [0, 0, 2], [0, 2, 0], [0, 0, 0], [0, 2, 2], [0, 4, 4], [0, 4, 6], [0, 6, 6], [0, 6, 4]], [[1, 23, 0], [1, 21, 0], [1, 20, 0], [1, 22, 0], [1, 11, 0], [1, 8, 0], [1, 9, 0], [1, 10, 0], [0, 4, 0], [0, 4, 2], [0, 6, 2], [0, 6, 0], [0, 0, 6], [0, 2, 4], [0, 0, 4], [0, 2, 6], [0, 2, 2], [0, 0, 0], [0, 2, 0], [0, 0, 2], [0, 6, 4], [0, 6, 6], [0, 4, 6], [0, 4, 4]]]], dtype=int)
conjugation_table = np.array([0, 1, 2, 3, 4, 6, 5, 7, 8, 11, 10, 9, 12, 13, 15, 14, 20, 22, 23, 21, 16, 19, 17, 18], dtype=int)
measure_table = np.array([[[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]], [[1, 1], [1, 1], [1, -1], [1, -1], [2, -1], [2, -1], [2, 1], [2, 1], [3, -1], [3, -1], [3, 1], [3, 1], [1, -1], [1, -1], [1, 1], [1, 1], [2, 1], [2, 1], [2, -1], [2, -1], [3, 1], [3, 1], [3, -1], [3, -1]], [[2, 1], [2, -1], [2, 1], [2, -1], [1, -1], [1, 1], [1, -1], [1, 1], [2, -1], [2, 1], [2, -1], [2, 1], [3, -1], [3, 1], [3, -1], [3, 1], [3, 1], [3, -1], [3, 1], [3, -1], [1, 1], [1, -1], [1, 1], [1, -1]], [[3, 1], [3, -1], [3, -1], [3, 1], [3, -1], [3, 1], [3, 1], [3, -1], [1, -1], [1, 1], [1, 1], [1, -1], [2, -1], [2, 1], [2, 1], [2, -1], [1, 1], [1, -1], [1, -1], [1, 1], [2, 1], [2, -1], [2, -1], [2, 1]]], dtype=int)