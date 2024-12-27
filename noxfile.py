import nox


@nox.session
def tests(session):
    session.install("pytest")
    session.run("pytest", "tests")


@nox.session
def lint(session):
    session.install("flake8", "flake8-import-order")
    session.run(
        "flake8",
        "--import-order-style",
        "google",
        "src",
        "tests",
    )


@nox.session
def black(session):
    session.install("black")
    session.run("black", "--check", "src", "tests", "noxfile.py")


@nox.session
def isort(session):
    session.install("isort")
    session.run("isort", "--check", "--profile", "black", ".")


@nox.session
def mypy(session):
    session.install("mypy")
    session.run("mypy", "src")


@nox.session
def pre_commit(session):
    session.install("black", "isort", "flake8", "mypy", "pytest")

    # Define targets excluding pyproject.toml
    python_targets = ["src", "tests", "noxfile.py"]

    # Run Black with explicit exclusion
    session.run("black", "--exclude", "pyproject\\.toml$", *python_targets)

    # Run Isort
    session.run("isort", "--profile", "black", ".")

    # Run Flake8
    session.run("flake8", "--max-line-length=88", "src", "tests")

    # Run Mypy
    session.run("mypy", "src")

    # Run Tests
    session.run("pytest", "tests")
