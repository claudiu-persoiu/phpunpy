import string

__author__ = "Claudiu Persoiu"
__copyright__ = "Copyright 2014, Claudiu Persoiu"
__license__ = "GPL"
__email__ = "claudiu@claudiupersoiu.ro"

class DumpPHPUnserialized:

    def __init__(self, str):
        self.str = str
        self.output = ''
        self.buffer = ''
        self.objects = 0

    def unserialize(self):
        identifier = self._get_identifier()
        self.parse(identifier)()
        return self.output

    def _get_identifier(self):
        result = self.str[0:1]
        self.str = self.str[2:]
        return result

    def parse(self, identifier):
        return {'a': self._parse_array,
             'i': self._parse_integer,
             'b': self._parse_boolean,
             'd': self._parse_decimal,
             'N': self._parse_null,
             's': self._parse_string,
             'O': self._parse_object}[identifier]

    def _parse_array(self):
        elements_number = self._elements_number()

        self.str = self.str[1:] # {
        buffer = self.buffer
        self.buffer += "  "
        self.output += buffer + "array(" + elements_number + ") {\n"
        
        for i in range(0, int(elements_number)):
            try:
                self.parse(self._get_identifier())(True)
                self.unserialize()
            except Exception:
                pass
            
        self.output += buffer + "}\n"
        self.buffer = buffer
        self.str = self.str[1:] # }

    def _parse_object(self):
        str_length = self._elements_number()

        result = self.str[1:int(str_length)+1]
        self.str = self.str[int(str_length) + 3:] # "str":

        self.objects += 1
        
        elements_number = self._elements_number()
        
        buffer = self.buffer
        self.buffer += "  "
        self.output += buffer + 'Object(' + result + ")#" + str(self.objects) + " (" + elements_number + ") {\n"
        self.str = self.str[1:] # {
        
        for i in range(0, int(elements_number)):
            self.parse(self._get_identifier())(True)
            self.unserialize()
            
        self.output += buffer + "}\n"
        self.buffer = buffer
        self.str = self.str[1:] # }


    def _elements_number(self):
        result = self.str[0:self.str.index(':')]
        self.str = self.str[len(result)+1:] # :
        return result

    def _parse_integer(self, identifier = False):
        int_length = self.str.index(';')
        result = self.str[:int_length]
        self.str = self.str[int(int_length) + 1:] # ;
        
        if identifier:
            self.output += self.buffer + '[' + result + ']=>' + "\n"
        else:
            self.output += self.buffer + 'int(' + result + ")\n"
        
    def _parse_boolean(self, identifier = False):
        result_int = self.str[:1]
        if result_int == '0':
            result = 'false'
        else:
            result = 'true'
            
        self.str = self.str[2:] # ;
        if identifier:
            self.output += self.buffer + '[' + result + ']=>' + "\n"
        else:
            self.output += self.buffer + 'bool(' + result + ")\n"

    def _parse_decimal(self, identifier = False):
        float_length = self.str.index(';')
        result = str(float(self.str[:float_length]))
        self.str = self.str[int(float_length) + 1:] # ;
        
        if identifier:
            self.output += self.buffer + '[' + result + ']=>' + "\n"
        else:
            self.output += self.buffer + 'float(' + result + ")\n"

    def _parse_null(self, identifier = False):
        if identifier:
            self.output += self.buffer + '[NULL]=>' + "\n"
        else:
            self.output += self.buffer + "NULL\n"

    def _parse_string(self, identifier = False):
        str_length = self._elements_number()
        result = self.str[1:int(str_length)+1]
        self.str = self.str[int(str_length) + 3:] # "str";
        
        if identifier:
            self.output += self.buffer + '["' + result + '"]=>' + "\n"
        else:
            self.output += self.buffer + 'string(' + str_length + ') "' + result + '"' + "\n"

