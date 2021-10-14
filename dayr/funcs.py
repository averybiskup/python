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
    input_string = 'day [ENTER=today, q=quit]\n> '
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
    pre_string = '+---------------------| {} |'.format(date)
    print('{}{}+'.format(pre_string, '-' * (80 - len(pre_string) - 1)))

def print_bottom_line():
    print('+{}+'.format('-' * 78))

def print_tasks(date):
    with open('data.json', 'r') as f:
        data = json.load(f)
        if (date not in data['data'] or len(data['data'][date]) == 0):
            print('Empty Task List')
        else:
            print_date_line(date)
            for task in data['data'][date]:
                done = 'X' if task['done'] else ' '
                pre_string = '| [{}] {}'.format(done, task['text'])
                print('{}{}|'.format(pre_string, ' ' * (80 - len(pre_string) - 1)))

    print_bottom_line()


def draw_table(title):
    return 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--create', dest='create', 
                              action='store_true', 
                              help='create a new task')
    parser.add_argument('-p', '--print', dest='display', 
                              action='store_true', 
                              help='display all tasks')

    args = parser.parse_args()

    if (args.create):
        request_task()
    elif (args.display):
        print_tasks(get_date())
    else:
        print('No arguements given... (-h for help)')


if __name__ == '__main__':
    main()
