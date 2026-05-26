import argparse
from pathlib import Path

from app.ui import RepoTutorApp


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="repotutor",
        description="RepoTutor – Codeverständnis per Terminal-UI.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        metavar="PROJEKTPFAD",
        help="Pfad zum Projekt (optional; sonst Eingabe in der TUI)",
    )
    args = parser.parse_args()
    project_path = Path(args.path).expanduser().resolve() if args.path else None
    RepoTutorApp(project_path=project_path).run()


if __name__ == "__main__":
    main()
