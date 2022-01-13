Here i have a sample html document with a form, ( Refer to the HTML Document )

In this form you can see that my action attribute is set to signin and my method is set to GET

you can also observe that i have three input elements , one to get the email address , one for the password and one to submit the data

Now on rendering this html document , you can see that the form has come up. i am going to type in my username and password and hit the signin button.

Now you can see that it has redirected us to the signin page which was our action attribute and the data i placed inside the input tags are now in the url , the data is seperated from the url with a `?` charecter and each value is seperated using a `&` charecter.

Lets try and change the same form to use POST and see what happens

Now on submitting the form you can see that data no longer appears in the URL, this is because the data is now being sent in the HTTP body instead, This is more secure and allows really long content

Now you might be asking why use the get method at all?

GET can be emulated with a simple anchor element as such.

GET methods are also easier to cache and are used primarily when there is no side effect to the action.
like passing the page number or a search query or anything like that where the data is not really confidential and the action cannot cause any changes internally.

Try it yourselves and see what happens
