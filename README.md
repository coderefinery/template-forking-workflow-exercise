

## Exercise: practice collaborative forking workflow

In this exercise, we make a fork, push to that fork, and make a pull
request to the "central" repository. Later we will exercise updating the individual forks
after changes from all participants have been merged.

As an example we will collaboratively develop a cookbook for taco recipes,
inspired by [tacofancy](https://github.com/sinker/tacofancy).

We recommend that you discuss with your neighbor throughout the exercise.

Objectives:

- Learn how to fork, modify the fork, and file a pull request towards the forked repo.
- Learn how to update your fork with upstream changes.


### Part A: Fork and clone

First fork this repository
into your namespace and then clone the fork to your computer.


### Part B: Open an "issue" as a change proposal

Before we start any coding, open a new "Issue" on the central repository as a
"proposal" where you describe your idea for a recipe with the possibility to
collect feedback from others. After creating this issue note the issue number.
We will later refer to this issue number.

Discuss with your neighbor why it can be useful to open an issue before
starting the actual coding.


### Part C: Modify and commit

Before we do any modification, we create a new branch and switch to it: this is
a good reflex and a good practice. Choose a branch name which is descriptive of
its content.

On the new branch create a new file which will hold your recipe,
for instance `traditional_coderefinery_tacos.md` (but change the name). You can get inspired
[here](https://github.com/sinker/tacofancy/tree/master/full_tacos). Hopefully we all use different
file names, otherwise we will experience conflicts later (which is also interesting!).

There is also a file called `test.py` which will automatically verify whether your recipe contains the string
"taco" (case insensitive). This is there to slowly introduce us to automated testing.

Once you are happy with your recipe, commit the change and in your commit
message reference the issue which you have opened earlier with "this is my
commit message; closes #N" (use a more descriptive message and replace N by the
actual issue number).


### Part D: Push your changes to the fork

Now push your new branch to your fork. Your branch is probably called something else than "feature". Also verify where
"origin" points to.

```shell
$ git push origin feature
```


### Part E: File a pull request

Then file a pull request from the branch on your fork towards the master branch on the repository where you forked from.

Wait here until we integrate all pull requests into the central repo
together on the big screen.

Observe how the issues automatically close after the pull requests are merged
(provided the commit messages contain [the right keywords](https://help.github.com/en/articles/closing-issues-using-keywords)).


### Part F: Update your fork

We do this part **after the contributions from all participants have been integrated**.

Once this is done, practice to update your forked repo with the upstream
changes and verify that you got the files created by other participants.

Make sure that the contributions from other participants are not only on your local repository
but really also end up in your fork.
