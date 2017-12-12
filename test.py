"""
This will loop through all the files with group*.py and assert that their
tweet()-function returns a string that is less than 140 characters long.
"""

import os

for filename in os.listdir("."):
    if filename.startswith("group") and filename.endswith(".py"):
        module_name = filename[:-3] # ignore .py at the end
        module = __import__(module_name)
        tweet_content = module.tweet().encode('utf-8')
        assert len(tweet_content) <= 140, \
            "tweet is too long: '{}'".format(tweet_content)
