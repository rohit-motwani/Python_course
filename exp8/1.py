import re
phone_list = []
with open('PhoneBook.txt', 'r') as my_file:
    
    for entry in my_file:
        phone_list.append(entry.split())

print("----------All Details----------")
print('\nSurname\tName\tPhone')
print('-'*30)       
for phone in phone_list:
    print(f'{phone[0]}\t{phone[1]}\t{phone[2]}\n')

print("----------Details only of surname Rao and first name starts with J or K----------")
print('\nSurname\tName\tPhone')
print('-'*30)

for phone in phone_list:
    
    check_fname_fletter = re.search('(^J.)|(^K.)', phone[1]) 
    check_sname=re.search('Rao',phone[0])
    if check_sname and check_fname_fletter:
        
        print(f'{phone[0]}\t{phone[1]}\t{phone[2]}\n')