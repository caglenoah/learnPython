def area_sum(rectangles):
    total_area = 0
    for rectangle in rectangles:
        area = rectangle['height'] * rectangle ['width']
        total_area += area
    return total_area