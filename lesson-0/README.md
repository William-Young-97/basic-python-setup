## Lesson-0

### Git

**What is it?**

Git provides us with version control. This means we can commit (save) our work whenever we want and return to that point in the future. As you can imagine this is useful for if we make mistakes in our code. It can also be used with GitHub to store code online. Finally, Git allows multiple people to work on the same project at the same time.

**Why bother?**

Git is widely used by industry professionals and is an essential developer tool for any beginner to learn. It helps us to track changes in our code over time, and as well as leading to safer projects, it allows multiple people to work on a single project.

**How can we use it?**

- `brew install git` To install Git
- `git init` Initiates a new hidden git repository
- `git commit` Allows you to commit your work (save it)
- `git push` Can push your work up to GitHub

To use `git push` create an account on GitHub and generate an ssh keypair:

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

to allow you to securely push your work.

### Testing

**What is it?**

Testing is the practice of ensuring your code works even if changes are made to it. Specifically, unit tests are written to test input vs output. Many languages have many different testing frameworks. For python we will be using pytest. 

**Why bother?**

The benefits of testing are numerous:

- Allows us to refactor and change code whilst ensuring functionality is kept the same.
- Verification that each component of your code works in different situations.
- Helps to guard against programmatic errors.
- Provides a form of documentation for your code base.
- Creates a scalable framework for your codebase as it grows and new contributers join.

**How can we use it?**

More on this in lesson-1.

### Red, Green, Refactor Cycle

**What is it?**

The Red, Green, Refactor cycle refers to a workflow for using testing and git. It is linked to test driven development and is a good way to write code.

**Why bother?**

In tech, proper workflows and best practices are extremly important. Systems can very quickly become complex, so it is important that we build them up with simple iterations, in order to minimise errors. Red, Green, Refactor cycles enable this through testing and git. Another benefit is that they shorten feedback loops, meaning we can quickly respond to demands and make proper changes in our code.

**How can we use it?**

Firstly: We use `git init` to create a git repository and then `git commit` for an inital empty commit.

Then: 

Red: Refers to writing a test for the function we want to create. We create some inputs for this test and assert that we expect a certain output. For example, `assert add(1, 1) == 2`. As we haven't yet created this function in the code, we can expect this to fail and see red text appear when running pytest.

Green: Refers to writing the function that will allow this test to pass. In this case, we would create a simple `add(a, b):` function with a body of `return a + b`. Now when we run our test we should see it pass in a lovely shade of green.

Refactor: It's great that our test is passing, but is there anything we can do to make our function better? The `add(a, b)` function is fairly simplistic, so in this case, there's nothing refactor. It's always worth looking for places to refactor after writing your test and function.

Following this cycle we can slowly and simply build out our code, mitigating a lot of the confusion that arises from complex systems. It is important that we try to keep our commits small and frequent for the best results.