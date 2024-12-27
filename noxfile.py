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
    session.run("black", "--check", "src", "tests")


@nox.session
def isort(session):
    session.install("isort")
    session.run("isort", "--check", "--profile", "black", ".")


@nox.session
def mypy(session):
    session.install("mypy")
