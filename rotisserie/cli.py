import typing as t
import sys
from .app import app, SECRET_KEY
from .config import APP_CONFIGS


def debug():
    print(f"SECRET_KEY: {SECRET_KEY}")
    app.run(**APP_CONFIGS)


COMMANDS: t.Dict[str, t.Callable] = {
    "debug": debug,
    "production": lambda: print("Not done yet")
}


def main(args: t.List[str]) -> int:
    function = COMMANDS.get(args[1], None)
    if function is None:
        print(f"Could not find command named {args[1]}")
        return 1
    else:
        try:
            function()
        except Exception as e:
            raise e
        else:
            return 0


def run():
    return main(sys.argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
