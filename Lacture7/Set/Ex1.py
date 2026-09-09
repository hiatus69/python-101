survey_results = [
    ["Python","JavaScript","C++"],
    ["Python","JavaScript","C#"],
    ["Python","Java"],
    ["Python","C++","JavaScript",],
    ["Python","JavaScript","C++","Java"]
]

survey_results_set = [set(line) for line in survey_results]
all_languages = set.union(*survey_results_set)

#1
languages_use_every_line = set.intersection(*survey_results_set)
print(languages_use_every_line)

#2
one = []
for line in survey_results_set:
    
    Tee = all_languages ^ line
    one.append(Tee)
    print(one)

# print(chosenone)


#3
languages_count = len(all_languages)
print(languages_count)

#4
