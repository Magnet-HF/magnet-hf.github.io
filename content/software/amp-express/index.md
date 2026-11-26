---
{"title":"AMP-Express","description":"A MagNet utility for preparing FLAMP relay files from message documents.","section":"software","kind":"MagNet utility","order":11,"updated":"2026-11-26"}
---
AMP-Express prepares files for FLAMP without transmitting. It encodes a message document into the compressed, checksummed AMP-2 blocks FLAMP sends, wraps them as an FLMSG relay file (`.b2s`) ready for the relay workflow, and can clear-sign the original with the operator's own PGP key.

## Get the utility

- [Downloads](https://github.com/Magnet-HF/AMP-Express/releases): choose the newest release and download the zip under **Assets**.
- [Setup and documentation](https://github.com/Magnet-HF/AMP-Express#readme)
- [Report a problem](https://github.com/Magnet-HF/AMP-Express/issues)

## Prerequisites

- Windows 10 or 11. The installer sets up Python if needed.
- A callsign.
- For signing only: your own exported PGP private key. No key is supplied with AMP-Express.

Linux installation is documented in the application README. Detailed requirements, installation and troubleshooting are maintained there.

## Technical guidance

**MagNet-tested version: not yet recorded.** Version-specific changes are listed in each release's notes.

## Historical download

[Original AMP-Express v1.0 release](https://github.com/Magnet-HF/Mag-Windows/releases/tag/Amp-Express-v1.0) in the Mag-Windows repository.
