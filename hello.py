class namegreeter:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f"{self.name} ,how can i help you today jacob?")

ng=namegreeter("sam")
ng.greet()