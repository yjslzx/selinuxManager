import os
class TypeEnforceFileManager:
    
    """
    This class is used to manage the type enforce file
    """

    def __init__(self, env_path):
        self.env_path = env_path
        self.file_list = []
    
    def add_file(self, file_path):
        self.file_list.append(file_path)
        print("Added file: " + file_path)

    def remove_file(self, file_path):
        self.file_list.remove(file_path)
        print("Removed file: " + file_path)
    
    def init_file_list(self):
        """
        Initialize the file list from the root folder of the project, which contains just te files
        """
        for root, dirs, files in os.walk(self.env_path):
            for file in files:
                if file.endswith(".te"):
                    file_path = os.path.join(root, file)
                    self.add_file(file_path)



class SELinuxManager:

    def __init__(self):
        # TODO: initialize
        type_enforce_file_manager = TypeEnforceFileManager(r"..\test\env")
        type_enforce_file_manager.init_file_list()
        print(type_enforce_file_manager.file_list)
        print("SELinuxManager initialized")

def main():
    se_manager = SELinuxManager()

if __name__ == '__main__':
    main()