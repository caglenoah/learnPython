def get_test_score(answer_sheet, student_answers):
        name = student_answers.pop(0)
        correct_count = 0
        for i in range(0, len(answer_sheet)):
            if answer_sheet[i] == student_answers[i]:
                correct_count += 1
        percentage = (correct_count / len(answer_sheet)) * 100
        return name, percentage