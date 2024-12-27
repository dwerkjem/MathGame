import nox


@nox.session
def tests(session):
    session.install("pytest")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "--import-order-style", "google")


@nox.session
def black(session):
    session.install("black")
    session.run("black", "--check", ".")


@nox.session
def isort(session):
    session.install("isort")
    session.run("isort", "--check", "--profile", "black", ".")


@nox.session
def mypy(session):
    session.install("mypy")
    session.run("mypy", "math_game")
