# Text Removal Tool
## What is it
The tool removes a list of keywords from files in a specific folder. For each match in the list of keywords, the match is removed from the file. This means if a file has two or more keywords, all the keywords are removed from the file sequentially. Note that the execution to change each filename is only called once for each file.

## How to use
1. Run the python file "remover.py"
1. Navigate the menu as necessary
    1. On the first run-through a config file is created
    1. You must enter a path the first time
    1. You must enter an extension the first time
1. Add keywords using the add keywords
    1. If you need to remove an accidental keyword, use the remove keyword section. Note that this is case sensitive
1. Press the verify button and check that you only have files you want to change the name of
    1. If you find files that are matched which you dont want to remove, change your keywords so that it is no longer included
1. Once you are okay with the verified files, run "Execute" to remove the keywords

## Advanced use - Wildcards
'?' and '\*' wildcards can be used in the tools functions. '?' is a wildcard to match any single character, while '\*' matches any combination of characters. To use wildcards, simply enter the character without quotes, instead of your character.

NOTE: Space must be replaced with a ? wildcard if it is in the front or at the end of your keyword.

## Potential improvements
- Allow the user to whitelist files that shall not be changed