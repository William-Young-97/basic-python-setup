**Testing for errors**

**What is it?**

~ Error handling in code ~

As developers we want to make sure that we catch and limit the amount of bugs in our code. We can do this through the use of error handling. Error handling allows us to return information about why something is going wrong. This is crucial for debugging and building complex systems.

~ Testing our error handled code ~

Error testing involves mocking a condition that causes an error to be raised. This is important as it allows us to verify if we are testing the correct block of code. Poorly written tests can give a false positive, meaning we think our code is safe, but it isn't. Writing unit tests (our automated tests for our functions), and doing manual testing (executing your code in a python shell) are great ways to ensure you're testing your code correctly.


**Next**

~ Tutorial files ~

Included in this directoy is an example function that use error handling. Accompanying it will be tests relevant to what the function and its use of error handling. Have a look through them both and run the tests with pytest. Feel free to play around with the function and testing to see what you can break.

~ Manual testing in the pytyhon shell ~

From this directory (lesson-2) in terminal type in `python3`. This will bring you into the python shell and it is from here that you can manually execute your code. Type `import err` to bring the err.py file into your shells scope. Now we have access to the contents of the err file. We can instantiate an instance of our Basics() class with the following command: `basics = Basics()`. With our basics instance we can use the functions that are defined on that class. Try calling `basics.add(1 + 1)` and watch the function execute.

**Reference/additional resource**
https://www.programiz.com/python-programming/user-defined-exception



