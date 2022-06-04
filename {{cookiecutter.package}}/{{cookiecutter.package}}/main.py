import argparse
import logging
import sys

log = logging.getLogger(__name__)


def init_logging(verbose: bool) -> None:
    """Initialize the package logger."""
    fmt = logging.Formatter("%(asctime)s %(name)s [%(levelname)s] %(message)s")
    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    ch.setLevel(logging.DEBUG if verbose else logging.INFO)
    pkg_log = logging.getLogger(__package__)
    pkg_log.addHandler(ch)
    pkg_log.setLevel(logging.DEBUG if verbose else logging.INFO)


def main() -> int:
    """Just a main function."""
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    init_logging(args.verbose)

    try:
        pass
    except Exception:
        log.exception("Unhandled error")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
