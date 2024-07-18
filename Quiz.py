# ## Quiz 1 : 두 수의 덧셈, 뺄셈, 나눗셈, 곱셈 함수를 포함하는 클래스를 만들고 해당 클래스를 통해 객체 생성
#
# class 사칙연산계산기 :
#     def add (self, a,b) :
#         result = a + b
#         return result
#     def mul (self, a, b):
#         result = a * b
#         return result
#     def may (self, a, b) :
#         result = a / b
#         return result
#
# app = 사칙연산계산기()
# print(app.may(5,2))

# ## Quiz 2 : 게임 캐릭터 만들기, 게임 캐릭터 생성 클래스는 아이디, 성별, 직업 정보를 갖음. 기본 공격 함수를 갖음.
# ## 기본 공격 함수는 사용시 "공격!" 문자열을 화면에 출력
#
# class 캐릭터 :
#     def __init__(self, n, s, j, at) :
#         self.name = n
#         self.sex = s
#         self.job = j
#         self.att = at
#     def attack (self, en ) :
#         print(self.name , "이(가)" , en ,"을(를) 공격했다!")
#
# my_ch = 캐릭터("마지로","여","백수","얍")
# my_ch.attack("모니")

## Quiz 3 : 부동산 정보 입력 클래스, 위치, 평수, 건물의 종류, 가격, 건물이 지어진 년도 정보를 갖음.
## 정보 확인 함수를 사용하면 부동산 객체에 포함된 속성 정보를 화면에 출력

# class 부동산 :
#     def __init__ (self, l, sc, v, mon, y) :
#         self.location = l
#         self.scale = sc
#         self.var = v
#         self.money = mon
#         self.year = y
#     def check(self):
#         print(self.check)
#
# a = "강남"
# my_qwer = 부동산("a","b","c","d","e")

# ## Quiz 4 : 사용자 이름, 나이, 연락처를 입력 받아서 화면에 "입력하신 이름은 ~~~이며, 나이는 ~~~, 그리고 연락처는 0000000000입니다.
# ## 출력하는 프로그램 작성
#
# mn = input("이름을 입력해주세요. : ")
# aa = input("나이를 입력해주세요. : ")
# num = input("연락처를 입력해주세요. : ")
# class 회원가입 :
#
#     def __init__(self, mn, aa, num):
#         self.name = mn
#         self.age = aa
#         self.phone = num
#
#     def check_2(self):
#       print("입력하신 이름은 " , self.name, "이며, 나이는 " , self.age, "그리고 연락처는 " , self.phone, "입니다." )
# bb = 회원가입(mn,aa,num)
# bb.check_2()

## Quiz 5 : 문자 메시지 길이 판별 클래스. 문자 길이에 따라 문자 요금 결정 프로그램 작성
## 문자 길이에 따라 부과되는 요금은 클래스를 생성할 때 속성 정보로 갖게 된다. 요금이 부과될 문자 메시지의 길이를 정할 수 있도록 설정
## 이때 사용자로부터 문자메시지를 입력 받아서 문자 요금을 반환하는 코드 작성

class message :

    def __init__ (self, len, p, p2):
        self.len1 = len
        self.p1 = p
        self.p4 = p2
    def check(self, message):
        result = 0
        if len(message) <= self.len1:
            result = self.p1
        return result

        if len(message) > self.len1:
            result = self.p4
        return result

q = input("문자메세지를 입력해주세요. :")
my_ch = message(10,50,60)
print(my_ch.check(q))
