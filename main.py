def get_english_grade(student):
    english_grade = student["type"]["student"]["courses"]["English_1010"]["current_grade"]
    return english_grade