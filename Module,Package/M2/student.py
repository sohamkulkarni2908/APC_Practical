def total(m1, m2, m3):
    return m1 + m2 + m3

def percentage(total):
    return total / 3

def grade(per):
    if per >= 75:
        return "A"
    elif per >= 60:
        return "B"
    elif per >= 50:
        return "C"
    else:
        return "D"