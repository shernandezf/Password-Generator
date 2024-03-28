from itertools import permutations

def generate_combinations(word, start_index, end_index):
    if end_index > len(word):
        end_index = len(word)
    substring = word[start_index:end_index]
    rest=word[0:start_index]
    combinations=[]
    for p in permutations(substring):
        temp=''.join(p)
        combination=rest+temp
        combinations.append(combination)
    return combinations

def write_combinations_to_file(word, start_index, end_index, filename):
    combinations = generate_combinations(word, start_index, end_index)
    with open(filename, 'w') as file:
        for combination in combinations:
            file.write(combination + '\n')
            
word = input("Enter a word: ")
start_index = int(input("Enter the starting index: "))
end_index = int(input("Enter the ending index: "))
filename = input("Enter the filename to save combinations: ")

if start_index < 0 or end_index < 0 or start_index > end_index or start_index >= len(word):
    print("Invalid input")
else:
    write_combinations_to_file(word, start_index-1, end_index,filename)
    print("Program finished succesfully")

