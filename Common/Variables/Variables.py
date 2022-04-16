import os
from pathlib import Path


class VariablesClass():
    defaultLogin = "testingyan94@gmail.com"
    defaultPassword = "InchkhEs22#"
    defaultSearchItem = "hiking boots for women"

    def generatePath(self):
        ROOT_DIR = Path(__file__).absolute().parent.parent.parent
        PATH = str(ROOT_DIR) + "\Common\Drivers\chromedriver.exe"
        PATH = PATH.replace("\\", "\\\\")
        print(PATH)
        return PATH


if __name__ == "__main__":
    obj = VariablesClass()
    obj.generatePath()
