=================
git-sync-upstream
=================

git-sync-upstream is a CLI to sync git `upstream` remote branches and tags with
the local clone and `origin` remote.

Installation
------------

git-sync-upstream is distributed on `PyPI`_. It requires Python 3.7+. To
install:

.. code-block:: console

    $ python -m pip install git-sync-upstream

Usage
-----

Change directory to the git project to sync. The project must have a remote
named `upstream` and `origin`. The remote `upstream` will be used to sync
_from_. Its branches and tags will be synced locally and _to_ `origin`.

.. code-block:: console

    $ cd myproject
    # To sync the current branch
    $ git-sync-upstream
    # To sync all branches
    $ git-sync-upstream --all-branches

It is convenient to add a git alias to the command:

.. code-block:: console

    $ git config --global alias.sync "!git-sync-upstream"

Then:

.. code-block:: console

    $ cd myproject
    # To sync the current branch
    $ git sync
    # To sync all branches
    $ git sync --all-branches
