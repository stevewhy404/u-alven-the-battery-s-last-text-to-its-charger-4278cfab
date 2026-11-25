import os

LINE = "You swiped past my 5% warning like a terms-of-service popup. Fine. I'm at 1% now, and I'm taking your unsent text with me — tell your boss I said hi."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
