Now that we have seen what python can do, let's take it for a test drive and observe various ways to solve a problem.

we won't be going deep into algorithms or advanced python data structures, but just enough to help you complete your milestone, we'll include links for further reading if you are interested

Programming a simple countdown.

A countdown is a simple program that counts down from a given number until 0. There are a couple of ways to solve this problem, let's take a look at each one

- Using While loops and logic

```python
i = 10
while i >= 0:
    print(i)
    i = i - 1 # Can also be written as i -= 1
```

- Using the range function with for loops

```python
for i in range(10,0,-1): # Only counts till 1
    print(i)
```

- Or using functions

```python
def countdown(number):
    if number < 0:
        return
    print(number)
    countdown(number - 1)
countdown(10)
```

The above solution involves recursive functions, recursive functions are functions that call themselves. These are tricky to comprehend and can be hard to debug but they are used to solve certain types of problems very easily. If you observe the code snippet, you can see that that the function behaves differently depending on the value of the number parameter.

The condition that stops the recursion is called the base case, without the base case condition the recursion will keep going forever and the program will crash. Try it out and see what happens.

In the above example, the base condition is triggered when the value of the parameter number drops below 0, at this point, we don't want the countdown to continue and we want to stop execution. This is our base case, In all other cases, the function will call itself with a decremented value for the parameter number.

> Let's say you are standing in a long line of people, you wanted to know how many people are in front of you. So you ask the person in front of you how many people are standing in front of them, and they ask the same question to the person in front of them. This continues until you reach the end of the line where there is no one in front!, at this point, each person replies back the count to the person who asked them, This is how recursion works, you solve the problem by breaking the problem down into smaller pieces and solving them.

For Further Reading Visit:

- [Problem Solving with algorithms and data structures with Python](https://runestone.academy/runestone/books/published/pythonds/index.html)
- [Problem-Solving with Python](https://problemsolvingwithpython.com/)
- [Python CheetSheet](https://www.pythoncheatsheet.org/)
