import json
import os
import myrw


json_province = os.path.dirname(myrw.__file__) + '/json/province.json'
json_district = os.path.dirname(myrw.__file__) + '/json/district.json'
json_sector = os.path.dirname(myrw.__file__) + '/json/sector.json'

class Province:
    def __init__(self, identifier):
        self.identifier = identifier
        self.params = ''

        if isinstance(identifier, str):
            if self.identifier[0] == '0':
                self.params = 'code'
            else:
                try:
                    int(self.identifier)
                    self.params = 'id'
                except ValueError:
                    self.params = 'Name'
        else:
            self.params = 'Please define a string'

    def province(self):

        return self.params


