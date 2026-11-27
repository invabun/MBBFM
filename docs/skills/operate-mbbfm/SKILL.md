---
name: operate-mbbfm
description: Prepare and verify an MBBFM article, YouTube listing or site-content update in the Jekyll repository.
---

# Operate MBBFM

MBBFM is the publication at the URL in [_config.yml](../../../_config.yml). Its checked-in application exposes no MCP tools or database-write API. Use Git for editorial input and Jekyll for preview. The CRM, 3dforger.com, 3dforger.online and the Synology archive have no role in an MBBFM content update.

## Prepare the requested change

- **Article** — obtain the approved title, publication date, body, and any supplied tags or assets. Locate the existing entry under `_posts/` before editing. For a new article, use `_posts/YYYY-MM-DD-slug.md` with YAML `title` and `date`; follow a nearby published article for optional tags. Preserve the filename and existing public permalink on ordinary edits. Use sanctioned public content only.
- **YouTube listing** — [_tabs/youtube.md](../../../_tabs/youtube.md) renders [_data/youtube.yml](../../../_data/youtube.yml). For an approved feed refresh, [tools/fetch_youtube.py](../../../tools/fetch_youtube.py) reads the configured channel feed and rewrites that whole file. Review the diff for missing older entries, duplicate IDs, valid URLs, titles and thumbnails. A narrower correction can edit the one tracked row.
- **Blog archive import** — [tools/import_blogspot.py](../../../tools/import_blogspot.py) imports a whole external feed. Run bulk imports only for that explicit task in a clean task branch, then review the changed post and asset paths.

The public editorial source lives in Git. Generated `_site/` is replaceable. Private business records and backups belong in their owning system. A site edit needs no database connection.

## Preview and verify

From a fresh development checkout use Ruby 3.3 (as in CI), Bundler and `bundle install`. Run `bash tools/test.sh` to build and check internal links. This script recreates the generated `_site/` directory. Run `bash tools/run.sh` for a local browser preview. For an article, follow it from the listing to its permalink, check title/date, body and assets. For a video, verify the intended tile and its destination. External destinations are outside the internal link check.

Push proposed changes on a task branch. The [Pages workflow](../../../.github/workflows/pages-deploy.yml) builds and deploys on pushes to `main` or manual dispatch. The owner's production decision covers that publish step. Before an approved release identify the previous deployed commit, domain and rollback target; after release verify the same page and assets in the browser. Record the tested commit, environment and result and distinguish preview from publication.

When inputs, generator or publish triggers change, update this skill in the same change. README and `docs/` are excluded from site generation by the current Jekyll configuration.
