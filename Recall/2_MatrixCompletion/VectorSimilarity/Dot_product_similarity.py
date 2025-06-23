import numpy as np

def dot_product_similarity_2d(vec1, vec2):
    """
    计算两个二维向量的内积相似度
    :param vec1: 第一个二维向量，格式为 [x1, y1]
    :param vec2: 第二个二维向量，格式为 [x2, y2]
    :return: 内积结果（标量值）
    """
    # 检查向量维度是否为2
    if len(vec1) != 2 or len(vec2) != 2:
        raise ValueError("输入向量必须是二维的")

    # 计算内积
    similarity = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    return similarity

# 示例用法(二维)
vector_a = [1, 2]
vector_b = [3, 4]
result = dot_product_similarity_2d(vector_a, vector_b)
print(f"向量 {vector_a} 和 {vector_b} 的内积相似度为: {result}")

def calculate_dot_product_similarity_n_dim(vec1, vec2):
    """
    计算两个N维向量的内积相似度。

    参数:
    vec1 (list 或 numpy.array): 第一个N维向量，例如 [x1, y1, z1, ...]
    vec2 (list 或 numpy.array): 第二个N维向量，例如 [x2, y2, z2, ...]

    返回:
    float: 两个向量的内积相似度。
           如果输入的向量维度不一致，将抛出 ValueError。
    """
    if len(vec1) != len(vec2):
        raise ValueError("输入向量的维度必须一致。")

    # 将输入转换为 NumPy 数组，以便进行向量运算
    np_vec1 = np.array(vec1)
    np_vec2 = np.array(vec2)

    # 计算内积
    dot_product = np.dot(np_vec1, np_vec2)

    return float(dot_product)

# --- 示例用法 ---
if __name__ == "__main__":
    # 二维向量示例
    vector_2d_a = [1, 2]
    vector_2d_b = [3, 4]

    # 三维向量示例
    vector_3d_p = [1, 2, 3]
    vector_3d_q = [4, -1, 0]

    # 四维向量示例
    vector_4d_x = [1, 0, -1, 2]
    vector_4d_y = [3, 2, 0, -1]

    print("--- N 维向量内积相似度计算 ---")

    print(f"\n2D 向量 A: {vector_2d_a}")
    print(f"2D 向量 B: {vector_2d_b}")
    similarity_2d = calculate_dot_product_similarity_n_dim(vector_2d_a, vector_2d_b)
    print(f"向量 A 和 向量 B 的内积相似度: {similarity_2d}") # 1*3 + 2*4 = 11

    print(f"\n3D 向量 P: {vector_3d_p}")
    print(f"3D 向量 Q: {vector_3d_q}")
    similarity_3d = calculate_dot_product_similarity_n_dim(vector_3d_p, vector_3d_q)
    print(f"向量 P 和 向量 Q 的内积相似度: {similarity_3d}") # 1*4 + 2*(-1) + 3*0 = 4 - 2 + 0 = 2

    print(f"\n4D 向量 X: {vector_4d_x}")
    print(f"4D 向量 Y: {vector_4d_y}")
    similarity_4d = calculate_dot_product_similarity_n_dim(vector_4d_x, vector_4d_y)
    print(f"向量 X 和 向量 Y 的内积相似度: {similarity_4d}") # 1*3 + 0*2 + (-1)*0 + 2*(-1) = 3 + 0 + 0 - 2 = 1

    # 错误处理示例: 维度不一致的向量
    try:
        calculate_dot_product_similarity_n_dim([1, 2, 3], [4, 5])
    except ValueError as e:
        print(f"\n错误捕获: {e}")

    try:
        calculate_dot_product_similarity_n_dim([1], [4, 5])
    except ValueError as e:
        print(f"错误捕获: {e}")