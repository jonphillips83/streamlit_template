import argparse
import getpass

import bcrypt

# uv run scripts/generate_password_hash.py


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a bcrypt password hash for Streamlit secrets."
    )
    parser.add_argument(
        "--password",
        help="Plaintext password to hash. If omitted, you will be prompted securely.",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=12,
        help="Bcrypt cost factor. Defaults to 12.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    password = args.password or getpass.getpass("Password to hash: ")

    if not password:
        raise SystemExit("Password cannot be empty.")

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(rounds=args.rounds),
    ).decode("utf-8")

    print(hashed_password)


if __name__ == "__main__":
    main()
