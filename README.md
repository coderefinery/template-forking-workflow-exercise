[![Build Status](https://travis-ci.org/coderefinery/forking-workflow-exercise.svg?branch=master)](https://travis-ci.org/coderefinery/forking-workflow-exercise/builds)

## Distributed version control

## Exercise to practice collaborative forking workflow

We will run this exercise in groups. Groups can choose a number or a name.

Objectives:

- Learn how to fork, modify the fork, and file a pull request towards forked repo
- Learn how to update your fork with upstream changes.


### Part A: Fork and clone

First fork this repository on GitHub into your namespace and then clone the fork to your computer.


### Part B: Modify and commit

Before we do any modification, we create a new branch and switch to it - this is a good reflex and a good practice.
On the new branch add a file `group-X.py` where X is your group number or group name, e.g. `group-17.py`.
**Add only one file per group**.
(Why? - if you are adventurous, add both a file with the same name to see what happens)

This file should contain a function called `tweet()` which returns
a string of maximum 280 characters, for instance (don't worry, nothing gets out to Twitter):

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

If it works, commit the change.


### Part C: Push your changes to the fork

Once you see your sentence correctly printed, commit and push the branch to your fork.

Don't worry
nothing gets out to Twitter but please mind that your changes will be public on
GitHub (but you can delete them later).


### Part D: File a pull request

Then file a pull request from the branch on your fork towards the master branch on the repository where you forked from.

Wait here until we integrate all pull requests into the central repo
together on the big screen.


### Part E: Update your fork

We do this part **after the contributions from all groups have been integrated**.

Once this is done, practice to update your forked repo with the upstream
changes and verify that you got the files created by other groups:

```shell
$ python main.py
```

Make sure that the contributions from other groups are not only on your local repository
but really also end up in your fork.
