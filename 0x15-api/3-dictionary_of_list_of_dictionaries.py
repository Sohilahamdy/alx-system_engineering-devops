#!/usr/bin/python3
import json
import requests

def fetch_data():
    # Replace with actual URLs for the users and todos endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)
    
    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data")
        return None, None
    
    users = users_response.json()
    todos = todos_response.json()
    
    return users, todos

def export_data_to_json(users, todos):
    # Create a dictionary to hold the data in the required format
    data = {}
    
    # Populate the dictionary with user IDs and their tasks
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        data[user_id] = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos if todo['userId'] == user['id']
        ]
    
    # Write the dictionary to a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f, indent=4)

def main():
    users, todos = fetch_data()
    if users and todos:
        export_data_to_json(users, todos)

if __name__ == "__main__":
    main()
