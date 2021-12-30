Now you have an application that runs locally in your computer, Thats great! but how does someone else use it?

Deployment is the set of activities that are performed to make a an application available to the public or for general use. Usually applications are hosted on a remote machine somewhere in a data center.

There might be some questions you have at this point,

- Why not just deploy the application on your own machine?
Well that is not a bad idea, You can technically deploy web application on your own machine, but you'll have to make sure that your machine runs all day, everyday, which means the internet connection and power should always be maintained, and then there is the problem of ip addresses, usually home internet connections have a dynamic ip, as in your address might change every time you restart your router or when your ISP wishes to. This means that everytime it changes you have to keep track of it in your DNS (DNS is what maps a domain name to an IP address). We are starting to see why a remote machine would be better now.

There are way more complicated issues like monitoring and scaling that you'll have to deal with.

To quickly share your local deployment with others you can use a tunnel like ngrok or cloudflare tunnels, that creates a unique publicly accessible link that points to your local deployment.

- How can i make this process less painful?
Usually deployment is a pain, it involves a lot of manual provisioning and configuration and its extremely simple to get wrong and for inexperienced devs it might be extremely hard to get it right. That is where PAaS or Platform as a Service tools come in. They are folks who handle the deployment for us, We write the code and the PAaS takes care of the rest. Simple Enough Right? Heroku and DigitalOcean are two of the most popular PAaS tools, but there are many more out there.

### Deployment terminologies

**Development** refers to a developers environment, this is where you develop the application and test it manually. These usually are not deployed to the public as in they are locally deployed.

**Production** refers to a deployed application that is available to the public. They are mostly deployed in remote environments and have restricted access.

**Staging** refers to an environment just before the production environment, this is where you test your application and make sure it works as expected. They usually have a public url but is not made for general public use. This is where your team members test the application to ensure it works as intended. The staging deployment is configured to be exactly the same as Production so that any issues that may happen in Production can be identified before deployment.

There can be more deployments if needed.

