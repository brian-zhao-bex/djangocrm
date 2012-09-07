import pystache
 
class Index(pystache.View):
    def set_names(self, names):
        self.__names = names
    def names(self):
        return self.__names
 
class Edit(pystache.View):
 
    def set_name(self, name):
        self.__name = name
 
    def name(self):
        return self.__name
 
 
class Outline(pystache.View):
    def set_body(self, body):
        self.__body = body
 
    def body(self):
        return self.__body.render()