class Square:
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value): 
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        if value < 0 :
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return(self.__size * self.__size)
    
    def my_print(self):
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                print(self.__size * '#')