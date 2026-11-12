#!/usr/bin/env python3
"""Generate an absolute-URL sitemap after the deployment host is known."""

from argparse import ArgumentParser
from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape

PAGES = (
    "index.html",
    "about.html",
    "services.html",
    "team.html",
    "facilities.html",
    "insurance.html",
    "community.html",
    "contact.html",
)


def main() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("base_url", help="Confirmed public origin, e.g. https://clinic.example")
    base_url = parser.parse_args().base_url.rstrip("/")
    parsed = urlparse(base_url)
    if parsed.scheme not in {"https", "http"} or not parsed.netloc or parsed.path:
        parser.error("base_url must be a public origin with no path, such as https://clinic.example")

    urls = "\n".join(
        f"  <url><loc>{escape(base_url + '/' + page)}</loc></url>" for page in PAGES
    )
    Path("sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n"
        "</urlset>\n",
        encoding="utf-8",
    )
    print(f"Wrote sitemap.xml for {len(PAGES)} pages at {base_url}")


if __name__ == "__main__":
    main()
