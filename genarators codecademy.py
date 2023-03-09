# # throw

# def student_counter():
#   for i in range(1,5001):
#     yield i

# student_generator = student_counter()
# for student_id in student_generator:
#   # Write your code below:
#  for student_id in student_generator:
#      if student_id == 100:
#          student_generator.throw(ValueError,"Invalid student ID")
# print(student_id)


# #student_idMAX_STUDENTS = 50

# def get_student_ids():
#   student_id = 1
#   while student_id <= MAX_STUDENTS:
#     # Write your code below
#     n = yield student_id
#     if n is not None:
#       student_id = n
#       continue
    

    
#     student_id += 1

# student_id_generator = get_student_ids()
# for i in student_id_generator:
#   # Write your code below
#   if i == 1:
#     i = student_id_generator.send(25)

#   print(i)
class generator_stopper(Exception):
    pass

def student_counter():
    for i in range(1, 5001):
        try:
            yield i
        except generator_stopper:
            print('End of this generator, see ya later')
            break

try:
    student_generator = student_counter()
    for student_id in student_generator:
        if student_id == 100:
            student_generator.throw(generator_stopper)
        print(student_id)
except generator_stopper as e:
    print(e)

  
# def generator():
#   i = 0
#   while True:
#     try:
#       yield i
#     except GeneratorExit:
#       print("Early exit, BYE!")
#       break
#     i += 1
 
# my_generator = generator()
# for item in my_generator:
#   print(item)
#   if item == 1:
#     my_generator.close()
  
def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  if student_id == 100:
    student_generator.close()
  print(student_id)
  