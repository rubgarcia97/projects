import eurostat
import csv
import os

class EurostatAPIClient():

    def __init__(self):
        # self.__name = name

        self.__pars = None

    def get_repository(self):
    
        repo = eurostat.get_toc_df()
        dic = repo.set_index('title')['code'].to_dict()
        
        return dic

    def get_params (self):
        self.__pars = eurostat.get_pars(self.__name)
        

    def get_dic(self):
        self.get_params()
        dic = eurostat.get_dic(self.__name,self.__pars[2],full=True, frmt="list",lang="en")
        print(dic)

    def get_database (self, code):
        
        eurostat.get_data(code)


class GUIToolkit ():

    def __init__(self):
        pass

    def current_text(self,s):

        self.selected_option = s

    def push_button (self):

        pass


    def download_database (self,code):

        if code is not None:

            ruta = './data'
            os.chdir(ruta)

            eurostat.get_data(code)

    

       


        
