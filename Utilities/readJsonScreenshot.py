

class ReadJsonScreenshot:
    @staticmethod
    def geinputData():
        f = open("../testCase/screenshot.json", "r")
        return eval(f.read())
    @staticmethod
    def writetoafile(json):
        with open("../testCase/screenshot.json", 'w') as fp:
            fp.write(str(json))
  


