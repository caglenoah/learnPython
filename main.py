def filter_messages(messages):
    filtered_list = []
    number_of_dang = []
    for message in messages:
        words = message.split()
        clean_words = []
        counter = 0
        for word in words:
            if word == "dang":
                counter += 1
            else:
                clean_words.append(word)
        clean_message = " ".join(clean_words)
        filtered_list.append(clean_message)
        number_of_dang.append(counter)
    return filtered_list, number_of_dang



            















# A list of the same messages but with all instances of the word dang removed.
# A list containing the number of dang words that were removed from the message at that particular index.

# Create the 2 empty lists that you'll return at the end. One for the filtered messages, and one for counts of words removed.
# For each message in the input list:
# Split the message into a list of words 
# Create a new empty list for all the non-bad words for this message. *
# Create a counter variable and set it to 0. *
# For each word in the message:
# If the word is dang, increment the counter
# If it is not dang, add the word to the non-bad word list you created
# Join the list of non-bad words into a single string *
# Append the new clean message to the final list of filtered messages
# Append the count of bad words removed to its list

# Return the filtered messages first, then the counters
