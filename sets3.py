a = {'a','b','c'}
print(a)

a = set(('a','b','c'))
print(type(a))

a: set ={'a','b','c'}
print(type(a))

#create
#add:
a: set = {'a','b','c'}
a.add('d')
print(a)

#update:
a: set = {'a','b','c'}
b: set = { 'a','c','d'}
a.update('b')

#remove
a: set = {'a','b','c'}
a.remove('b')
print(a)
