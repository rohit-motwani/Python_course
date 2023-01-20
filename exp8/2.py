import re
cities_list = []
with open('Cities.txt', 'r') as my_file:
    
    for entry in my_file:
        cities_list.append(entry.split())

n=0
b=len(cities_list)
while(n<4):
    print("--------------Option-----------------\n1. Find all cities ending with “ai”\n2. Find all cities starting with “Mu” or “Ma”\n3. print name of cities with [u] as second letter and [a] as second last letter")
    n=int(input("Enter your choice : "))
    match n:
        case 1:
            cities=[]
            for cities in cities_list:
                check_end=re.search('(ai$)',cities[0])
                if check_end:
                    print(f'{cities[0]}')
        case 2:   
            cities=[]
            for cities in cities_list:
                check_end=re.search('(^Mu)|(^Ma)',cities[0])
                if check_end:
                    print(f'{cities[0]}')
        case 3:
            cities=[]
            i=0
            for cities in cities_list:
                check_end=re.search('(^.u)',cities[0])
                check_slletter=re.search('a.$',cities[0])
                if check_end and check_slletter:
                    print(f'{cities[0]}')
        