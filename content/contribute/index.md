---
{"title":"Share what works.","description":"Contribute a guide, radio configuration, correction, or supporting document through a reviewed GitHub submission.","section":"contribute","updated":"2026-10-23"}
---
## Who can contribute?

Approved contributors with repository write access can upload documents on a new branch. Other readers can propose changes through a fork or [request a guide](https://github.com/Magnet-HF/magnet-hf.github.io/issues/new/choose). The repository owner assigns access; publication follows the review process configured by the administrator.

## Upload a document in your browser

1. Open the [hub repository](https://github.com/Magnet-HF/magnet-hf.github.io) and create a branch such as `docs/your-guide` from `main`.
2. Open `documents/`, choose **Add file → Upload files**, and upload a folder with a short descriptive name containing the PDF and, if available, its editable source. Browser uploads are limited to 25 MiB per file.
3. Add a Markdown landing page under `content/operational-guidance/your-guide/index.md` or `content/radio-configurations/manufacturer/model/index.md`. Copy the [guide template](https://github.com/Magnet-HF/magnet-hf.github.io/blob/main/templates/guide.md) and fill in its metadata and review details.
4. Link the landing page to `/documents/your-guide/your-file.pdf`. Keep the file name stable when revising a guide.
5. Commit to your branch and open a pull request. Describe what changed, its author/source, and any testing performed. The site build checks internal links; a reviewer checks technical accuracy and placement.
6. After approval and merge, the publishing workflow updates the library. Guides with the appropriate `section` metadata appear automatically in their section's directory.

Do not upload executables as documentation. Software installers belong in project releases. A repository administrator can help with documents exceeding the browser upload limit.

## Before submitting

- Confirm you have permission to publish the material and identify its author/source.
- Include supported equipment, software versions, limitations, and a verification date when known.
- Remove credentials, private rosters, personal contact details, and operational secrets. This is a public library.
- Preserve one authoritative copy. Link related tool pages to the same guide.
- An untested procedure may be submitted, but label its status accurately.

## Make a small correction

Use **Suggest an edit** at the bottom of any page. Update the Markdown, propose a branch, and open a pull request. Updating the page's `updated` date records an editorial change; it is separate from a station-test date.

## Maintaining software recommendations

Tool pages have a **Technical guidance** section. Record a suggested version, who approved or tested it, the date, and the applicable platform or radio. Publisher-listed versions may be recorded as context, but do not label them MagNet-tested without evidence.

[GitHub's upload instructions](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) provide additional help.
