import os
from urllib.parse import urlparse

folders = {
    "py": "Python3",
    "ts": "TypeScript",
    "pd": "Pandas",
    "js": "JavaScript",
    "sh": "Bash",
    "sql": "MySQL"
}

extensions = {
    "py": "py",
    "ts": "ts",
    "pd": "py",
    "js": "js",
    "sh": "sh",
    "sql": "sql"
}

comments = {
    "py": "# ",
    "ts": "// ",
    "pd": "# ",
    "js": "// ",
    "sh": "# ",
    "sql": "-- "
}

flag = False

while True:
    if flag:
        user_input_1 = input("Would you like to add another file? (y/n): ")
        if user_input_1.lower() != "y":
            break

    input_1 = ""  
    while True:
        input_1 = input("Url: ")
        if len(input_1) > 0:
            break

    technology = ""
    while True:
        technology = input("Technology - " + str(list(folders.keys())) + " : ")
        if technology in extensions:
            break
        else:
            print("Invalid technology name")

    path = urlparse(input_1).path
    path = path.replace("/", "")
    path = path[8:]

    file_path = folders[technology] + "/" + path + "." + extensions[technology]

    if not os.path.exists(os.getcwd() + "/" + file_path):
        print('File not exists')
        f = open(os.getcwd() + "/" + file_path, "x")
        f.write(comments[technology] + input_1)
        f.close()
        os.system("code " + file_path)

        user_input = input("Do you want to upload changes to the repository? (y/n): ")
        if user_input.lower() == "y":
            os.system("git add " + file_path)
            os.system("git commit -m " + '"' + path + '"')
            os.system("git push origin main")
    else:
        print('File exists')
        user_input = input("Do you want to view the file? (y/n): ")
        if user_input.lower() == "y":
            os.system("code " + file_path)

    flag = True

user_input = input("Generate a new README file? (y/n): ")
if user_input.lower() == "y":
    os.system("python3 readme-generator.py")
    os.system("git add README.md")
    os.system("git commit -m " + '"README.md"')
    os.system("git push origin main")

print("-- exit --")