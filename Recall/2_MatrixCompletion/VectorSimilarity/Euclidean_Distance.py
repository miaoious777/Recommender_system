import math

def euclidean_distance_2d(vec1, vec2):
    """
    计算两个二维向量的欧几里得距离。

    参数:
    vec1 (tuple 或 list): 第一个二维向量，例如 (x1, y1) 或 [x1, y1]。
    vec2 (tuple 或 list): 第二个二维向量，例如 (x2, y2) 或 [x2, y2]。

    返回:
    float: 两个向量之间的欧几里得距离。
    """
    if len(vec1) != 2 or len(vec2) != 2:
        raise ValueError("输入向量必须是二维的（包含两个元素）。")

    x1, y1 = vec1[0], vec1[1]
    x2, y2 = vec2[0], vec2[1]

    distance = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return distance

# --- 示例用法（二维向量） ---
vector_a = (1, 2)
vector_b = (4, 6)
dist_ab = euclidean_distance_2d(vector_a, vector_b)
print(f"向量 {vector_a} 和 {vector_b} 之间的欧几里得距离是: {dist_ab:.4f}")

def euclidean_distance_nd(vec1, vec2):
    """
    计算两个任意维度向量的欧几里得距离。

    参数:
    vec1 (list 或 tuple): 第一个向量。
    vec2 (list 或 tuple): 第二个向量。

    返回:
    float: 两个向量之间的欧几里得距离。

    Raises:
    ValueError: 如果输入向量的维度不一致。
    """
    if len(vec1) != len(vec2):
        raise ValueError("输入向量的维度必须一致。")

    # 计算每个维度上差的平方，然后求和
    # sum_sq_diff = 0
    # for i in range(len(vec1)):
    #     sum_sq_diff += (vec1[i] - vec2[i]) ** 2

    # 或者使用更简洁的 生成器表达式 和 sum() 函数
    sum_sq_diff = sum((v1 - v2)**2 for v1, v2 in zip(vec1, vec2))

    distance = math.sqrt(sum_sq_diff)
    return distance

# --- 示例用法（任意维度向量） ---
if __name__ == "__main__":
    # 高维向量示例
    vector_a_high_dim = [10, 20, 30, 40, 50]
    vector_b_high_dim = [11, 22, 29, 41, 53]
    dist_high_dim = euclidean_distance_nd(vector_a_high_dim, vector_b_high_dim)
    print(f"高维向量 {vector_a_high_dim} 和 {vector_b_high_dim} 的欧几里得距离是: {dist_high_dim:.4f}")
