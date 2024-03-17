# Data Storage on Git Hub using Python 

This resporatory works as a cloud storage that can be maintained using python through the following modules and code

## Modules and Libreries

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Github.

```bash
pip install Github
```
or 
```bash
py -m pip install Github
```
## Usage

```python
class Storage:
    def __init__(self,token=<token>",resporatory="<resporatory>"):
        self.token = token
        self.resporatory = resporatory
        self.g = Github(token)
        self.repo = self.g.get_user().get_repo(resporatory)
        
    def uploadFile(self, file, folder=""):
        self.file_content = open(file, "rb").read()
        self.repo.create_file(folder+file, f"File uploaded [{file}]", self.file_content)

    def downloadFile(self, file, filePath=""):
        file = self.repo.get_contents(file)
        file_content = base64.b64decode(file.content)
        open(file.path, "wb").write(file_content)

    def deleteFile(self,file):
        file = self.repo.get_contents(file)
        self.repo.delete_file(file.path, f"File deleted [{file}]", file.sha)
        
    def showContents(self, folder=""):
        contents = self.repo.get_contents(folder)
        print(contents)
        return(contents)
```
```python
myStorage = Storage()
myStorage.uploadFile('<path of the file to upload on local computer>')
myStorage.downloadFile('<path of the file to download from github>')
myStorage.deleteFile('<path of the file to delete from github>')
myStorage.uploadFile('<path of the file to upload on local computer>',folder="<path of the folder on github>")
myStorage.showContents('<path of the folder of github>')
```


