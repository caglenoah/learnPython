def get_test_score(answer_sheet, student_answers):
    correct_ans = 0
    for ans_key, ans_student in zip(answer_sheet, student_answers):
        if ans_key == ans_student:
            correct_ans += 1
    percentage = (correct_ans / len(answer_sheet)) * 100
    return percentage
        









#my original code
# def get_test_score(answer_sheet, student_answers):
#     correct_ans = 0 
#     for i in range(len(answer_sheet)):
#         if answer_sheet[i] == student_answers[i]:
#             correct_ans += 1
#     percentage = (correct_ans / len(answer_sheet)) * 100
#     return percentage