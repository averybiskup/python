import os

"""
+------| TASKS (order of importance) |----------------------------------------+
| [x] Send email to Peyton Reddick                                            |
| [ ] Follow up with BPS                                                      |
+-----------------------------------------------------------------------------+

+------| UPCOMING (chronological order) |-------------------------------------+
|                                                                             |
+-----------------------------------------------------------------------------+
"""

# write a task to current table
def write_task (date, id, text, importance):
    return 0

def complete_task (id):
    return 0

# write a future task to current table
def write_future_task (date, id, text):
    return 0
def complete_future_task (id):
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

# getting a task from the user
def request_task ():
    return 0

# create a new file for the given date
def create_new_file ():
    return 0

def draw_new_table (title):
    return 0

def main():
    draw_task('test drawing man this is cool')

if __name__ == '__main__':
    main()
