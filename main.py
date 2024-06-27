def main():
    with open('books/frankenstein.txt', 'r') as file:
        file_contents = file.read()
    # print(count_words(file_contents))
    # print(character_count(file_contents))
    ## turning the object into an array of objects

    character_dict = character_count(file_contents)
    character_array = []
    for key, value in character_dict.items():
        character_array.append({"name":key,"value":value})

    ## sorting the array    
    character_array.sort(reverse=True,key=sort_on)

    ### writing the report

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print("")
    for element in character_array:
        print(f"The '{element['name']}' character was found {element['value']} times")
    print("--- End report ---")



## sorting a list of dicts on a value in a dict
def sort_on(dict):
    return dict["value"]

def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_case_text = text.lower()
    obj = {}
    for element in lower_case_text:
        if element.isalpha():
            if element in obj:
                obj[element] += 1
            else:
                obj[element] = 1
    return obj






if __name__ == '__main__':
    main()
