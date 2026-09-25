"""jazzcommon — canonical jazz standards reference CLI and dataset."""

from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from typing import Any

STANDARDS: list[dict[str, Any]] = [
    {
        "title": "Autumn Leaves",
        "aliases": ["Les Feuilles Mortes"],
        "composer": "Joseph Kosma",
        "key": "E minor",
        "form": "AABA",
        "tempo": "medium",
        "era": "standard",
    },
    {
        "title": "All the Things You Are",
        "aliases": [],
        "composer": "Jerome Kern",
        "key": "E-flat major",
        "form": "AABA",
        "tempo": "medium-up",
        "era": "standard",
    },
    {
        "title": "Take the A Train",
        "aliases": [],
        "composer": "Billy Strayhorn",
        "key": "C major",
        "form": "AABA",
        "tempo": "medium-up",
        "era": "swing",
    },
    {
        "title": "So What",
        "aliases": [],
        "composer": "Miles Davis",
        "key": "D Dorian",
        "form": "AABA",
        "tempo": "medium",
        "era": "modal",
    },
    {
        "title": "Blue in Green",
        "aliases": [],
        "composer": "Miles Davis",
        "key": "G major",
        "form": "AABA",
        "tempo": "ballad",
        "era": "modal",
    },
    {
        "title": "Round Midnight",
        "aliases": ["'Round Midnight", "Love & Peace"],
        "composer": "Thelonious Monk",
        "key": "C minor",
        "form": "AABA",
        "tempo": "medium",
        "era": "bop",
    },
    {
        "title": "Giant Steps",
        "aliases": [],
        "composer": "John Coltrane",
        "key": "B major",
        "form": "AABA",
        "tempo": "up",
        "era": "hardbop",
    },
    {
        "title": "A Love Supreme, Pt. 1 - Acknowledgement",
        "aliases": ["A Love Supreme"],
        "composer": "John Coltrane",
        "key": "C minor",
        "form": "head-solos",
        "tempo": "medium",
        "era": "postbop",
    },
    {
        "title": "Summertime",
        "aliases": [],
        "composer": "George Gershwin",
        "key": "C minor",
        "form": "AABA",
        "tempo": "ballad",
        "era": "standard",
    },
    {
        "title": "Stardust",
        "aliases": ["Star Dust"],
        "composer": "Hoagy Carmichael",
        "key": "C major",
        "form": "AABA",
        "tempo": "ballad",
        "era": "early",
    },
    {
        "title": "Body and Soul",
        "aliases": [],
        "composer": "Johnny Green",
        "key": "D minor",
        "form": "AABA",
        "tempo": "medium-up",
        "era": "standard",
    },
    {
        "title": "Take the Five",
        "aliases": ["Take Five"],
        "composer": "Paul Desmond",
        "key": "E-flat minor",
        "form": "ABAC",
        "tempo": "medium",
        "era": "postbop",
    },
    {
        "title": "Satin Doll",
        "aliases": [],
        "composer": "Duke Ellington",
        "key": "C major",
        "form": "AABA",
        "tempo": "medium-up",
        "era": "swing",
    },
    {
        "title": "In a Mellow Tone",
        "aliases": [],
        "composer": "Duke Ellington",
        "key": "C major",
        "form": "AABA",
        "tempo": "medium-up",
        "era": "swing",
    },
    {
        "title": "Moore Something",
        "aliases": [],
        "composer": "Charlie Parker",
        "key": "F major",
        "form": "AABA",
        "tempo": "up",
        "era": "bop",
    },
    {
        "title": "Donna Lee",
        "aliases": [],
        "composer": "Charlie Parker",
        "key": "E-flat major",
        "form": "AABA",
        "tempo": "up",
        "era": "bop",
    },
    {
        "title": "Cherokee",
        "aliases": [],
        "composer": "Ray Noble",
        "key": "A major",
        "form": "AABA",
        "tempo": "up",
        "era": "bop",
    },
    {
        "title": "Oleo",
        "aliases": [],
        "composer": "Sonny Rollins",
        "key": "B-flat major",
        "form": "AABA",
        "tempo": "up",
        "era": "hardbop",
    },
    {
        "title": "St Thomas",
        "aliases": [],
        "composer": "Sonny Rollins",
        "key": "E-flat major",
        "form": "AABA",
        "tempo": "up",
        "era": "hardbop",
    },
    {
        "title": "Cantaloupe Island",
        "aliases": [],
        "composer": "Herbie Hancock",
        "key": "C major",
        "form": "AABA",
        "tempo": "medium",
        "era": "postbop",
    },
    {
        "title": "Maiden Voyage",
        "aliases": [],
        "composer": "Herbie Hancock",
        "key": "E-flat major",
        "form": "AABA",
        "tempo": "medium",
        "era": "postbop",
    },
    {
        "title": "Watermelon Man",
        "aliases": [],
        "composer": "Herbie Hancock",
        "key": "A-flat major",
        "form": "AABA",
        "tempo": "medium-up",
        "era": "postbop",
    },
    {
        "title": "Sidewinder",
        "aliases": ["The Sidewinder"],
        "composer": "Lee Morgan",
        "key": "B-flat major",
        "form": "AABA",
        "tempo": "medium-up",
        "era": "hardbop",
    },
    {
        "title": "Mercy, Mercy, Mercy",
        "aliases": [],
        "composer": "Cannonball Adderley",
        "key": "E-flat major",
        "form": "AABA",
        "tempo": "medium",
        "era": "postbop",
    },
    {
        "title": "Moanin'",
        "aliases": ["Moanin"],
        "composer": "Charles Mingus",
        "key": "B-flat minor",
        "form": "AABA",
        "tempo": "medium",
        "era": "hardbop",
    },
    {
        "title": "Goodbye Pork Pie Hat",
        "aliases": [],
        "composer": "Charles Mingus",
        "key": "F minor",
        "form": "AABA",
        "tempo": "ballad",
        "era": "hardbop",
    },
    {
        "title": "Blue Bossa",
        "aliases": [],
        "composer": "Joe Henderson",
        "key": "C minor",
        "form": "AABA",
        "tempo": "medium-up",
        "era": "postbop",
    },
    {
        "title": "Recorda Me",
        "aliases": [],
        "composer": "Joe Henderson",
        "key": "E-flat major",
        "form": "AABA",
        "tempo": "medium-up",
        "era": "postbop",
    },
    {
        "title": "Naima",
        "aliases": [],
        "composer": "John Coltrane",
        "key": "E-flat major",
        "form": "AABA",
        "tempo": "ballad",
        "era": "postbop",
    },
    {
        "title": "Moment's Notice",
        "aliases": [],
        "composer": "John Coltrane",
        "key": "C minor",
        "form": "AABA",
        "tempo": "up",
        "era": "postbop",
    },
    {
        "title": "Pent-Up House",
        "aliases": [],
        "composer": "Sonny Rollins",
        "key": "B-flat major",
        "form": "AABA",
        "tempo": "up",
        "era": "hardbop",
    },
]


def _normalize(text: str) -> str:
    return text.strip().lower()


def _match(text: str, term: str) -> bool:
    norm_text = _normalize(text)
    norm_term = _normalize(term)
    return norm_term in norm_text


def _search(term: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for std in STANDARDS:
        haystack = " ".join(
            [
                std.get("title", ""),
                *std.get("aliases", []),
                std.get("composer", ""),
                std.get("form", ""),
            ]
        )
        if _match(haystack, term):
            results.append(std)
    return results


def _find_by_title(title: str) -> dict[str, Any] | None:
    for std in STANDARDS:
        if _normalize(std["title"]) == _normalize(title):
            return std
        for alias in std.get("aliases", []):
            if _normalize(alias) == _normalize(title):
                return std
    return None


def _format_record(record: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"Title: {record['title']}")
    lines.append(f"Composer: {record.get('composer', '')}")
    lines.append(f"Key: {record.get('key', '')}")
    lines.append(f"Form: {record.get('form', '')}")
    lines.append(f"Tempo: {record.get('tempo', '')}")
    lines.append(f"Era: {record.get('era', '')}")
    aliases = record.get("aliases", [])
    if aliases:
        lines.append(f"Aliases: {', '.join(aliases)}")
    return "\n".join(lines)


def _table_row(record: dict[str, Any]) -> str:
    return (
        f"{record['title']:<32} "
        f"{record.get('composer', ''):<18} "
        f"{record.get('key', ''):<12} "
        f"{record.get('form', ''):<10} "
        f"{record.get('era', ''):<8}"
    )


def _list_plain() -> str:
    return "\n".join(_table_row(r) for r in STANDARDS)


def _search_plain(term: str) -> list[str]:
    return [_table_row(r) for r in _search(term)]


def _show_plain(title: str) -> str:
    record = _find_by_title(title)
    if record is None:
        return f"jazzcommon: no standard found for '{title}'"
    return _format_record(record)


def _tags_plain() -> str:
    tags = sorted({r.get("era", "") for r in STANDARDS})
    return "\n".join(tags)


def _export_json() -> str:
    return json.dumps(STANDARDS, ensure_ascii=False, indent=2)


def _export_csv() -> str:
    if not STANDARDS:
        return ""
    header = ["title", "composer", "key", "form", "tempo", "era"]
    rows: list[list[str]] = []
    for r in STANDARDS:
        rows.append(
            [
                r.get("title", ""),
                r.get("composer", ""),
                r.get("key", ""),
                r.get("form", ""),
                r.get("tempo", ""),
                r.get("era", ""),
            ]
        )
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(header)
    writer.writerows(rows)
    return buf.getvalue()


def _resolve_command(args: argparse.Namespace) -> str:
    if args.command == "list":
        return _list_plain()
    if args.command == "search":
        return "\n".join(_search_plain(args.search_term))
    if args.command == "show":
        return _show_plain(args.show_title)
    if args.command == "tags":
        return _tags_plain()
    if args.command == "export":
        if args.export_format == "json":
            return _export_json()
        if args.export_format == "csv":
            return _export_csv()
        return (
            f"jazzcommon: "
            f"unknown export format '{args.export_format}'"
        )
    return ""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="jazzcommon",
        description="Canonical jazz standards reference CLI and dataset.",
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "list", help="List all canonical standards."
    )
    search_p = subparsers.add_parser(
        "search", help="Search title, aliases, composer, and form."
    )
    search_p.add_argument(
        "search_term", metavar="TERM", help="Search term."
    )
    show_p = subparsers.add_parser(
        "show", help="Show one standard by title or alias."
    )
    show_p.add_argument(
        "show_title", metavar="TITLE", help="Standard title or alias."
    )
    subparsers.add_parser("tags", help="List unique era tags.")
    export_p = subparsers.add_parser(
        "export", help="Export the dataset."
    )
    export_p.add_argument(
        "--format",
        dest="export_format",
        choices=["json", "csv"],
        default="json",
        help="Export format.",
    )

    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    output = _resolve_command(args)
    print(output)

    if args.command == "show" and output.startswith("jazzcommon:"):
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
