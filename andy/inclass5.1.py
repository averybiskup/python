def get_login_name(first, last, id):
    first = first[0:3]
    last = last[0:3]

    new_id = []
    for i in list(id):
        if i.isdecimal():
            new_id.append(i)

    new_id = ''.join(new_id[-3:])


    return first + last + new_id

print(get_login_name('Amanda', 'Spencer', 'ENG6721'))
print(get_login_name('Spencer', 'Amanda', 'WE34221'))
print(get_login_name('Amanda', 'Tanner', 'CCSF325234'))
print(get_login_name('Tina', 'Spencer', 'Y12451'))
