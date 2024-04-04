def merge(dict1, dict2):
    merged_dict = {}
    for k in dict1:
        merged_dict[k] = dict1[k]
    for k in dict_2:
        merged_dict[k] = dict2[k]
    return merged_dict
   

def total_score(score_dict):
    total = 0 
    for key, value in score_dict.items():
        total += value
    return total
    

# def merge(dict1, dict2):
#     merged_scores = {
#         "first_quarter": dict1["first_quarter"] if "first_quarter" in dict1 else 0,
#         "second_quarter": dict1["second_quarter"] if "second_quarter" in dict1 else 0,
#         "third_quarter": dict2["third_quarter"] if "third_quarter" in dict2 else 0,
#         "fourth_quarter": dict2["fourth_quarter"] if "fourth_quarter" in dict2 else 0,
#     }
#     return merged_scores
# def total_score(score_dict):
#     total = 0
#     total += score_dict["first_quarter"]
#     total += score_dict["second_quarter"]
#     total += score_dict["third_quarter"]
#     total += score_dict["fourth_quarter"]
#     return total

