class Dog :
    #클래스의 이름 정의
    def __init__(self, n, b):
        self.dog_name = n
        self.dog_breed = b
        self.dog_sex = "여"
    def bark(self):
        print(self.dog_breed, "개가 짖습니다.")

my_dog = Dog("뽀삐", "말티즈")
my_dog.bark()
my_dog.bark()
my_dog.bark()