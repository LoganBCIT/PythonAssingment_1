# author: Logan Dutton-Anderson

import data


def print_json_countries_and_capitals():
    """
    Prints each country and it's capital in JSON format
    """
    c = 0
    while c < len(data.countries_and_capitals):
        json_format = '''{\n\t"country_name":"%s", \n\t"capital_city":"%s"\n}''' \
                      % (data.countries_and_capitals[c][0], data.countries_and_capitals[c][1])
        c += 1
        print(json_format)


def get_list_of_countries_whose_nth_letter_is(n, letter):
    """
    Checks each list item in the tuple countries for the nth index, and adds whichever countries' nth index is the given
    letter to a new list of countries.
    :param n: The index that the function uses to determine the new list of countries with the given letter at that index.
    :param letter: The letter that will be at index n for all items in the new list of countries.
    :return: Returns a list of all countries whose nth letter matches the letter in the parameter.
    """
    letter = letter.lower()
    new_list_of_countries = []
    for r in data.countries:
        if r[n - 1].lower() == letter:
            new_list_of_countries.append(r)

    return new_list_of_countries


def get_funny_case_capital_cities(letter):
    """
    Checks each item in the tuple capitals for the given letter. Each time that it finds that letter in an item, it
    will capitalize the letter after and before the instance of that letter, skipping consecutive instances of that letter.
    :param letter: The letter that each item is checked for.
    :return: Returns a new list of items that contain the given letter, with the letters surrounding the given letter being capitalized.
    """

    # For example, if you called get_funny_case_capital_cities(“z”), it would return: ['brAzzAville', 'zAgreb', 'vadUz']
    # notice how in Brazzaville, there is 2 instances of z, and the second one is skipped. the A's encasing it are both
    # capitalized surrounding the z's.
    # However, this function could not handle a capital like 'azzzzzza' but since the tuple is of normal capital names, I kept it simple.

    funny_letter_capital_list = []
    for c in data.capitals:
        c = c.lower()
        letter_check = list(c)
        for index, letter_in_capital in enumerate(letter_check):
            if letter_in_capital == letter:
                if 0 < index < len(letter_check) - 1:  # This ensures that the index isn't 0 or equal to the length of each item so that the [index +- 1] isn't out of bounds.
                    if letter_check[index - 1] != letter_in_capital and letter_check[index + 1] != letter_in_capital:  # makes sure there isn't any duplicates of the given letter in sequence
                        letter_check[index + 1] = letter_check[index + 1].upper()
                        letter_check[index - 1] = letter_check[index - 1].upper()
                        funny_letter_capital = "".join(letter_check)  # This joins the split up capital names back into a word with the newly capitalized letters
                        funny_letter_capital_list.append(funny_letter_capital)  # adds the new list item to the end of the new list
                        break
                    else:
                        if 1 < index < len(letter_check) - 2:  # if there is duplicates, it must be within a smaller range because we need to uppercase a letter 2 in front or 2 behind now
                            if letter_check[index + 1] == letter_in_capital:
                                letter_check[index + 2] = letter_check[index + 2].upper()
                                letter_check[index - 1] = letter_check[index - 1].upper()
                                funny_letter_capital = "".join(letter_check)
                                funny_letter_capital_list.append(funny_letter_capital)
                                break
                            elif letter_check[index - 1] == letter_in_capital:
                                letter_check[index - 2] = letter_check[index - 2].upper()
                                letter_check[index + 1] = letter_check[index + 1].upper()
                                funny_letter_capital = "".join(letter_check)
                                funny_letter_capital_list.append(funny_letter_capital)
                                break
                elif letter_in_capital == letter and index == 0:  # if the index is 0 or the length of the item, we still want the closest letter to be capitalized, so this covers that
                    letter_check[index + 1] = letter_check[index + 1].upper()
                    funny_letter_capital = "".join(letter_check)
                    funny_letter_capital_list.append(funny_letter_capital)
                    break
                elif letter_in_capital == letter and index == len(letter_check) - 1:
                    letter_check[index - 1] = letter_check[index - 1].upper()
                    funny_letter_capital = "".join(letter_check)
                    funny_letter_capital_list.append(funny_letter_capital)
                    break
    return funny_letter_capital_list


def get_doubled_letter_countries():
    """
    Creates a tuple of all the countries that have doubled letters and sorts them alphabetically by the doubled letter.
    :return: Returns a tuple of all the countries that have a doubled letter, organised alphabetically by the doubled letter
    """
    countries_with_doubled_letters = []
    for country in data.countries:
        for letter in range(len(country) - 1):
            if country[letter] != " " and country[letter + 1] == country[letter]:  # this checks each item in countries for a doubled letter and adds it to a new list
                countries_with_doubled_letters.append(country)

    countries_with_doubled_letters.sort(key=lambda c: has_doubled_letter(c.lower()))  # uses lambda and the external function called has_doubled_letter() to determine how to sort the countries
    countries_with_doubled_letters = tuple(countries_with_doubled_letters)  
    return countries_with_doubled_letters


def has_doubled_letter(c):   # this is an external function that checks and returns the doubled letter's char value so that it can be sorted accordingly using lambda
    for i in range(len(c) - 1):
        if c[i] != " " and c[i + 1] == c[i]:  # takes the parameter and checks if it's a doubled letter. if so, it returns that letter so that lambda can use it to sort the tuple appropriately
            return c[i]

    return False


def main():
    print("I should not be called.")


if __name__ == '__main__':
    main()
