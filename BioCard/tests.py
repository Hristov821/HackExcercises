import unittest
from BioCardGenerator import get_people
from BioCardGenerator import get_data
from BioCardGenerator import create_indentation_card_string
import os.path

class Test(unittest.TestCase):

    def test_get_people(self):
        strr = 'dsads'
        data=get_data('copy.json')
        self.assertRaises(AssertionError, get_people, strr)
        self.assertRaises(AssertionError,get_people,data)
    def test_create_indentation_card_string(self):
    	test='DEFINATLY NOT DICT'
    	data=get_data("data.json")
    	people=get_people(data)
    	wrong_person=...
    	for i in people:
    		img=i['avatar']
    		if os.path.exists(img)==False:
    			wrong_person=i

    	self.assertRaises(AssertionError,create_indentation_card_string,wrong_person)


if __name__ == '__main__':
    unittest.main()
