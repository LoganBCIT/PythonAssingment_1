# author: logan dutton-anderson
import data
from data import countries_and_capitals, countries, capitals
import project
from string import ascii_lowercase


def main():
    project.print_json_countries_and_capitals()
    print("----------------------------------------------------")
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']
    list_of_nums = [1, 2, 3]
    for v in list_of_vowels:
        for n in list_of_nums:
            print("____________________________________________________")
            print(project.get_list_of_countries_whose_nth_letter_is(n, v))
    for letter in ascii_lowercase:
        print("-----------------------------------------------------")
        print("Letter:", letter)
        print(project.get_funny_case_capital_cities(letter))
    print("____________________________________________________")
    print(project.get_doubled_letter_countries())


if __name__ == '__main__':
    main()
