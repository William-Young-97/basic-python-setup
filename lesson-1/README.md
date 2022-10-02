## Lesson-1

### Python Virtual Environments 

**Starting a virtual environment**

In the terminal run: 
```
mkdir \<my-python-project\>
cd \<my-python-project\>
python3 -m venv .
source bin/activate
```
*To quit type: `deactivate`*

**What is it?**

"Virtual environments stop problems by creating special isolated environments where all the packages and versions you install only apply to that specific environment. It’s like a private island! — but for code."

**Why bother?**

"You can organize your packages much better and know exactly the packages you need to run your code in case someone else needs to run it on their machine. Additionally, your main python package directory won't get FLOODED with unnecessary python packages."

Ref: https://towardsdatascience.com/why-you-should-use-a-virtual-environment-for-every-python-project-c17dab3b0fd0

### Testing

**Basics**

1. Inside the virtual environment run `pip install pytest`, to install the testing library. 
2. Verify the proper installation with `pytest --version`
3. Create a file named maths.py and make a basics class with a `add(a, b)` method that sums two numbers.
4. In the same directory create a file called test_maths.py and import your `maths` file and `Basics` class.
5. Create a `test_add()` function that uses `assert` to check if your function is running.
6. Type `pytest` into the terminal to run the test.




