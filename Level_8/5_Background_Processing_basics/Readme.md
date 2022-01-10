Everything that we discussed till now worked in the context of an HTTP request, usually we'll also have jobs that are not invoked by an external HTTP request, we will be looking into some use cases and how its implemented.

Let's say that you want to send an email with all the pending tasks to the user at midnight every day. This is a job that is dependent on the current time and not based on an external request. These types of jobs are usually called cronjobs. There can also be an externally triggered job, for example, let's say you have an endpoint that does a lot of computation and needs a lot of time to process. These types of long-running jobs are usually performed in the background so that the actual server has more time to work on simpler requests.

Celery is a popular library that solves exactly this problem. Note that celery is not dependent on Django, there are packages that integrate Django and celery for specific use cases.

Celery introduces a bunch of new terms, let's take a look at them one by one.

### Task

A Celery task is a representation of a callable that can be invoked by celery, in other words, it is a method that is registered with celery, An instance of the task contains the arguments you passed to the method as well. When you start a background job, all you are doing is creating a new task object and storing it somewhere to be executed, That brings us to the next topic.

### Broker

Since celery is used in background processing there needs to be some sort of queueing mechanism, any task that needs to be processed are added to the queue and then processed one by one. This queue is usually called a broker. The broker does not have any knowledge of the actual implementation of the task, it just stores the task in the queue.

For our implementation we will be using Redis as the broker, Redis is an in-memory data store, Redis has implementations of different kinds of abstracted data structures built-in, one of them is the queue which makes it ideal as the broker.

The use of Redis is not limited to celery, check out the Redis [homepage](https://redis.com) for more use cases and its cool features.

### Worker

A Celery worker is responsible for actually executing the task, A Celery worker asks the broker to get pending tasks and executes them as soon as they are available. You can have as many celery workers as you want in a project.

### Periodic Scheduler ( Beat )

Periodic Tasks in celery are made possible with celery beat, which is a scheduler that schedules tasks to be executed based on the schedules we configure.


Now that we have a basic understanding of celery, let's install and configure it in our project.

Before we get started, ensure that you have Redis installed and configured properly. follow this [tutorial](https://flaviocopes.com/redis-installation/) to install Redis.

once you have Redis configured, running the following command in your terminal should print out `PONG`

```bash
redis-cli ping
```

If you have configured Redis correctly, you can move ahead to the next step.

Let's install the python packages for celery and Redis.

```bash
pip install celery==4.4.7 redis
```

let's also add the following configurations to the `settings.py` file

```python
BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
```

Let's create a new config file for celery, this file will be called `celery.py` and will live in the same folder as your settings file.

These are the contents of your celery config file:

```python
import os
from datetime import timedelta

from django.conf import settings

from celery import Celery
from celery.decorators import periodic_task

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")
app = Celery("task_manager")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# Periodic Task
@periodic_task(run_every=timedelta(seconds=30))
def every_30_seconds():
    print("Running Every 30 Seconds!")

```

The initial bit of the file defines the default settings, where celery should look for files and so on, these are usually common to all celery configurations. The next bit of the file defines a task that runs every 30 seconds. The task is decorated with the `periodic_task` decorator and the run_every argument specifies the time interval between each execution of the task.

> Decorators in Python are used to modify the behavior of a function, we can add statements before and after the function call and modify the behavior of the function. Read more about decorators [here](https://www.programiz.com/python-programming/decorator)

Now we have a method that is called every 30 seconds, but how do we test it?

open up two terminals, and run the following command in the first terminal:

```bash
celery -A task_manager beat
```

This starts the periodic scheduler, this will figure out when the task should be called and add the task to the broker whenever it needs to be called

In the next terminal run the following command:

```bash
celery -A task_manager worker
```

The worker checks the broker for any pending tasks and just executes them, It does not care whether the task is periodic or not, if the task exists in the broker, the worker will just execute them.

Play around with the configs and see if you can create more periodic tasks, try to see if you can make the tasks wait for a random time to see how the worker behaves.

> Note that celery does NOT automatically restart when code changes are made, Celery processes have to be manually restarted for any changes to take effect.