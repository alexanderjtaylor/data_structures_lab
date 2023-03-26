
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
pi = 3.141592653589793238462643
num = int(pi)
print(num)

food = {"Apple", "Peach", "Banana", "Cucumber", "Asparagus"}
food.add("Grapes")
food.add("Blackberries")
food.add("Celery")
food.add("Avocado")
for i in food:
    print(i)

user = {
    "first_name": "Alex",
    "last_name": "Taylor",
    "email": "alex@gmail.com",
    "phone_number": "3151231234",
}
print("The user's name is {} {} and contact info is {}, {}".format(user["first_name"], user["last_name"], user["email"], user["phone_number"]))



family_list = [
    {
        "first_name": "Bob",
        "last_name": "Taylor",
        "relation": "father",}, 
    {
        "first_name": "Dianne",
        "last_name": "Taylor",
        "relation": "mother",}, 
    {
        "first_name": "Jacob",
        "last_name": "Taylor",
        "relation": "son",}]

def family(x):
    for i in x:
        print(i["first_name"], i["relation"])

family(family_list)