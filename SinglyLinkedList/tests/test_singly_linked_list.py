from src.SinglyLinkedList.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList:
    """Class containing test methods for singlyLinkedList"""

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        """?Instantiate new singlyLinkedList before each test"""
        print('setUp')
        singly_linked_list = SinglyLinkedList()

    def tearDown(self):
        print('tearDown')

    def test__init__(self):
        self.assertEquals()






