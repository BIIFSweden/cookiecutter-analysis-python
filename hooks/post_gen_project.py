import subprocess


def init_git() -> None:
    try:
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "branch", "-M", "main", "-q"])
        subprocess.run(["git", "remote", "add", "origin", "git@github.com:BIIFSweden/{{ cookiecutter.project_id }}.git"])
    except Exception:
        pass


if __name__ == "__main__":
    init_git()
