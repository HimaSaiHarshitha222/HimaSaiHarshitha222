original_str = "The quick brown fox jumps over the extremely lazy dog."
num_words_list = []
for i in original_str.split():
    num_words_list.append(len(i))
print(num_words_list)
