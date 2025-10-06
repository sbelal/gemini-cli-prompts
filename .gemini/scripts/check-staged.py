import subprocess
import sys

# subprocess.run() executes the command.
# We capture the result, which includes the exit code.
result = subprocess.run(
    ['git', 'diff', '--cached', '--quiet'],
    capture_output=True
)

# The git command returns an exit code of 0 if there are NO staged changes.
if result.returncode == 0:
    print("No staged files found. Please use 'git add' first.")
else:
    # It returns 1 if there ARE staged changes.
    print("Files are staged and ready for commit.")