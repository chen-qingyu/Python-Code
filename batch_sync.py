# FileName: batch_sync.py
# Brief: Python3 script for automating batch synchronization of Git remote repositories.
# Author: Qing Yu
# CreateDate: 2022.02.11
# Functions:
#   - batch check Git repositories status
#   - batch synchronize Git remote repositories
#   - clean up redundant files and directories

import os
import colorama

colorama.init(autoreset=True)

COLOR_START = colorama.Fore.BLUE + colorama.Style.BRIGHT
COLOR_INFO = colorama.Fore.CYAN + colorama.Style.BRIGHT
COLOR_FINISH = colorama.Fore.GREEN + colorama.Style.BRIGHT
COLOR_ERROR = colorama.Fore.RED + colorama.Style.BRIGHT


# remote repository address: "host branch"
GITHUB = "github master"
GITEE = "gitee master"


# REPOS: ((root, remote, clean), ...)
# root: string, the root path of the local repository.
# remote: (string, ...), remote repository address.
# clean: bool, True if use "root/.gitignore" as pattern to clean up redundant files and directories.
REPOS = (
    ("F:/C/C Programs", (GITEE, GITHUB), True),
    ("F:/Python/Python Programs", (GITEE, GITHUB), False),
    ("F:/Java/Java Programs", (GITEE, GITHUB), False),
    ("F:/C/C Primer Plus", (GITEE, GITHUB), True),
    ("F:/Java/StuScore", (GITEE, GITHUB), False),
    ("F:/OSTEP", (GITEE, GITHUB), False),
    ("F:/Projects/BadApple", (GITEE, GITHUB), True),
    ("F:/Projects/HelloWorld", (GITEE, GITHUB), False),
    ("F:/Projects/LinearAlgebra", (GITEE, GITHUB), False),
    ("F:/Projects/Love Miao", (GITEE, GITHUB), False),
    ("F:/Racket/HtDP", (GITEE, GITHUB), False),
    ("F:/STM32/STM32 Programs", (GITEE, GITHUB), True),
    ("F:/TeX", (GITEE, GITHUB), True),
    ("F:/Projects/TestTime", (GITEE, GITHUB), True),
    ("F:/Projects/MDS", (GITEE, GITHUB), False),
    ("F:/Projects/MDSPP", (GITEE, GITHUB), False)
)


def status():
    print(COLOR_START + "Start checking.")

    for root, _, _ in REPOS:
        os.chdir(root)  # cd root/
        print(COLOR_INFO + f"Start checking {root}:")
        os.system("git status")
        print()

    print(COLOR_FINISH + "Checking completed.")


def push():
    # synchronize Git remote repositories.
    print(COLOR_START + "Start synchronize.")

    for i in range(len(REPOS)):
        root = REPOS[i][0]
        remote = REPOS[i][1]
        print(COLOR_INFO + f"({i + 1}/{len(REPOS)}) Start syncing {root}:")
        os.chdir(root)
        # if modified, commit successfully, or skip remote confirmation
        if os.system("git add . && git commit -m \"batch synchronize\"") == 0:
            for address in remote:
                print(COLOR_INFO + f"---{address}---")
                os.system(f"git push {address}")
        print()

    print(COLOR_FINISH + f"Synchronize completed, {len(REPOS)} repositories are synchronized.")


def clean():
    # use "root/.gitignore" as pattern to clean up redundant files and directories.
    print(COLOR_START + "Start cleaning.")

    for root, _, need_clean in REPOS:
        if need_clean:  # clean = True
            os.chdir(root)  # cd root/
            print(COLOR_INFO + f"Start cleaning {root}:")
            os.system("git clean -d -f -X")  # remove files ignored by Git recursively.
            print()

    print(COLOR_FINISH + "Cleaning completed.")


if __name__ == '__main__':
    while True:
        print()
        print("S: Status check.")
        print("P: Push repositories.")
        print("C: Clean redundant files.")
        print("Q: Quit.")

        x = input("Your choice [S(default)/P/C/Q]: ").strip()
        if x in "sS":  # "" in "sS" is True
            status()
        elif x in "pP":
            push()
        elif x in "cC":
            clean()
        elif x in "qQ":
            break
        else:
            print(COLOR_ERROR + "Invalid option: " + x)

    print("Bye!")