#!/usr/bin/env python

import argparse

from .git import Git


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("branches", nargs="*")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    git = Git()

    # Halt if there are uncommitted changes.
    git.diff("--exit-code", capture_stdout=False)

    current_branch = git.branch("--show-current")
    assert current_branch is not None

    git.checkout("--detach")
    try:
        options = ["--all", "--tags", "--prune"]
        if args.force:
            options.append("--force")
        git.fetch(*options)

        if args.all:
            out = git.for_each_ref(
                "--format=%(refname:lstrip=3)", "refs/remotes/upstream/"
            )
            assert out is not None
            upstream_branches = out.split()
        elif args.branches:
            upstream_branches = args.branches
        else:
            upstream_branches = [current_branch]

        options = []
        if args.force:
            options.append("--force")
        options.append(".")
        options += [
            f"refs/remotes/upstream/{branch}:{branch}" for branch in upstream_branches
        ]
        git.fetch(*options)

        options = ["--set-upstream", "--tags"]
        if args.force:
            options.append("--force")
        git.push(*options, "origin", *upstream_branches)
    finally:
        if current_branch:
            git.checkout(current_branch)


if __name__ == "__main__":
    main()
