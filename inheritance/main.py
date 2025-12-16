from Single_Inheritance import Vehicle, Car
from Multiple_Inheritance import Person, Student, ClassRepresentative
from Multilevel_Inheritance import Book, PrintedBook, EBook 
from Hierarchical_Inheritance import Animal, Dog, Cat   
from Hybrid_Inheritance import DepartmentHead   

print("------------- Single Inheritance -------------------")
car1 = Car("Tesla")
car1.info()  
car1.drive()      
print("\n------------- Multiple Inheritance -----------------")
rep = ClassRepresentative("Kenneth")
rep.show_role()
rep.assign_section("2B")
print("\n------------- Multilevel Inheritance ---------------")
ebook = EBook("One Piece", "Eiichiro Oda", 250, 50)
ebook.info()           
ebook.printed_info()   
ebook.ebook_info()     
print("\n------------- Hierarchical Inheritance -------------")
dog1 = Dog("Max")
cat1 = Cat("Luna")
dog1.eat()    
dog1.bark()   
cat1.eat()    
cat1.meow()   
print("\n------------- Hybrid Inheritance -------------------")
head = DepartmentHead("Sir Haber","OOP","Information System Department")
head.teach()
head.course_info()
head.lead_department()
