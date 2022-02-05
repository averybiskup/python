#!/usr/bin/python3

import argparse

PATH = '../../personal/todo.txt'

def print_todo():
  with open(PATH, "r") as f:
    print(f.read())

def add_item(name):
  with open(PATH, "a+") as f:
    f.write(name + "\n")

def clear_todo():
  with open(PATH, "r+") as f:
    f.truncate(0)

def add_input():
  print("add items below:")

  _input = input(">")
  if (_input != "q"):
    add_item(_input)

  while (_input != "q"):
    _input = input(">")
    if (_input != "q"):
        add_item(_input)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-a', '--add-item', dest='add', 
                            action='store_true',
                            help='add item to todo list')
  parser.add_argument('-p', '--print', dest='display',
                            action='store_true',
                            help='print the entire todo list')
  parser.add_argument('-c', '--clear', dest='clear',
                            action='store_true',
                            help='clear entire todo list')

  args = parser.parse_args()

  if (args.add):
    add_input()
  elif (args.display):
    print_todo()
  elif (args.clear):
    clear_todo()
  else:
     print('No args given, -h for help') 

if __name__ == "__main__":
  main()
