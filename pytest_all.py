#!/usr/bin/env python3
from pathlib import Path
from subprocess import run

if __name__ == "__main__":
    app_folders = [f for f in Path().cwd().glob('*') if f.is_dir()
    if f.name.startswith('app')]

    [run(['pytest', f]) for f in app_folders]
