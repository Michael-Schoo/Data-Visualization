
from os.path import exists
import csv

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
class TitanicType(dict):
    PassengerId: int
    Survived: int
    Pclass: int
    Name: str
    Sex: str
    Age: float
    SibSp: int
    Parch: int 
    Ticket: str
    Fare: float
    Cabin: str
    Embarked: str
    def get_raw_data(self):
        temp_dict = {
            "PassengerId": self.PassengerId,
            "Survived": self.Survived,
            "Pclass": self.Pclass,
            "Name": self.Name,
            "Sex": self.Sex,
            "Age": self.Age,
            'SibSp': self.SibSp,
            "Parch": self.Parch,
            "Ticket": self.Ticket,
            "Fare": self.Fare,
            "Cabin": self.Cabin,
            "Embarked": self.Embarked
        }
        return temp_dict

  # no suggestion here
class GetData:
    def __init__(self):
        self.data = []
        self.file_name = "data.csv"
    
    def get_data(self):
            
        file_exists = exists("./awesome-public-datasets/Datasets/titanic.csv/titanic.csv")

        if not file_exists:
            raise Exception("File not found (uncompress the dataset and try again)")

        dictionary: list[TitanicType] = []

        with open('./awesome-public-datasets/Datasets/titanic.csv/titanic.csv', mode='r') as data:
            reader = csv.reader(data)
            # dict_from_csv = {rows[0]:rows[11] for rows in reader}
            for line in csv.reader(data):
                if line[0] == 'PassengerId':
                    continue
                
                tmp_dict = TitanicType()
                tmp_dict.PassengerId = int(line[0])
                tmp_dict.Survived = int(line[1])
                tmp_dict.Pclass = int(line[2])
                tmp_dict.Name = str(line[3])
                tmp_dict.Sex = str(line[4])
                tmp_dict.Age = float(line[5] or 0)
                tmp_dict.SibSp = int(line[6])
                tmp_dict.Parch = int(line[7])
                tmp_dict.Ticket = str(line[8])
                tmp_dict.Fare = float(line[9])
                tmp_dict.Cabin = str(line[10] or "")
                tmp_dict.Embarked = str(line[11] or "")
                dictionary.append(tmp_dict)

            
        # print(dict_from_csv)
        return dictionary
