from itertools import permutations

def generate_combinations(word, start_index, end_index,combination_length):
    if end_index > len(word):
        end_index = len(word)
    substring = word[start_index:end_index]
    if end_index<len(word):
        rest_2=word[end_index:len(word)]
    else:
        rest_2=""
    rest=word[0:start_index]
    combinations=[]
    for p in permutations(substring):
        temp=''.join(p)
        if end_index-start_index>combination_length:
            temp=temp[0:combination_length]
        combination=rest+temp+rest_2
        combinations.append(combination)
    return combinations

def write_combinations_to_file(word, start_index, end_index, filename,combination_length):
    combinations = generate_combinations(word, start_index, end_index,combination_length)
    with open(filename, 'w') as file:
        for combination in combinations:
            file.write(combination + '\n')
            
word = input("Enter a word: ")
start_index = int(input("Enter the position of the firt letter: "))
end_index = int(input("Enter the position of the last letter: "))
filename = input("Enter the filename to save combinations: ")
combination_length = int(input("Enter the lenght of the resulting combination: "))
if start_index < 0 or end_index < 0 or start_index > end_index or start_index >= len(word):
    print("Invalid input")
else:
    write_combinations_to_file(word, start_index-1, end_index,filename,combination_length)
    print("Program finished succesfully")

