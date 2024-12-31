class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = self.filepath.split('/')[-1]
    def extension(self):
        return self.file.split(".")[-1]
    def filename(self):
        return self.file.split(".")[-2]
    def dirpath(self):
        return self.filepath.split(self.file)[0]

test = FileMaster('/Users/person1/Pictures/house.png')
print(test.extension())
print(test.filename())
print(test.dirpath())