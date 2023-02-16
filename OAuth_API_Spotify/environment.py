import os
import json


class Environment():

    def __init__(self):
        
        self.__parent_dir = os.getcwd()
        self.__path = None

    def create_folder(self,directory=str):

        self.__path = os.path.join(self.__parent_dir, directory)
        try:
            os.mkdir(self.__path)
            print("Directory {} created at {}".format(directory,self.__parent_dir))
        except FileExistsError:
            
            print("ERROR : Directory {} already exist at {}".format(directory,self.__parent_dir))



    def create_image(self,file_name,content):

        if self.__path == None:
            path_image = file_name

            with open (path_image, "wb") as file:
                file.write(content)
        
        else:

            path_image = os.path.join(self.__path,file_name)
            
            with open (path_image, "wb") as file:
                file.write(content)
            

    def create_file(self,file_name,content):

        if self.__path == None:
            path_file = file_name

            with open(path_file, "w") as file:
                file.write(json.dumps(content))
            file.closed
        else:
            path_file = os.path.join(self.__path,file_name)

            with open(path_file, "w") as file:
                file.write(json.dumps(content))
            file.closed