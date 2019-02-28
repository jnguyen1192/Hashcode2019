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


def data_retrieve(lines):
    # return the new lines traited
    return lines


def data_preparation(data):
    # return the value of input
    list_photos = []
    for key, d in enumerate(data):
        list_photos.append(Photo(key, d))
    #input_description(list_photos)
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

    def get_list_words(self):
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
        for word in photo.get_list_words():
            strconcat += word + ", "
        strconcat = strconcat[:-2] + "]\n"
    strconcat += "-----------------------------------------------------------\n"
    print(strconcat)


class Slide:
    """
    Class to describe a slide using one horizontal photo
    or two vertical photo
    """
    def __init__(self, photo1, photo2=""):
        self.photo1 = photo1
        self.photo2 = photo2

    def get_words(self):
        if self.photo2 != "":
            return set(self.photo1.get_list_words() + self.photo2.get_list_words())
        else:
            return self.photo1.get_list_words()

    def get_photo1_orientation(self):
        """
        Get the first photo
        :return: a photo
        """
        return self.photo1.get_orientation()

    def get_num_photo1(self):
        """
        Get the number of the first photo
        :return: the num of the photo
        """
        return self.photo1.get_num_photo()

    def get_num_photo2(self):
        """
        Get the number of the second photo
        :return: the num of the photo
        """
        if self.photo2 == "":
            return 0
        else:
            return self.photo2.get_num_photo()


class SlideShow:
    """
    Class to get the score of the current SlideShow
    """
    def __init__(self, list_photos):
        self.list_photos = list_photos
        self.list_slides = []

    def build_slides_easy_way(self):
        """
        The way without logic, only sort the slide with their orientation
        """
        slide_part1 = None
        for photo in self.list_photos:
            if photo.get_orientation() == "H":
                # case the slide is horizontal
                self.list_slides.append(Slide(photo))
            else:
                # case the slide is vertical
                if slide_part1 is None:
                    # add the vertical photo on memory
                    slide_part1 = photo
                else:
                    # create a slide with the photo on memory and the current photo
                    self.list_slides.append(Slide(slide_part1, photo))
                    slide_part1 = None
        import random
        random.shuffle(self.list_slides)

    def intersect_f(self, s_, s_next):
        """
        Get the intersection of the two list
        :param s_: list 1
        :param s_next: list 2
        :return: the number of word in intersect
        """
        return len(set(s_).intersection(s_next))

    def s_not_in_s_next(self, s_, s_next):
        """
        Get the second factor which means s not in s_next
        :param s_: list 1
        :param s_next: list 2
        :return: the number of word of list 1 not in list 2
        """
        return len(set(s_) - set(s_next))

    def s_next_not_in_s_(self, s_, s_next):
        """
        Get the third factor which means s not in s_next
        :param s_: list 1
        :param s_next: list 2
        :return: the number of word of list 1 not in list 2
        """
        return len(set(s_next) - set(s_))

    def interest_factor(self, s_, s_next):
        """
        Get the number of interest factor which is the minimum of
        the three calculate values of factor
        :param s_: list 1
        :param s_next: list 2
        :return: the minumum of factor
        """
        factors = []
        factors.append(self.intersect_f(s_, s_next))
        factors.append(self.s_not_in_s_next(s_, s_next))
        factors.append(self.s_next_not_in_s_(s_, s_next))
        return min(factors)

    def get_score(self):
        """
        Get the score the the slide show using interest factor
        :return: the score
        """
        score = 0
        s_ = self.list_slides[0]
        for s_next in self.list_slides[1:]:
            score += self.interest_factor(s_.get_words(), s_next.get_words())
        return score

    def submit_describe(self):
        """
        Nous voulons afficher le resultat de notre slide show
        sous la forme d'un texte
        The slideshow has 3 slides
        First slide contains photo 0
        Second slide contains photo 3
        Third slide contains photos 1 and 2
        """
        str_concat = "------------------------Submit-----------------------------\n"
        str_concat += "The slideshow has " + str(len(self.list_slides)) + " slides\n"
        for key, slide in enumerate(self.list_slides):
            str_concat += str(key) + " slide contains photo " + str(slide.get_num_photo1())
            if slide.get_photo1_orientation() == "V":
                str_concat += " and " + str(slide.get_num_photo2())
            str_concat += "\n"
        str_concat += "-----------------------------------------------------------\n"
        print(str_concat)

    def visualize(self):
        """
        Nous affichons l'output pour le submit sur le judge system
        """
        str_concat = str(len(self.list_slides)) + "\n"
        for slide in self.list_slides:
            str_concat += str(slide.get_num_photo1())
            if slide.get_photo1_orientation() == "V":
                str_concat += " " + str(slide.get_num_photo2())
            str_concat += "\n"
        return str_concat


def hc2019(lines):
    # data retrieve
    data = data_retrieve(lines)
    # data preparation
    list_photos = data_preparation(data)
    # data modelisation
    slide_show = SlideShow(list_photos)
    # data analyse
    slide_show.build_slides_easy_way()
    # slide_show.submit_describe()
    # data visualize
    res = slide_show.visualize()
    #print(slide_show.get_score())
    return res


class Hashcode2019(unittest.TestCase):

    def test_hashcode2019(self):
        list_sample = ["a_example", "b_lovely_landscapes",
                       "c_memorable_moments", "d_pet_pictures",
                       "e_shiny_selfies"]
        for sample in list_sample:
            lines = input_file(sample + ".txt")
            #res = output_file()
            pred = hc2019(lines)
            f = open(sample + "_output.txt", "w+")
            f.write(pred)
            f.close()
"""
    def test_hashcode2019_e_score(self):
        lines = input_file("e_shiny_selfies.txt")
        #res = output_file()
        pred = hc2019(lines)
        print(pred)
        
    def test_hashcode2019_a(self):
        lines = input_file("b_lovely_landscapes.txt")
        pred = hc2019(lines)
        f = open("b_lovely_landscapes_output.txt", "w+")
        f.write(pred)
        f.close()

    def test_hashcode2019_b(self):
        lines = input_file("b_lovely_landscapes.txt")
        pred = hc2019(lines)
        f = open("b_lovely_landscapes_output.txt", "w+")
        f.write(pred)
        f.close()

    def test_hashcode2019_c(self):
        lines = input_file("c_memorable_moments.txt")
        pred = hc2019(lines)
        f = open("c_memorable_moments_output.txt", "w+")
        f.write(pred)
        f.close()

    def test_hashcode2019_d(self):
        lines = input_file("d_pet_pictures.txt")
        pred = hc2019(lines)
        f = open("d_pet_pictures_output.txt", "w+")
        f.write(pred)
        f.close()

    def test_hashcode2019_e(self):
        lines = input_file("e_shiny_selfies.txt")
        pred = hc2019(lines)
        f = open("e_shiny_selfies_output.txt", "w+")
        f.write(pred)
        f.close()
"""

if __name__ == '__main__':
    unittest.main()
