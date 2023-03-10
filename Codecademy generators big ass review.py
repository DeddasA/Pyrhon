# def cs_courses():
#     yield 'Computer Science'
#     yield 'Artificial Intelligence'
 
# def art_courses():
#     yield 'Intro to Art'
#     yield 'Selecting Mediums'
 
 
# def all_courses():
#     yield from cs_courses()
#     yield from art_courses()
 
# combined_generator = all_courses()
# print(next(combined_generator))
# print(next(combined_generator))
# print(next(combined_generator))
# print(next(combined_generator))
# print(next(combined_generator))
# for c in combined_generator:
#     print(c[1])


# def science_students(x):
#   for i in range(1,x+1):
#     yield i

# def non_science_students(x,y):
#   for i in range(x,y+1):
#     yield i
  
# # Write your code below
# def combined_students():
#   yield from science_students(5)
#   yield from non_science_students(10,15)
#   yield from non_science_students(25,30)
  
# student_generator = combined_students()
# for c in student_generator:
#     print(c)
 
    
# def science_students(x):
#   for i in range(0,x+1):
#     yield i
# a = science_students(20)
# for b in a:
#     print(b)
 
 
 
# def number_generator():
#   i = 0
#   while True:
#     yield i
#     i += 1
 
# def even_number_generator(numbers):
#   for n in numbers:
#     if n % 3 == 1:
#       yield n
 
# even_numbers = even_number_generator(number_generator())
 
# for e in even_numbers:
#   print(e)
#   if e == 101:
#     break
# def course_generator():
#     yield ('Computer Science', 5)
#     # Checkpoint 1
#     yield ('Art', 10)
#     yield ('Business', 15)
# def add_five_students(courses):
#   for courses, num_students in courses:
#       num_students += 5
#       yield (courses,num_students)
   
# add_generator = add_five_students(course_generator())
# for a in add_generator:
#     print(a)

# days = 25
# gpas = [3.2, 4.0, 3.6, 2.9]

# def summa():
#     yield 'Summa Cum Laude'
# def magna():
#     yield 'Magna Cum Laude' 
# def cum_laude():
#     yield 'Cum Laude'
# # Write your code below:
# def graduation_countdown(days):
#     while days >= 0:
#       days_left = yield days
#       if days_left != None:
#         days = days_left
#       else:
#         days -= 1     
    
# days = 25
# countdown_generator = (day for day in range(days, -1,-1))
# grad_days = graduation_countdown(days)
# for day in grad_days:
#   print(day)
#   if day == 15:
#     grad_days.send(10)
#     print(day)
#   elif day == 3:
#     grad_days.close()
#     print ('Days Left:', day)

# def honors_generator(gpas):
#   for gpa in gpas:
#     if gpa > 3.9:
#       yield from summa()
#       print(gpa)
#     elif gpa > 3.7:
#       yield from magna()
#       print(gpa)
#     elif gpa > 3.5:
#       yield from cum_laude()
#       print(gpa)

# honors = honors_generator(gpas)
# for h in honors:
#   print(h)
 
def thot_slayer(days):
    while days >= 0:
      days_left = yield days
      if days_left != None:
        days = days_left
      else:
        days -= 1 
       
gen = thot_slayer(10)
for g in gen:
    # print(g)
    if g == 6:
        print('')
        gen.send(2)
    print(g)
    
    

