# FileName: auto_git.py
# Brief: Python3 script for automating batch manage git repositories.
# Author: Qing Yu
# CreateDate: 2022.02.11

import os
import tomllib

import colorama

with open('auto_git.toml', 'rb') as f:
    data = tomllib.load(f)
    size = len(data['repos'])

colorama.init(autoreset=True)

COLOR_START = colorama.Fore.BLUE + colorama.Style.BRIGHT
COLOR_INFO = colorama.Fore.CYAN + colorama.Style.BRIGHT
COLOR_FINISH = colorama.Fore.GREEN + colorama.Style.BRIGHT
COLOR_ERROR = colorama.Fore.RED + colorama.Style.BRIGHT


def main():
    print("Welcome to the automatic git management program!")
    print()
    print("status: check repositories status.")
    print("push:   push local repositories to remote repositories.")
    print("clean:  clean up redundant files and directories.")
    print("remote: show a list of existing remote repositories.")
    print("gc:     optimize the local repositories.")
    print()
    print("exit:   exit this program.")
    print()

    while True:
        x = input("\nYour choice [status(default)/push/clean/remote/gc/exit]: ").strip().lower()
        if x == 'status' or x == '':
            status()
        elif x == 'push':
            push()
        elif x == 'clean':
            clean()
        elif x == 'remote':
            remote()
        elif x == 'gc':
            gc()
        elif x == 'exit':
            break
        else:
            print(COLOR_ERROR + "Invalid option: " + x)

    print("Bye!")


def status():
    print(COLOR_START + "Start status.\n")

    for i, repo in zip(range(size), data['repos']):
        os.chdir(repo['root'])
        print(COLOR_INFO + f"({i + 1}/{size}) Checking {repo['root']}:")
        os.system("git status")
        print()

    print(COLOR_FINISH + "Finish status.")


def push():
    print(COLOR_START + "Start push.\n")

    for i, repo in zip(range(size), data['repos']):
        print(COLOR_INFO + f"({i + 1}/{size}) Pushing {repo['root']}:")
        os.chdir(repo['root'])
        for address in repo['addresses']:
            print(COLOR_INFO + f"to {address}:")
            os.system(f"git push {address}")
        print()

    print(COLOR_FINISH + "Finish push.")


def clean():
    print(COLOR_START + "Start clean.\n")

    for repo in data['repos']:
        if repo['clean']:
            os.chdir(repo['root'])
            print(COLOR_INFO + f"Cleaning {repo['root']}:")
            # use ".gitignore" as pattern to clean up redundant files and directories recursively.
            os.system("git clean -d -f -X")
            print()

    print(COLOR_FINISH + "Finish clean.")


def remote():
    print(COLOR_START + "Start remote.\n")

    for i, repo in zip(range(size), data['repos']):
        os.chdir(repo['root'])
        print(COLOR_INFO + f"({i + 1}/{size}) Showing {repo['root']}:")
        os.system("git remote --verbose")
        print()

    print(COLOR_FINISH + "Finish remote.")


def gc():
    print(COLOR_START + "Start gc.\n")

    for i, repo in zip(range(size), data['repos']):
        os.chdir(repo['root'])
        print(COLOR_INFO + f"({i + 1}/{size}) Optimizing {repo['root']}:")
        os.system("git gc --aggressive")
        print()

    print(COLOR_FINISH + "Finish gc.")


if __name__ == '__main__':
    main()
