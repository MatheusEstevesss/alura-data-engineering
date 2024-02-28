import json
import csv

class Data:
    def __init__(self, path, type): #self = maneira que o python interpreta o objeto(para poder acessar as propriedades)
        self.__path = path
        self.__dataType = type
        self.data = self.__reading_data()
        self.columns_name = self.__get_columns()

    def __reading_json_data(self):
        with open(self.__path, 'r') as file:
            json_data = json.load(file)

        return json_data

    def __reading_csv_data(self):
        csv_data = []

        with open(self.__path, 'r') as file:
            spam_reader = csv.DictReader(file, delimiter=',')
            for data in spam_reader:
                csv_data.append(data)
            
        return csv_data

    def __reading_data(self):
        data = []

        if self.__dataType == 'csv':
            data = self.__reading_csv_data()
        elif self.__dataType == 'json':
            data = self.__reading_json_data()
        elif self.__dataType == 'list':
            data = self.__path
            self.__path = 'list in memory'

        return data
    
    def __get_columns(self):
        return list(self.data[-1].keys())
    
    def rename_columns(self, key_mapping):
        new_data = []

        for old_dict in self.data:
            dict_tmp = {}
            for old_key, value in old_dict.items():
                dict_tmp[key_mapping[old_key]] = value
            new_data.append(dict_tmp)
        
        self.data = new_data
        self.columns_name = self.__get_columns()

    def matching_data(dataA, dataB):
        combined_list = []

        combined_list.extend(dataA.data)
        combined_list.extend(dataB.data)

        return Data(combined_list, 'list')
    
    def __transforming_data_table(self):
        combined_data_table = [self.columns_name]

        for row in self.data:
            new_row = []
            for column in self.columns_name:
                new_row.append(row.get(column, 'Indisponivel'))
            combined_data_table.append(new_row)

        return combined_data_table
    
    def saving_data(self, path):

        matching_data_table = self.__transforming_data_table()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(matching_data_table)
        
        return(f'File saved on: {path} with {len(matching_data_table)} rows')