import json
import os
import myrw



class Province:
    def __init__(self, identifier):
        self.identifier = identifier
        self.params = ''
        self.json_province  = os.path.dirname(myrw.__file__) + '/json/province.json'
        self.json_district =  os.path.dirname(myrw.__file__) + '/json/district.json'
        self.json_sector =  os.path.dirname(myrw.__file__) + '/json/sector.json'

        try:
            if self.identifier.lower() == 'all':
                self.params = 'all'

            elif isinstance(identifier, str):
                if self.identifier[0] == '0':
                    self.params = 'code'
                else:
                    try:
                        self.identifier = int(self.identifier)
                        self.params = 'id'
                    except ValueError:
                        self.params = 'name'
            self.status = 'success'
        except AttributeError:
            self.status = 'error'



    def province(self):
        json_province = json.loads(open(self.json_province).read())

        if self.status == 'error':
            return json.dumps({'error': 'class Province allow string not int'})


        if self.params == 'all':
            return json.dumps({'provinces': json_province},
                        sort_keys=True,
                        indent=3,
                        separators=(',', ': ')
                    )
        else:
            json_data = {'province':[]}
            for province in json_province:
                try:
                    if province[self.params].lower() == self.identifier.lower():
                        json_data['province'].append(province)
                except AttributeError:
                    if province[self.params] == self.identifier:
                        json_data['province'].append(province)
            return json.dumps(json_data,
                        sort_keys=True,
                        indent=3,
                        separators=(',', ': ')
                    )


    def district(self):
        json_province =  json.loads(open(self.json_province).read())
        json_district = json.loads(open(self.json_district).read())
        data = []

        if self.status == 'error':
            return json.dumps({'error': 'class Province allow string not int'})

        if self.params == 'all':
            for province in json_province:
                json_p = {province['name']:[]}
                province['district'] = ''
                json_d = []
                for district in json_district:
                    if province['id'] == district['province_id']:
                        json_d.append(district)

                province['district'] = json_d
                json_p[province['name']].append(province)

                data.append(json_p)

            return json.dumps(data,
                    sort_keys=False,
                    indent=3,
                    separators=(',', ': ')
                )
        else:
            data = {}
            province = json.loads(Province(str(self.identifier)).province())['province']
            for item in province:
                data['id'] = item['id']
                data['name'] = item['name']
                data['code'] = item['code']

            json_p = {data['name']:[]}
            json_d = []


            for district in json_district:
                if data['id'] == district['province_id']:
                    json_d.append(district)

            data['district'] = json_d
            json_p[data['name']].append(data)

            return json.dumps(json_p,
                    sort_keys=False,
                    indent=3,
                    separators=(',', ': ')
                )






