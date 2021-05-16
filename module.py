class BusinessCard:

    def __init__(self, name, email, address, job, age, phone):
        """
        생성자 함수
        클래스가 복사되어 인스턴스가 생성될 때, 무조건 실행되는 함수..
        """
        self.name = name
        self.email = email
        self.address = address
        self.job = job
        self.age = age
        self.phone = phone
        
    def business_card(self):
        
        print("="*30)
        print('Name  : {}'.format(self.name))
        print('Email : {}'.format(self.email))
        print('Phone : {}'.format(self.phone))
        print("="*30)
        
    def detail_info(self):
        print("="*30)
        print('Job  : {}'.format(self.job))
        print('Age : {}'.format(self.age))
        print('Address : {}'.format(self.address))
        print("="*30)


class circle:
    pi = 3.14   #클래스 변수 - 모든 클래스 내에서 공유되는 변수
    def __init__(self, r):
        self.r = r   #인스턴스 변수 - 각각의 인스턴스 공유되는 변수
        
    def area(self):
        m = (self.r)*(self.r)
        return circle.pi*m
        
    def len_cir(self):
        return 2*(circle.pi)*self.r
        

def hello():
    print('hello python')
hello()