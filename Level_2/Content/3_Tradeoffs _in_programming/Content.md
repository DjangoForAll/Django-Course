### Analysing Programs ( optional )

There are certain questions that you might have about programming,
like how to write better code, then again how do i know that my code is better?
how do i compare two programs?
my program works now for small datasets how will it work for larger datasets?
does fewer lines of code mean better performance?

I'll give a short example about how to approach these problems,

Assume that you have a phone directory with a list of names and phone numbers. if you dont know what a phone directory is, its just a book that contains the names of every person with a phone number along with their phone number in a sorted manner ( based on the persons name ) These books get really large and it might get tricky to find a person's phone number quickly and efficiently.  
if you wanted to teach someone to find someone in these directory, what all approaches might you take?

1. Native Method ( look at each phone number one by one ):
   This method is pretty simple, take each name check if its the required person and move to the next person and repeat this process until you find the person.
2. The Smart Method :
   Most of us use this method even though we never really learnt it formally, to find a name we take the middle ( or sorta middle ) of the list and check if the name of the required person is greater than or lower than the names in the current page, repeat by halfing the number of names in the list until you find the required person.
3. Even Smarter Method :
   Check if there is an index, usually there is an index page that contains the first two letters and the page number containing those names, which narrows down our search a lot.

Now lets imagine that we take one second to check if the name is correct each time, can you figure out how much time it will take to find someone in a phone directory with each method? ( assume that there are 1 million entries in the phone directory )

with the first method it will take approximately ~12 days , seems kinds long to find someone right ?
with the second method it will take approximately 20 second, that is a huge decrease right ?
with the third method it will take less than 20 seconds, Yay!

This example was designed to contrast how much of a difference proper algorithms and programming can make, The native method is called linear search , the smart method is called binary search , and the even smarter method is called jump search.
The length of your program does not matter ( negligible ) as long as the implementation is correct, complex algorithms are rarely used in our course and it might not come up as often as you think in web development, nevertheless whenever developing make sure to check if your code can be improved.

> As an optional exercise you can try and implement all three methods with integers and see how can you compare the performance of each method with large inputs.

For a better understanding about this topic [read this](https://en.wikipedia.org/wiki/Time_complexity)
