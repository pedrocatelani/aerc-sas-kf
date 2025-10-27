def normalize_by_min_max(cur_value, min_value, max_value):
    min_max = (cur_value - min_value) / (max_value - min_value)

    value = (min_max + 0.01) / (1 + 0.01)

    return value
