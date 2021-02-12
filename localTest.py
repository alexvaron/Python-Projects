# problem3.py
# when do_nonlocal(), it sets spam to the nonlocal spam which is printed
# when do_global(), it prints the non local spam
# when scope_test(), the global spam is printed
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
        spam = "test spam"
    do_local()
    print ("local:", spam)
    do_nonlocal()
    rint("nonlocal:", spam)
    do_global()
    print("global:",spam)
scope_test()
print("global scope:", spam)
