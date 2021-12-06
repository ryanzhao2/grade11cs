g = 'Horror'
list2_title = ['Fast', 'Slow', 'Medium', 'Ok']
list2_genre = [['Horror', 'Adventure', 'Sci-fi'], ['Adventure', 'Sci-fi'], ['Horror', 'Adventure', 'Sci-fi'], ['Horror', 'Adventure', 'Sci-fi']]
list2_actors = ['Jackie Chan', 'Ryan Reynolds', 'Actor1', 'Actor2']
list2_writers = ['Ryan', 'Bob', 'Jack', 'Kevin']
main_list = []
for i in range(len(list2_genre)):
    if g in list2_genre[i]:
        print('\n', list2_title[i], list2_genre[i], list2_actors[i], list2_writers[i])
"""
main_list.append(list2_title)
main_list.append(list2_genre)
main_list.append(list2_actors)
main_list.append(list2_writers)
print(main_list)
"""
