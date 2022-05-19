
from os.path import exists
import csv

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
class TitanicType():

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
    def __init__(self):
        self.Pclass = 0


    # def __str__(self) -> str:
    #     return "PassengerId: " + str(self.PassengerId) + '\n' + "Survived: " + str(self.Survived)  + '\n' + "Pclass: " + str(self.Pclass)  + '\n' + "Name: " + self.Name  + '\n' + "Sex: " + str(self.Sex)  + '\n' + "Age: " + str(self.Age)  + '\n' + 'SibSp' + str(self.SibSp)  + '\n' + "Parch: " + str(self.Parch)  + '\n' + "Ticket: " + (self.Ticket)  + '\n' +  "Fare: " + str(self.Fare)  + '\n' + "Cabin: " + str(self.Cabin)  + '\n' + "Embarked: " + str(self.Embarked) + '\n'
    #     return temp_dict


class GetData:
    """
    The class that gets the data from the csv file
    """
    def __init__(self):
        self.data = []
        self.file_name = "data.csv"

    def get_data(self) -> list[TitanicType]:
        """
        The actual function that gets the data from the csv file
        """
            
        file_exists = exists("./awesome-public-datasets/Datasets/titanic.csv/titanic.csv")

        if not file_exists:
            raise Exception("File not found (decompress the dataset and try again)")

        list: list[TitanicType] = []

        with open('./awesome-public-datasets/Datasets/titanic.csv/titanic.csv', mode='r') as data:
            # dict_from_csv = {rows[0]:rows[11] for rows in reader}
            for index, line in enumerate(csv.reader(data)):
                
                # option 1:
                if index == 0: continue
                
                # option 2:
                if index == 0: 
                    continue
                
                tmp_dict = TitanicType()
                print(tmp_dict.__dict__, tmp_dict.Pclass)
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
                print(tmp_dict.__dict__, tmp_dict.Pclass)
                print(tmp_dict)
                list.append(tmp_dict)

        print("inside loop")
        print(list)
        return list
