In This milestone you will be implementing a basic command line program that lets you manage your tasks.

The specification for this pogram is as follows,

## Specification

You are asked to build a command line program that lets you manage your tasks. Each task is associated with a priority, the priority is a number that denotes how important a task is, note that the value of the priority is inversed ( lower the value highest the priority).

1. The incomplete version of the program can found in the file `solve_me.py`

2. Priority can be any integer _greater than_ or _equal to_ 1. 1 being the highest priority

3. Two tasks cannot have the same priority, If a new task is added with an existing priority, the priority of the existing task will be increased by 1.

## Usage

### 1. Help

Executing the command without any arguments, or with a single argument help prints the CLI usage.

```
$ python tasks.py help
Usage :-
$ python tasks.py add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ python tasks.py ls                   # Show incomplete priority list items sorted by priority in ascending order
$ python tasks.py del PRIORITY_NUMBER  # Delete the incomplete item with the given priority
$ python tasks.py done PRIORITY_NUMBER # Mark the incomplete item with the given priority as complete
$ python tasks.py help                 # Show usage
$ python tasks.py report               # Statistics
```

### 2. List all pending items

Use the ls command to see all the items that are not yet complete, in ascending order of priority.

Every item should be printed on a new line. with the following format

```
[index] [task] [priority]
```

Example:

```
$ ./tasks ls
1. change light bulb [2]
2. water the plants [5]
```

index starts from 1, this is used to identify a particular task to complete or delete it.

### 3. Add a new item

Use the add command. The text of the task should be enclosed within double quotes (otherwise only the first word is considered as the item text, and the remaining words are treated as different arguments).

```
$ ./tasks add 5 "the thing i need to do"
Added task: "the thing i need to do" with priority 5
```

### 4. Delete an item

Use the del command to remove an item by its priority.

```
$ ./tasks delete 3
Deleted item with priority 3
```

Attempting to delete a non-existent item should display an error message.

```
$ ./tasks delete 5
Error: item with priority 5 does not exist. Nothing deleted.
```

### 5. Mark a task as completed

Use the done command to mark an item as completed by its priority.

```
$ ./tasks done 1
Marked item as done.
```

Attempting to mark a non-existed item as completed will display an error message.

```
$ ./tasks done 5
Error: no incomplete item with priority 5 exists.
```

### 6. Generate a report

Show the number of complete and incomplete items in the list. and the complete and incomplete items grouped together.

```
$ ./tasks report
Pending : 2
1. this is a pending task [1]
2. this is a pending task with priority [4]

Completed : 3
1. completed task
2. another completed task
3. yet another completed task
```

## Testing

Run the test.py file to test if your submission is correct.
The test.py file will run your program and compare the output with the expected output. Any errors in your implementation will be displayed.

## Submission

You can find the incomplete code and the instructions to complete it in the following GitHub repository. ( Fork this repo to get started )

https://github.com/DjangoForAll/GDC-Level-2-Milestone