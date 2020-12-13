import argparse
from pathlib import Path

from pikepdf import Pdf


def decrypt_password(src_path: Path, dst_path: Path, password: str):
    with Pdf.open(str(src_path), password=password) as pdf:
        pdf.save(str(dst_path))
    return


def decrypt_all(src_dir: Path, dst_dir: Path, src_pass: str):
    for src_path in src_dir.glob("*.pdf"):
        print(src_path)
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst_path = dst_dir / f"{src_path.stem}.pdf"
        decrypt_password(src_path, dst_path, src_pass)
    print("done.")
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Unlock password for all PDF files in the directory.")
    parser.add_argument("src_dir")
    parser.add_argument("dst_dir")
    parser.add_argument("password_file")
    args = parser.parse_args()


    src_dir = Path(args.src_dir)
    dst_dir = Path(args.dst_dir)
    with Path(args.password_file).open("rt") as f:
        src_pass = f.readline().strip('\n')
    print(f"password: {src_pass}")

    decrypt_all(src_dir, dst_dir, src_pass)
