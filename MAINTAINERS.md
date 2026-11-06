# Maintainer setup and handoff

## Owner actions before publication

Magnet-HF is a GitHub organization. Use individual accounts and grant maintainers access to the repositories they manage.

1. Create public `MAGNET-HF.github.io`, initialized with a README, and invite the contributor under **Settings → Collaborators**.
2. Upload this repository's contents, including `.github/workflows/pages.yml`.
3. Select **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. In **Settings → Branches** or **Rules → Rulesets**, protect `main`: require a pull request, at least one approval, and the `Build and check library` check. Require resolved conversations and dismiss stale approvals. Apply protections to administrators if the group wants all publication reviewed.
5. Configure the `github-pages` environment to allow deployments only from `main`.
6. Add named reviewers in `.github/CODEOWNERS` once the administrators identify the appropriate GitHub usernames. No fictional reviewer is preconfigured.
7. Confirm an approved pull request builds and a merge deploys successfully.

These files implement the contribution process and build checks. Branch protection, contributor invitations, environment protection, and CODEOWNERS identities are administrative configuration and are not applied automatically by this package.

## Stable website-card destinations

| Website card | Hub destination |
| --- | --- |
| JS8Call Subspace — MagNet Edition | https://magnet-hf.github.io/software/js8call/ |
| CommStat | https://magnet-hf.github.io/software/commstat/ |
| SpotterX — MagNet Edition | https://magnet-hf.github.io/software/spotterx/ |
| VarAC | https://magnet-hf.github.io/software/varac/ |
| fldigi | https://magnet-hf.github.io/software/fldigi/ |
| flmsg | https://magnet-hf.github.io/software/flmsg/ |
| flrig | https://magnet-hf.github.io/software/flrig/ |
| flamp | https://magnet-hf.github.io/software/flamp/ |
| Meshtastic | https://magnet-hf.github.io/software/meshtastic/ |
| CommsPlan | https://magnet-hf.github.io/software/commsplan/ |
| Forms / public key | https://magnet-hf.github.io/resources/ |

Use **Downloads & Setup** as the card action. Link the existing combined FLDIGI/FLMSG card to `/software/fldigi/` until the website splits it. Keep website descriptions brief; changing upstream URLs and technical versions belong here.

## Content requiring maintainer input

- Confirm suggested versions, test combinations, reviewer names, and dates. The site explicitly distinguishes publisher versions from MagNet approval.
- Confirm SpotterX platform support, installation, dependencies, and bundled forms with its developer.
- Add the supplied guide's author, revision, publication terms, and station-test results when available.
- Confirm current forms packages and establish a trusted public-key fingerprint/import guide.
- Publish radio-specific guides as contributors provide them.

## SpotterX migration

Create the dedicated `SpotterX` repository with developer and hub-maintainer access. Copy the original package byte-for-byte, verify its SHA-256, preserve upstream credits and the original release description, and publish a versioned release. The workspace's `migration/` tooling prepares and checks this migration without removing original releases.

Only after the new release is verified, replace the SpotterX tool page's legacy download URL with `https://github.com/Magnet-HF/SpotterX/releases` and replace the transition paragraph with links to that repository's documentation and issues. Keep the website card pointing to the stable hub page.

Original Mag-Windows releases remain available. AMP-Express is a separate utility and must not be included in the SpotterX release.

## Review cadence

Check links and upstream release pages when a maintainer receives an update or an operator reports a problem. Update version recommendations only with an explicit basis. A page's editorial date is not a hardware verification date.
