import os
import json
from datetime import date
import argparse

"""
+------| 10 / 13 / 2021 |-----------------------------------------------------+
| [x] Send email to Peyton Reddick                                            |
| [ ] Follow up with BPS                                                      |
+-----------------------------------------------------------------------------+

+------| 10 / 14 / 2021 |-----------------------------------------------------+
|                                                                             |
+-----------------------------------------------------------------------------+
"""

TABLE_WIDTH = 80

def get_date():
    today = date.today()
    return(today.strftime('%d-%m-%Y'))

def get_year():
    today = date.today()
    return(today.strftime('%Y'))

def get_month():
    today = date.today()
    return(today.strftime('%m'))

def get_day():
    today = date.today()
    return(today.strftime('%d'))

def date_exists(date):
    with open('data.json', 'r') as f:
        data = json.load(f)
        return (date in data['data'])

# write a task to current table
def write_task (date, text):

    new_task = {}
    new_task[date] = { 'text': text, 'done': False }

    if (date_exists(date)):
        with open('data.json', 'r+') as f:
            data = json.load(f)

            data['data'][date].append(new_task[date])
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    else:
        with open('data.json', 'r+') as f:
            data = json.load(f)

            data['data'][date] = []
            data['data'][date].append(new_task[date])
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            f.truncate()
        
    return 0

def complete_task ():
    return 0

# write a future task to current table
def write_future_task (date, text):
    return 0

def complete_future_task ():
    return 0

# Function for getting previous uncompleted tasks / future tasks to new table
def import_previous_tasks ():
    return 0

def get_terminal_size():
    size = os.get_terminal_size()
    columns = size[0]
    lines = size[1]
    return [columns, lines]

# Function to add line
def draw_task (text):
    print(f'| [ ] {text} |')

    return 0

# function for getting the max width of a task in order to keep table shape
def get_max_task_width():
    return 0

def get_user_day():
    input_string = '__-{}-{} [ENTER=today, q=quit]\n> '.format(get_month(),
                                                                   get_year())
    day = input(input_string)

    while (not day.isdigit() and day != '' and day != 'q'):
        print('INVALID DAY\n')
        day = input(input_string)

    if (day == ''):
        day = get_day()

    if (day == 'q'):
        exit(0)

    print('{} / {} / {}'.format(day, get_month(), get_year()))

    return day


# getting a task from the user
def request_task():
    task_name = input('task: ')
    task_date_day = get_user_day()

    date = '{}-{}-{}'.format(task_date_day, get_month(), get_year())

    write_task(date, task_name)
    print('TASK CREATED\n---')
    print('{} | {}'.format(date, task_name))
    print('---')

    return 0

def print_date_line(date):
    pre_string = '+{}|{}|'.format('-' * 60, date)
    print('{}{}+'.format(pre_string, '-' * (TABLE_WIDTH - len(pre_string) - 1)))

def print_bottom_line():
    print('+{}+\n'.format('-' * (TABLE_WIDTH - 2)))

def print_table(date):
    with open('data.json', 'r') as f:
        data = json.load(f)

        if (date in data['data']):
            tasks = data['data'][date]
        else:
            tasks = []

        if (len(tasks) > 0):
            print_date_line(date)
            for task in tasks:
                done = 'X' if task['done'] else ' '
                pre_string = '| [{}] {}'.format(done, task['text'])
                print('{}{}|'.format(pre_string, ' ' * (TABLE_WIDTH - len(pre_string) - 1)))
            print_bottom_line()
            return True
        else:
            print_date_line(date)
            return False


def print_tasks():
    day = get_day()
    month = get_month()
    year = get_year()

    days_to_print = 7

    # iterating next 7 days
    for i in range(0, days_to_print):
        date = '{}-{}-{}'.format(int(day) + i, month, year)

        print_table(date)


def delete_task(date, index):
    return 0

def finish_task():
    day = get_user_day()
    date = '{}-{}-{}'.format(day, get_month(), get_year())

    with open('data.json', 'r') as f:
        data = json.load(f)

        tasks = data['data'][date]
        
        for i, task in enumerate(tasks):
            print('{} | {}'.format(i, task['text']))

        complete = int(input('\n# of completed task\n>'))

        # TODO not replacing done field
        if (complete <= len(tasks)):
            data['data'][date][complete]['done'] = 'true'
        else:
            print('invalid task #')
    


        
    
    
    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--create', dest='create', 
                              action='store_true', 
                              help='create a new task')
    parser.add_argument('-p', '--print', dest='display', 
                              action='store_true', 
                              help='display all tasks')
    parser.add_argument('-f', '--finish', dest='finish', 
                              action='store_true', 
                              help='mark a task as finished')

    args = parser.parse_args()

    if (args.create):
        request_task()
    elif (args.display):
        print_tasks()
    elif (args.finish):
        finish_task()
    else:
        print('No arguements given... (-h for help)')


if __name__ == '__main__':
    main()
