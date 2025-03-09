import pyzipper

class FileHandler:
    def __init__(self, file_path):
        self.path = file_path

    def get_path(self) -> str:
        return self.path

    def get_file_extension(self) -> str:
        file = self.get_path()
        dot_index = file.rfind('.')

        if dot_index == -1:
            print('there is no extension for that file')
            return False
        
        file_extension = file[dot_index:]
        
        return file_extension
    
    def extract_content(self, password, extract_directory):
        file = self.get_path()
        with pyzipper.AESZipFile(file, 'r') as zip_file:
            zip_file.extractall(extract_directory, pwd=password.encode())

    def verify_password(self, password):
        try:
            file_path = self.get_path()

            with pyzipper.AESZipFile(file_path, 'r') as encrypted_file:
                encrypted_file.setpassword(password.encode()) #on encode car les algos de chiffrement manipules la data brutes (donc en bytes)
                file_list = encrypted_file.namelist()

                with encrypted_file.open(file_list[0]) as extracted_file:
                    extracted_file.read(1)     
                return True
            
        except:
            return False
    
    def create_file(self, file_name):
        with open(f'{file_name}', 'x'):
            pass

    def write_in_file(self, data, file_path):
        if type(data) == 'list':
            with open(file_path, 'w') as file:
                for word in data:
                    file.write(f'{word}\n')


    def open_with_password(self, password):
        try :
            self.extract_content(password,'./extract')
        except:
            'something happend when opening file'