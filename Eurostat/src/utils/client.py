import eurostat

class EurostatAPIClient():

    def __init__(self):
        # self.__name = name

        self.__pars = None

    def get_repository(self):
    
        toc = eurostat.get_toc()
        repo = [toc[i][0] for i in range(1, len(toc))]
        
        return repo

    def get_params (self):
        self.__pars = eurostat.get_pars(self.__name)
        

    def get_dic(self):
        self.get_params()
        dic = eurostat.get_dic(self.__name,self.__pars[2],full=True, frmt="list",lang="en")
        print(dic)

    def database (self):
        print('Hello')
