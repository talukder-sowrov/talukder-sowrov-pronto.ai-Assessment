import argparse
from validation import dir_valid
from actions import status_actions, log_actions

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = "Was it Rufus?",
        description = "Program takes in a GitHub directory, gets information for it, and checks if the author is Rufus.",
        epilog = "Program for Pronto.ai coding assessment."
    )

    parser.add_argument('git_dir')

    git_dir = parser.parse_args().git_dir
    dir_valid(git_dir)

    status_actions(git_dir)
    log_actions(git_dir)