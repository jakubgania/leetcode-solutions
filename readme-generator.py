import os

folders = {
    "py": "Python3",
    "ts": "TypeScript",
    "pd": "Pandas",
    "js": "JavaScript",
    "sql": "MySQL"
}

f = open(os.getcwd() + "/README.md", "w")
f.write("# leetcode-solutions\n")
f.write("My own solutions to tasks on LeetCode platform. I'm saving them here for archiving. Not every solution is the most optimal or appropriate because this is a learning process for me in general - keep taht in mind.\n")

for extension, folder in folders.items():
    number_of_files = len(os.listdir(os.getcwd() + "/" + folder))
    f.write("## " + folder + " - " + str(number_of_files) + "\n")
    f.write("\n")
    for item in os.listdir(os.getcwd() + "/" + folder):
        url = "https://github.com/jakubgania/leetcode-solutions/blob/main/" + folder + "/" + item
        item = item.replace("." + extension, "")
        f.write("* [" + item + "](" + url + ")\n")
        # f.write("\n")

f.close()