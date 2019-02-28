import unittest


def input_file(inp):
    # return the input file in a text
    file = open(inp, 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines[1:]


def output_file():
    # read line of output file
    file = open('output', 'r')
    res = file.read()
    file.close()
    return res


class Elve:
    """
    An Elve has a recipe position and value
    """
    def __init__(self, current_recipe_position, current_recipe_value):
        """
        An Elf use those parameter build new recipe
        :param current_recipe_position:
        :param current_recipe_value:
        """
        self.current_recipe_position = current_recipe_position
        self.current_recipe_value = current_recipe_value

    def get_current_recipe_position(self):
        """
        :return:  the current recipe position
        """
        return self.current_recipe_position

    def get_current_recipe_value(self):
        """
        :return:  the current recipe value
        """
        return self.current_recipe_value

    def set_current_recipe_position(self, position):
        """
        set the current recipe position
        """
        self.current_recipe_position = position

    def set_current_recipe_value(self, value):
        """
        set the current recipe value
        """
        self.current_recipe_value = value


class ChocolateChartsManager:
    """
    Chocolate charts manager permits us to know what happened each turn
    """
    def __init__(self, after_number_recipe=9, first_recipe=3, second_recipe=7):
        """
        The value of the first recipe are 3 and 7 for the two elves
        :param after_number_recipe: number of recipe from the beginning of recipe list
        :param first_recipe: recipe of the first elve
        :param second_recipe: recipe of the second elve
        """
        self.after_number_recipe = after_number_recipe
        self.first_elve = Elve(0, first_recipe)
        self.second_elve = Elve(1, second_recipe)
        self.recipes = str(first_recipe) + str(second_recipe)

    def sum_recipes(self):
        """
        Calculate the sum of recipe value of both elves
        :return: the sum of recipe
        """
        return self.first_elve.get_current_recipe_value() + self.second_elve.get_current_recipe_value()

    def extract_result(self, sum_):
        """
        Extract the result from the sum of each elves values
        :param sum_: sum of elves value
        :return: a list or a value
        """
        sum_extract = []
        if sum_/10 >= 1:
            # case superior by ten
            sum_extract.append(int(str(sum_)[0]))
            sum_extract.append(int(str(sum_)[1]))
            return sum_extract
        else:
            # case inferior by ten
            return [sum_]

    def next_elves_position(self):
        """
        Move the two elves using the rule that
        the next position is the current recipe
        value plus the current position plus one
        in the list of recipe
        """
        first_elve_move = (self.first_elve.get_current_recipe_position() + self.first_elve.get_current_recipe_value() + 1) % len(self.recipes)
        self.first_elve.set_current_recipe_position(first_elve_move)
        self.first_elve.set_current_recipe_value(int(self.recipes[first_elve_move]))

        second_elve_move = (self.second_elve.get_current_recipe_position() + self.second_elve.get_current_recipe_value() + 1) % len(self.recipes)
        self.second_elve.set_current_recipe_position(second_elve_move)
        self.second_elve.set_current_recipe_value(int(self.recipes[second_elve_move]))

    def execute(self, debug=False):
        # process on recipes
        i = 0
        while len(self.recipes) < self.after_number_recipe + 10:
            # sum of two elves recipe
            sum_ = self.sum_recipes()
            # split the result if > %10
            #extract_sum = self.extract_result(sum_)
            self.recipes = self.recipes + str(sum_)
            # move the elves
            self.next_elves_position()
            if debug:
                self.print_step(i)
            i += 1

    def print_step(self, i):
        """
        print each step
        """
        import sys
        print(str(i))
        #print(self.recipes)

    def visualize(self):
        """
        Get the ten digits after the number of recipes in input
        :return:ten digits in string format
        """
        return "".join(self.recipes[self.after_number_recipe:self.after_number_recipe+10])


def data_retrieve(lines):
    # return the new lines traited
    return lines


def data_preparation(data):
    # return the value of input
    list_photos = []
    for key, d in enumerate(data):
        list_photos.append(Photo(key, d))
    input_description(list_photos)
    return list_photos


class Photo:
    """
    Class to describe a photo containing a list
    """
    def __init__(self, num_photo, line):
        self.num_photo = num_photo
        self.orientation = line[0]
        self.nb_photo = line[2]
        self.list_photo = line.split(" ")[2:]

    def get_num_photo(self):
        """
        Get the id of the photo
        :return: the id of the photo
        """
        return self.num_photo

    def get_orientation(self):
        """
        Get the orientation of the photo
        :return: the id of the photo
        """
        return self.orientation

    def str_list_words(self):
        """
        Get the list of words
        :return:
        """
        return self.list_photo


def input_description(list_photos):
    """
    Print the data as the example with the cat on the beach
    The collection has 4 photos
    Photo 0 is horizontal and has tags [cat, beach, sun]
    Photo 1 is vertical and has tags [selfie, smile]
    Photo 2 is vertical and has tags [garden, selfie]
    Photo 3 is horizontal and has tags [garden, cat]

    :param list_photos: the different photos of dataset
    """
    strconcat = "-------------------Description----------------------------\n"
    strconcat += "The collection has " + str(len(list_photos)) + " photos\n"
    for photo in list_photos:
        if photo.orientation == 'H':
            ori = "horizontal"
        else:
            ori = "vertical"
        strconcat += "Photo " + str(photo.get_num_photo()) + " is " + ori + " and has tags ["
        for word in photo.str_list_words():
            strconcat += word + ", "
        strconcat = strconcat[:-2] + "]\n"
    print(strconcat)


def output_description(list_slides):
    """
    Print the data as the submission
    :param list_slides:
    :return:
    """


def intersect_f(s_, s_next):
    """
    Get the intersection of the two list
    :param s_: list 1
    :param s_next: list 2
    :return: the number of word in intersect
    """
    return len(set(s_).intersection(s_next))


def s_not_in_s_next(s_, s_next):
    """
    Get the second factor which means s not in s_next
    :param s_: list 1
    :param s_next: list 2
    :return: the number of word of list 1 not in list 2
    """
    return len(set(s_) - set(s_next))


def s_next_not_in_s_(s_, s_next):
    """
    Get the third factor which means s not in s_next
    :param s_: list 1
    :param s_next: list 2
    :return: the number of word of list 1 not in list 2
    """
    return len(set(s_next) - set(s_))


def interest_factor(s_, s_next):
    """
    Get the number of interest factor which is the minimum of
    the three calculate values of factor
    :param s_: list 1
    :param s_next: list 2
    :return: the minumum of factor
    """
    factors = []
    factors.append(intersect_f(s_, s_next))
    factors.append(s_not_in_s_next(s_, s_next))
    factors.append(s_next_not_in_s_(s_, s_next))
    return min(factors)


class Slide:
    """
    Class to describe a slide using one horizontal photo
    or two vertical photo
    """
    def __init__(self, words_photo1, words_photo2=[]):
        self.words_photo1 = words_photo1
        self.words_photo2 = words_photo2
        self.words_slide = set(words_photo1 + words_photo2)

    def get_words(self):
        """
        Get the words of the slide
        :return: the unique words
        """
        return self.words_slide




def hc2019(lines):
    # data retrieve
    data = data_retrieve(lines)
    # data preparation
    list_photos = data_preparation(data)
    # data modelisation
    #chocolate_charts_manager = ChocolateChartsManager(number_after_recipe)
    # data analyse
    #chocolate_charts_manager.execute(False)
    # data visualize
    #ten_digits_after = chocolate_charts_manager.visualize()
    return ""#ten_digits_after


class Hashcode2019(unittest.TestCase):

    def test_hashcode2019_a(self):
        lines = input_file("a_example.txt")
        #res = output_file()
        pred = hc2019(lines)
        print(pred)
        #assert(pred == res)

    def test_code(self):
        from itertools import chain
        string = "hello world"
        for c in chain(string):
            print(c)
        print((chain(string)))
        print(chain(string)[0])


if __name__ == '__main__':
    unittest.main()
