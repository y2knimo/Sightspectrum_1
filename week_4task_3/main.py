
def fun(name):
    print("Maybe " + name)
fun("more")
fun("mani")
fun("your self Gopi")

def fun(*name):
    print("Always kill by " + name[1])
fun("Gopi" , "kishore")

def fun(name3,name2,name1):
    print("The small age child is " + name3)
fun(name1="Gopi",name2="Kishore",name3="Mani")


def fun(**kid):
    print("What have " + kid["last"])
fun(first=" Gopi",last=" I Think so")

