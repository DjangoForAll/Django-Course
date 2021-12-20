Everything that we discussed till now was in the context of an HTTP request, usually there are jobs that are not invoked by an external http request, we will be looking into some use cases and how its implemented.

Lets say that you want to send an email with all the pending tasks to the user at midnight everyday. This is a job that is dependent on the current time and not based on an external request. These types of jobs are usually called cronjobs. There can also be an externally triggered job, for example lets say you have an endpoint that does a lot of computation and needs a lot of time to process. These types of long running jobs are usually performed in the background so that the actual server has more time to work on simpler requests.

Celery is a popular library that solves exactly this problem. Note that celery is not dependent on django, there are packages that integrate django and celery for specific usecases.

We'll just focus on getting a basic job up and running.

Lets create a task that
