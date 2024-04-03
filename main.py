def get_odds_and_evens(numbers):
    num_evens = 0
    num_odds = 0
    for number in numbers:
        if number % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    return num_odds, num_evens










# Write the get_odds_and_evens function to loop through the numbers list
# and check if each number in the list is either odd or even.

