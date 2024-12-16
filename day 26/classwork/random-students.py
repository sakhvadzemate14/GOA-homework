<<<<<<< HEAD
#შევქმნათ პროგრამა რომელსაც გადავსცემთ  მოსწავლეევბის სახელებს  შემდეგ კი ეს  პროგრამა ამ სახელებიდან რენდომულად ამოარჩევს თითოეულს
#და გაანაწილებს  ჯგუფებში


# list :
    #oppend-ლისტის ბოლოს ამატებს ახალ ელემენტს
    #remove-სიიდან შლის  ნებისმიერ ელემენტს
    

#tf else 



#loop
#random




import  random


group19_students = ["მათე სახვაძე", "ილიკო რაჯებაშვილიი", "მათე ფირანიშვილი", "ლუკა გოგოხია", "ნიკოლოზ კოტრიკიძე" ,"ნიკა სოსელია","ირაკლი დუდაშვილი","ირაკლი გელაძე","გიორგი ჭყონია","გიორგი წიბლიაშვილი"]


all_group = []
group=[]

while group19_students != []:
    random_student = random.choice(group19_students)
    group.append(random_student)
    group19_students.remove(random_student)


if   len(group) ==3:
 all_group.append(group)
group = []

random_group = random.choice(all_group)
random_group.append(group[0])




for i in range (3):
    print(all_group [i])


print(group)

#choice-არჩევა









=======
#შევქმნათ პროგრამა რომელსაც გადავსცემთ  მოსწავლეევბის სახელებს  შემდეგ კი ეს  პროგრამა ამ სახელებიდან რენდომულად ამოარჩევს თითოეულს
#და გაანაწილებს  ჯგუფებში


# list :
    #oppend-ლისტის ბოლოს ამატებს ახალ ელემენტს
    #remove-სიიდან შლის  ნებისმიერ ელემენტს
    

#tf else 



#loop
#random




import  random


group19_students = ["მათე სახვაძე", "ილიკო რაჯებაშვილიი", "მათე ფირანიშვილი", "ლუკა გოგოხია", "ნიკოლოზ კოტრიკიძე" ,"ნიკა სოსელია","ირაკლი დუდაშვილი","ირაკლი გელაძე","გიორგი ჭყონია","გიორგი წიბლიაშვილი"]


all_group = []
group=[]

while group19_students != []:
    random_student = random.choice(group19_students)
    group.append(random_student)
    group19_students.remove(random_student)


if   len(group) ==3:
 all_group.append(group)
group = []

random_group = random.choice(all_group)
random_group.append(group[0])




for i in range (3):
    print(all_group [i])


print(group)

#choice-არჩევა









>>>>>>> 8bf49274b65ebb4a3d2fc3df339420b04dd27c5b
