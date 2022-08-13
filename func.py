import sys
import json
import requests
import time

 
def get_spaces(api_token,team_id):
    try:
        url = "https://api.clickup.com/api/v2/team/%s/space?archived=false"%team_id
 
        headers = {"Authorization": api_token}
        r = requests.get(url = url, headers = headers)
        response_dict = json.loads(r.text)
        #print(response_dict)
        
        spaces = response_dict["spaces"]
        spaces_names_ids = []

        if spaces:
            for space in spaces:
                space_id = space['id']
                space_name = space['name']
                spaces_names_ids.append([space_name, space_id])
                #print(f"\nspace name : {space_name} | Space id : {space_id} ")
 
    except:
        print("\n*** Connection Failed *** ",sys.exc_info())
    
    return spaces_names_ids
 
def get_lists(api_token, space_id):
    try:
        url = f"https://api.clickup.com/api/v2/space/{space_id}/list"
 
        headers = {"Authorization": api_token}
        r = requests.get(url = url, headers = headers)
        response_dict = json.loads(r.text)
        #print(response_dict)
        
        lists = response_dict["lists"]
        lists_names_ids = []

        if lists:
            for list_ in lists:
                list_id = list_['id']
                list_name = list_['name']
                lists_names_ids.append([list_name, list_id])
                #print(f"\nList name : {list_name} | List id : {list_id} ")

    except:
        print("\n*** Function (get_task_member) Failed *** ",sys.exc_info())
 
    return lists_names_ids

def get_tasks(api_token,list_id):
    tasks_names_status_date_created_assignees_due_date_tags = []
    try:
        url = f"https://api.clickup.com/api/v2/list/{list_id}/task"
 
        headers = {"Authorization": api_token}
        r = requests.get(url = url, headers = headers)
        response_dict = json.loads(r.text)
        #print(response_dict)
        tasks = response_dict['tasks']
        tasks_names_status_date_created_assignees_due_date_tags = []
        if tasks:
            for task in tasks:
                task_list = task['list']['name']
                task_title = task['name']
                task_status = task['status']['status']
                task_date_created = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(task['date_created'])/1000))
                task_assignees_dict = task['assignees']
                if task_assignees_dict:
                    task_assignees = task_assignees_dict[0]['username']
                else:
                    task_assignees = None
                
                if task['due_date']:
                    task_due_date = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(task['due_date'])/1000))
                else:
                    task_due_date = None
                task_tags_dict = task['tags']
                if task_tags_dict:
                    task_tags = task_tags_dict[0]['name']
                else:
                    task_tags = None
                
                tasks_names_status_date_created_assignees_due_date_tags.append([task_list, task_title, task_status, task_date_created, task_assignees, task_due_date, task_tags])
        return tasks_names_status_date_created_assignees_due_date_tags
    except:
        print("\n*** Failed >>> ", sys.exc_info())