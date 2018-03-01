
Mylist = [{'id':1,'name':'Harsh','address':'Kunal Icon'},
          {'id':2,'name':'Jon','address':'Rose Vally'},
          {'id':3,'name':'Harry','address':'RoseLand'}]


#Insert:-->
list = []
def Insert():
    for i in range(3):
        d = {}
        d['id'] = input('Enter id: ')
        d['name'] = raw_input('Enter name: ')
        d['address'] = raw_input('Enter address: ')
        Mylist.append(d)
    print list

#For Searching:-->
def Search():
    item = input("Enter id to display: ")
    for i in Mylist:
        if i['id'] == item:
            print i

#For Remove:-->
def Remove():
    Id = input("Enter id for remove: ")
    for i in Mylist:
        if i['id'] == Id:
            Mylist.remove(i)
    print Mylist