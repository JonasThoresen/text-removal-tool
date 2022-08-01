# Imports
import glob
import os
import configparser
import re


# Main class
class remover():
    def add(self):
        """ Adds new keywords to the keyword list"""
        print("-------------------------------")
        print(f"Current list: {sorted(self.remove_list)}")
        print("-------------------------------")
        print("Add a new keyword or type 'Q' to exit without adding one."
              "\nNote that the keywords are case sensitive, except for Q."
              "\nYou can chain keywords using ',' but note that spaces"
              "\non the start and end of the keywords will be stripped."
              "\nTo keep these spaces, replace them with a question mark '?'."
              "\nThe extension supports wildcards '*' and '?'.")
        keyword = input("Keyword: ")

        if keyword.lower() != "q" and keyword.lower() != "":
            tmp_keyword = keyword.split(',')
            for kwd in tmp_keyword:
                kwd = str(kwd)
                self.remove_list.add(kwd.strip())

            print("New removal list is", self.remove_list)

    def remove(self):
        """ Removes keywords from the keyword list"""
        print("-------------------------------")
        print(f"Current list: {sorted(self.remove_list)}")
        print("-------------------------------")
        print("Remove a keyword or type 'Q' to exit without removals."
              "\nNote that the keywords are case sensitive, except for Q."
              "\nYou can chain keywords using ',' but note that the words"
              "\nmust match 100% to the added keyword. If a wildcard is used,"
              "\nuse the wildcard in the remove keyword section as well.")

        keyword = input("Keyword(s): ")
        if keyword.lower() != "q" or keyword.lower() != "":
            tmp_keyword = keyword.split(',')
            for kwd in tmp_keyword:
                kwd = str(kwd)
                if kwd in self.remove_list:
                    self.remove_list.remove(kwd.strip())

            if not self.remove_list:
                self.match_list = set()

            print("New removal list is", self.remove_list)

    def set_extension(self):
        """ Sets a new file extension to use for searches """
        print("-------------------------------")
        print("Setting a new extension. This extension is used by the"
              "\napplication to decide what types of files to look for."
              "\nAny files with a matching extension when running the"
              "\nremover will have its filename changed. The extension"
              "\nsupports wildcards like * and ?.")
        self.extension = input("Set extension: ")
        self.config['settings']['extension'] = self.extension
        try:
            with open('config.ini', 'w') as configFile:
                self.config.write(configFile)
        except OSError:
            return "The config.ini file could not be written to!"
        return ""

    def set_path(self):
        """ Sets a new path to search for files """
        print("-------------------------------")
        print("Setting a new path. This path is used by the application to"
              "\ndecide where it looks for files. Any files"
              "\npresent in this folder when running the"
              "\nremover will have its filename changed if a "
              "\nkeyword is present.")
        new_path = input("Set path: ")
        if not os.path.exists(new_path) or not os.path.isdir(new_path):
            return "That path is invalid, try again"
        else:
            print("Setting path to", new_path)
            self.folder = new_path
            self.config['settings']['path'] = new_path
            try:
                with open('config.ini', 'w') as configFile:
                    self.config.write(configFile)
            except OSError:
                return "The config.ini file could not be written to!"
            return ""

    def find_match(self):
        """ Find all matches that are equal to the path, extension and keywords """
        print("Finding all matches")
        self.match_list = set()

        if self.folder != "":
            if len(self.remove_list) >= 1:
                for keyword in self.remove_list:
                    files_matched = glob.glob(self.folder + "\\" + "*" + str(keyword)
                                              + "*" + self.extension)
                    for ext_file in files_matched:
                        if ext_file not in self.match_list:
                            self.match_list.add(ext_file)

                print("There are", len(self.match_list), f"{self.extension} "
                      "files meeting the critera:")
                for file in self.match_list:
                    print("\t>", file)
                input("Press enter to continue")
                return ""
            else:
                return "Keyword(s) list cannot be empty."
        else:
            return "You must enter a folder first in the Set Path area."

    def execute(self):
        """ Remove files that are in the matched list from find_match() """
        success = False
        print("Starting removal of keywords")
        # Make sure we have removal keywords and minimum one match
        if len(self.remove_list) >= 1:
            if len(self.match_list) >= 1:
                # When we do, we iterate through all removal
                # keywords for each match
                for i, file in enumerate(self.match_list):
                    tmp_file = file
                    for keyword in self.remove_list:
                        keyword = keyword.replace("?", ".")
                        tmp_file = re.sub(keyword, "", tmp_file)

                    tmp_file = tmp_file.replace(' .mp3', '.mp3')

                    print(f"-----\nFile {i}:\nOld:{file}\nNew:{tmp_file}")

                    try:
                        os.rename(file, tmp_file)
                        success = True

                    except OSError as e:
                        return ("Failed with exception: " + str(e))

            else:
                return ("You need at minimum one match to remove "
                        "keyword(s) from file(s). \nPlease run "
                        "'Verify' after adding at least one keyword.")
        else:
            return "Keyword(s) list cannot be empty."

        if success:
            self.remove_list = set()
            self.match_list = set()
            return ""

    def printAll(self):
        """ Prints the current keywords and matches """
        print(f"I am looking inside the folder: {self.folder}"
              f"\nI will remove the following keywords: {sorted(self.remove_list)}"
              f"\nWith matches in the following files: {sorted(self.match_list)}")

    def __init__(self):
        self.remove_list = set()
        self.match_list = set()

        self.config = configparser.ConfigParser()

        if os.path.exists('config.ini'):
            self.config.read('config.ini')
            self.folder = self.config['settings']['path']
            self.extension = self.config['settings']['extension']
        else:
            self.folder = ""
            self.extension = ""
            with open('config.ini', 'w') as configFile:
                configFile.write("[settings]"
                                 "\npath ="
                                 "\nextension =")
