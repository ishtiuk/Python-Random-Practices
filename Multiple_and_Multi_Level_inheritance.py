class Dad:
    dancing = 8
    
    def print_dance(self):
        return f"hey, I danced for {self.dancing} times"

class Son(Dad):
    badminton = 7

    def __init__(self):
        self.languages = ['C', 'PHP']
        self.skills = 'Driving'

class Grand_son(Son):
    cricket = 6

    def __init__(self, languages, skils):
        # self.languages = languages
        # self.skills = skils
        Son.__init__(self)
        super().__init__()
        # Dad.print_dance(self)
        self.languages = languages
        self.skills = skils
        
        
ran = Son()
print(ran.languages, '||', ran.skills)

rohim = Grand_son(['Python', 'C++'], 'Blog Writting')

print(rohim.skills, '||', rohim.languages)