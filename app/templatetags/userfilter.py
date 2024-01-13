from django import template
register=template.Library()

def swap(value):
    return value.swapcase()

def remove(value,arg):
    return value.replace(arg,'')

def count(value,arg):
    c=0
    for ip in range(len(value)):
        if arg==value[ip:len(arg)+ip:1]:
            c+=1

    return c

register.filter('swap',swap)
register.filter('remove',remove)
register.filter('count',count)