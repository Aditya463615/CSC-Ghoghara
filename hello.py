from github import Github
import base64

class Storage:
    def __init__(self,token="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",resporatory="CSC-Ghoghara"):
        self.token = token
        self.resporatory = resporatory
        self.g = Github(token)
        self.repo = self.g.get_user().get_repo(resporatory)
        
    def uploadFile(self, file, folder=""):
        self.file_content = open(file, "rb").read()
        self.repo.create_file(folder+file, "commit message", self.file_content)

    def downloadFile(self, file, filePath=""):
        file = self.repo.get_contents(file)
        file_content = base64.b64decode(file.content)
        open(file.path, "wb").write(file_content)

    def deleteFile(self,file):
        file = self.repo.get_contents(file)
        self.repo.delete_file(file.path, "commit message", file.sha)
        
    def showContents(self, folder=""):
        contents = self.repo.get_contents(folder)
        print(contents)
        return(contents)


myStorage = Storage()
myStorage.uploadFile('hello.py')
#myStorage.downloadFile('mrds.txt')
#myStorage.deleteFile('useless/Aditya.txt')
#myStorage.uploadFile('Aditya.txt',folder="useless/")
#myStorage.deleteFile('useless/Aditya.txt')
#myStorage.showContents()


