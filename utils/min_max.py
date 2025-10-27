def normalize_by_min_max(cur_value, min_value, max_value):
    min_max = (cur_value - min_value + 0.001) / (max_value - min_value + 0.001)

    return min_max
