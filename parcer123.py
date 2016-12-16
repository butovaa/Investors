import csv, json


class Investors():
    def parse_companies(file="companies.csv"):
    
        with open(file, newline="") as csvfile:
            csvreader = [x for x in csv.reader(csvfile)]
            return csvreader

    def create_dictionary(list, organization):
    
        dictionary = {rows[0]:rows[1] for rows in csvreader}
        return dictionary

    def decode_json(dictionary, json_name):
        parced_json = json.dumps(dictionary, indent=4)
        return parced_json

    def csv_to_json(file, json_name):
        self.decode_json(encode_csv(csv_name), json_name)


print(type(Investors))
print(type(Investors()))