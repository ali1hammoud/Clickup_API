#!/usr/local/bin/python3

import pandas as pd
from func import get_spaces, get_lists, get_tasks 

if __name__ == '__main__':
    print("\nClickUp data extraction process starts")

    api_token = input('enter your API: ')
    #team_id or space_id is nothing but workspace ID which you will find in URL after login in to ClickCup
    team_id = input('enter your team id: ')
    
    spaces = get_spaces(api_token,team_id)
    print('Extract spaces Done...\n')
    for  i, space in enumerate(spaces, start=0):
        print(f'{i}- {space[0]}')
    space_id = int(input('\nWhich space do you want? \nWrite the number: '))
    
    lists = get_lists(api_token, spaces[space_id][1])
    print('\nExtract lists Done...')
    for  i, list_clickup in enumerate(lists, start=0):
        print(f'{i}- {list_clickup[0]}')
    print(f'{i+1}- All')
    list_id = int(input('\nWhich list do you want? \nWrite the number: '))
    if list_id == i+1:
        all_lists_tasks = []
        print('Starting extraction all task from all list ...')
        for list_clickup in lists:
            tasks = get_tasks(api_token, list_clickup[1])
            for tt in tasks:
                all_lists_tasks.append(tt)
            print(f'{list_clickup[0]} -> Done.')
        df = pd.DataFrame(all_lists_tasks, columns= ['list', 'names', 'status', 'date_created', 'assignees', 'due_date', 'tags'])
        df.to_csv('all_tasks.csv', sep=',', encoding='utf-8')
        print('All data saved to CSV file.')                
    else:
        tasks = get_tasks(api_token, lists[list_id][1])
        df = pd.DataFrame(tasks, columns= ['list', 'names', 'status', 'date_created', 'assignees', 'due_date', 'tags'])
        df.to_csv(f'{lists[list_id][0]}_tasks.csv', sep=',', encoding='utf-8')
        print(F'All data saved from {lists[list_id][0]} to {lists[list_id][0]}_tasks.csv file.') 
    print("\nClickUp Analytics Process Finished.")