class Color:

    def __init__(self,rgb,name):
        self.rgb = rgb
        self.__name = name
    def set_name(self,name):
        if not isinstance(name,str):
            raise TypeError("nane is not valid")
        self.__name = name
    def get_name(self):
        return self.__name
    def del_name(self):
        del self.__name
        print("del")
    c = property(get_name,set_name,del_name)

c = Color(1,"red")
del c.c
