def triangle_type(a, b, c):
    max_side = max(a, b, c)
    
    if a + b + c <= 2 * max_side: return "Not Triangle"
    if 2 * max_side ** 2 == a ** 2 + b ** 2 + c ** 2: return "Right Triangle"
    if 2 * max_side ** 2 > a ** 2 + b ** 2 + c ** 2: return "Obtuse Triangle"
    return "Acute Triangle"