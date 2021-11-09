import ATM
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = ATM.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.A7_6r0eOSEZqsYiHswX4EenZ4QQfm6-IWki87EMN9UwFRQjBk8eMQt5Nxhg2BmttGOWfeuwYxY7994ftL1xnxqe0reWuuDMm97keDR9YqHvpMlPG4qJ2t4cYynPBpxoH957ErKk'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")
    # API v2
    transferData.upload_file(file_from, file_to)
    print ('file has been moved')
    
main()
