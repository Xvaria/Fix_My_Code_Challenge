#!/usr/bin/python3
'''My square'''


class square():
    '''I love geometry!'''
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        '''Method initialize'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        '''Method Area'''
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        '''Method Perimeter'''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''Method to print'''
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
