Before deploying our application to heroku, I'll walk you through some of the prerequisites.

We'll take a look at the production settings and take a look at some of the configurations, if you observe, you can see that most of the configurations are read from the environment, this is extremely useful when deploying application so that we dont need to change the code when we need to deploy to a new environment. 

The secret key referenced here is the one that is used to seed the session key, password hashes and everything else that the server might be doing secret. Similarly the database url is also being read from the environment. There are a lot of other configs here, instead of explaining them one by one, feel free to google the ones you find intriguing for more information, play around with the configs to see what happens.

We'll head over to heroku to visit our application, We'll take a quick look at configs and see what we have, you can find the configs in the settings section under config.

I'll leave these configs in the content, you can use the `https://djecrety.ir/` website to get a new pair of secrets, other configurations will be left in the content, the redis_url and the database_url is something that heroku populates by iself, we'll see how we can add those, once they are done, you can go ahead and deploy your application!