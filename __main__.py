from fuzzywuzzy import fuzz
list = ["this is a test", "this is a test!", "this", "this "]
final_list = []
matching_val = 0
match_ratio = 91
for value in list:
	for final_val in final_list:
		matching_val = fuzz.ratio(value, final_val)
		if matching_val > match_ratio:
			break;
	if matching_val < match_ratio:
		final_list.append(value)

print final_list
