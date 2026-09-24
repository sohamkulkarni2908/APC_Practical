from abc import ABC, abstractmethod
class CloudStorage(ABC):
    @abstractmethod
    def upload(self):
        pass

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class GoogleDrive(CloudStorage):

    def upload(self):
        print("File uploaded to Google Drive")

    def download(self):
        print("File downloaded from Google Drive")

    def delete(self):
        print("File deleted from Google Drive")

class OneDrive(CloudStorage):

    def upload(self):
        print("File uploaded to OneDrive")

    def download(self):
        print("File downloaded from OneDrive")

    def delete(self):
        print("File deleted from OneDrive")

drive = GoogleDrive()
one_drive = OneDrive()
drive.upload()
drive.download()
drive.delete()
one_drive.upload()
one_drive.download()
one_drive.delete()