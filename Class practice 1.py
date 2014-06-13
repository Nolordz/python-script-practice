""" Create Two classes,an Employee and a Job,where the employee class (has-a) job class and print My Name is Morgan Williams
 I am 24 years old and I am a Software Developer."""

"""class Job (object):
    def __init__(self,title):
     self.title = title

class Employee ():
    def __init__(self,name,age,title):
        self.name = name
        self.age = age
        self.job = Job (title)


    def talk (self):
        print "My name is %s, I'm %s years old and I am a %s" % (self.name, self.age, self.job.title )

employee = Employee('Morgan Williams', 24, 'Software Developer')

employee.talk()"""

class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def tastesLike(self):
        raise NotImplementedError("Subclasses are responsible for creating this method")


class HotDog(Food):
    def tastesLike(self):
        return("Extremely processed meat")


class Hamburger(Food):
    def tastesLike(self):
        return("grilled goodness")


class ChickenPatty(Food):
    def tastesLike(self):
        return("chicken")

dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Micky Mouse shaped Chicken Tenders', 170))

for course in dinner:
    print "%s is type %s"%(course.name,type(course))
    print "has %s calories"%(course.calories)
    print "and tastes like %s"%(course.tastesLike())




















