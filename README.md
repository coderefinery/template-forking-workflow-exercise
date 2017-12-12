## Exercise to practice collaborative forking workflow

We will run this exercise in groups. Groups can choose a number or a name.

Objectives:

- Learn how to fork, modify the fork, and file a pull request towards forked repo
- Learn how to update your fork with upstream changes


### Part A: Fork and clone

First fork this repository on GitHub into your namespace and then clone the fork to your computer.


### Part B: Modify and commit

Then add a file `group-X.py` where X is your group number or group name, e.g. `group-17.py`.
**Add only one file per group**. (Why?)

This file should contain a function called `tweet()` which returns
a string of maximum 140 characters, for instance:

```python
def tweet():
    return "please replace this boring sentence with something more fun"
```

The file `main.py` automatically calls all `tweet()` functions defined in files
`group*.py`. You do not need to edit `main.py`.

Test it before you commit your change:

```shell
$ python main.py

group 17 says: please replace this boring sentence with something more fun
```

### Part C: Push your changes to the fork

Once you see your sentence correctly printed, commit and push to your fork. Don't worry
nothing gets out to Twitter but please mind that your changes will be public on
GitHub (but you can delete them later).


### Part D: File a pull request

Then file a pull request towards the repository where you forked from.

Wait until we integrate all pull requests into the central repo
together on the big screen.


### Part E: Update your fork

We do this part **after the contributions from all groups have been integrated**.

Once this is done, practice to update your forked repo with the upstream
changes and verify that you got the files created by other groups:

```shell
$ python main.py
```
