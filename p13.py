#4. Demonstrate use of Dictionaries methods


box_office = {"avatar":2009, "titanic":1997, "starwars":2015, "harrypotter":2011,
"avengers":2012}
box_office_fromkeys = box_office.fromkeys(box_office)
print('fromkeys method::',box_office_fromkeys)
box_office_fromkeys = box_office.fromkeys(box_office,"Billion Doller")
print(box_office_fromkeys)
print(f'get() method::{box_office.get("avatar")}')
print(f'items() method::{box_office.items()}')
print(f'keys() method::{box_office.keys()}')
print(f'values() method::{box_office.values()}')
box_office.update({'titanic':1998})
print(f'update() method::{box_office}')
box_office.pop("avatar")
print(f'pop() method::{box_office}')
box_office.popitem()
print(f'pop() method::{box_office}')
box_office.clear()
print(f'clear() method::{box_office}')
