class ReadJson:
    @staticmethod
    def geinputData():
        f = open("../testCase/datatoken.json", "r")
        return eval(f.read())
    @staticmethod
    def writetoafile(json):
        with open("../testCase/datatoken.json", 'w') as fp:
            fp.write(str(json))
  


