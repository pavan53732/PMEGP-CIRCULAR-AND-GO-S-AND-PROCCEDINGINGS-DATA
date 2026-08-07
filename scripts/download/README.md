# Download Scripts

This folder hosts **document scrapers and crawlers** that fetch PMEGP-related PDFs from official government portals.

> **Status:** All scripts here are currently **planned** — none have been implemented yet. See [`../README.md`](../README.md) §2 for the roadmap.

---

## 1. Guidelines for New Scrapers

Before contributing a scraper, please:

1. **Open an Issue** describing the target portal and the document category you intend to scrape.
2. **Respect `robots.txt`** — verify the portal allows crawling of the target paths.
3. **Identify your User-Agent** — set a descriptive `User-Agent` string like:
   ```
   PMEGP-Archive-Bot/1.0 (https://github.com/pavan53732/PMEGP-CIRCULAR-AND-GO-S-AND-PROCCEDINGINGS-DATA; contact: <your-email>)
   ```
4. **Rate-limit aggressively** — at minimum a 1-second `time.sleep()` between requests. Government portals are not designed for high traffic.
5. **Cache responses** — store the raw HTML / PDF bytes locally so you don't re-download during development. Use a `data_raw/` folder (gitignored) outside the repo.
6. **Never commit credentials** — if the portal requires authentication, store credentials in a `.env` file (already in `.gitignore`).
7. **Manual review required** — scrapers must produce a queue of candidate URLs for human review, not auto-commit documents. The final registration must go through `scripts/metadata/generate_metadata.py`.

---

## 2. Planned Scrapers

| Script | Target Portal | Documents |
|---|---|---|
| `scrape_ap_govt_gos.py` | `ap.gov.in` | AP Government Orders related to PMEGP |
| `scrape_momsme.py` | `msme.gov.in` | Central Ministry of MSME PMEGP notifications |
| `scrape_slbc_ap.py` | `slbcap.nic.in` | SLBC AP agendas, minutes, and reports |
| `scrape_ap_industries.py` | `industries.ap.gov.in` | AP Commissioner of Industries proceedings |

---

## 3. Suggested Stack

- **HTTP**: `requests` (with `Session` for cookie persistence)
- **HTML parsing**: `beautifulsoup4` (`bs4`)
- **PDF text extraction**: `pdfminer.six` (pure Python, no Java dependency)
- **URL filtering**: `urllib.parse.urljoin` for relative-URL resolution
- **Scheduling**: `time.sleep(1.0)` between requests (do not use multi-threading)
