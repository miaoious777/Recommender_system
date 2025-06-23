import numpy as np

def calculate_cosine_similarity_2d(vec1, vec2):
    """
    计算两个二维向量的余弦相似度。

    参数:
    vec1 (list 或 numpy.array): 第一个二维向量，例如 [x1, y1]
    vec2 (list 或 numpy.array): 第二个二维向量，例如 [x2, y2]

    返回:
    float: 两个向量的余弦相似度。
           如果输入的向量不是二维的，将抛出 ValueError。
           如果任一向量为零向量，将返回0，因为无法定义方向。
    """
    if len(vec1) != 2 or len(vec2) != 2:
        raise ValueError("输入向量必须是二维的。")

    np_vec1 = np.array(vec1)
    np_vec2 = np.array(vec2)

    # 计算内积
    dot_product = np.dot(np_vec1, np_vec2)

    # 计算模长
    norm_vec1 = np.linalg.norm(np_vec1) # ||vec1||
    norm_vec2 = np.linalg.norm(np_vec2) # ||vec2||

    # 避免除以零的情况（如果向量是零向量）
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0 # 零向量没有明确的方向，通常认为相似度为0

    cosine_similarity = dot_product / (norm_vec1 * norm_vec2)

    return float(cosine_similarity)

def calculate_cosine_similarity_n_dim(vec1, vec2):
    """
    计算两个N维向量的余弦相似度。

    参数:
    vec1 (list 或 numpy.array): 第一个N维向量
    vec2 (list 或 numpy.array): 第二个N维向量

    返回:
    float: 两个向量的余弦相似度。
           如果输入的向量维度不一致，将抛出 ValueError。
           如果任一向量为零向量，将返回0，因为无法定义方向。
    """
    if len(vec1) != len(vec2):
        raise ValueError("输入向量的维度必须一致。")

    np_vec1 = np.array(vec1)
    np_vec2 = np.array(vec2)

    # 计算内积
    dot_product = np.dot(np_vec1, np_vec2)

    # 计算模长
    norm_vec1 = np.linalg.norm(np_vec1) # ||vec1||
    norm_vec2 = np.linalg.norm(np_vec2) # ||vec2||

    # 避免除以零的情况（如果向量是零向量）
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0 # 零向量没有明确的方向，通常认为相似度为0

    cosine_similarity = dot_product / (norm_vec1 * norm_vec2)

    return float(cosine_similarity)

# --- 示例用法 ---
if __name__ == "__main__":
    print("--- 二维向量余弦相似度 ---")
    vec2d_a = [1, 1]
    vec2d_b = [2, 2] # 与 vec2d_a 同向，模长不同
    vec2d_c = [1, 0] # 正交
    vec2d_d = [-1, -1] # 反向
    vec2d_e = [0, 0] # 零向量

    print(f"向量 A: {vec2d_a}, 向量 B: {vec2d_b}, 相似度: {calculate_cosine_similarity_2d(vec2d_a, vec2d_b):.4f}") # 应该接近 1.0
    print(f"向量 A: {vec2d_a}, 向量 C: {vec2d_c}, 相似度: {calculate_cosine_similarity_2d(vec2d_a, vec2d_c):.4f}") # 应该接近 0.707 (45度)
    print(f"向量 A: {vec2d_a}, 向量 D: {vec2d_d}, 相似度: {calculate_cosine_similarity_2d(vec2d_a, vec2d_d):.4f}") # 应该接近 -1.0
    print(f"向量 A: {vec2d_a}, 向量 E: {vec2d_e}, 相似度: {calculate_cosine_similarity_2d(vec2d_a, vec2d_e):.4f}") # 应该为 0.0 (零向量)

    print("\n--- N 维向量余弦相似度 ---")
    vecN_x = [1, 2, 3, 4]
    vecN_y = [5, 6, 7, 8]
    vecN_z = [-1, -2, -3, -4] # 反向
    vecN_w = [0, 0, 0, 0] # 零向量
    vecN_p = [1, 0, 0, 0]
    vecN_q = [0, 1, 0, 0] # 正交

    print(f"向量 X: {vecN_x}, 向量 Y: {vecN_y}, 相似度: {calculate_cosine_similarity_n_dim(vecN_x, vecN_y):.4f}")
    print(f"向量 X: {vecN_x}, 向量 Z: {vecN_z}, 相似度: {calculate_cosine_similarity_n_dim(vecN_x, vecN_z):.4f}") # 应该接近 -1.0
    print(f"向量 X: {vecN_x}, 向量 W: {vecN_w}, 相似度: {calculate_cosine_similarity_n_dim(vecN_x, vecN_w):.4f}") # 应该为 0.0 (零向量)
    print(f"向量 P: {vecN_p}, 向量 Q: {vecN_q}, 相似度: {calculate_cosine_similarity_n_dim(vecN_p, vecN_q):.4f}") # 应该为 0.0 (正交)

    # 错误处理示例
    try:
        calculate_cosine_similarity_2d([1, 2, 3], [4, 5])
    except ValueError as e:
        print(f"\n错误捕获 (2D): {e}")

    try:
        calculate_cosine_similarity_n_dim([1, 2, 3], [4, 5])
    except ValueError as e:
        print(f"错误捕获 (N-dim): {e}")