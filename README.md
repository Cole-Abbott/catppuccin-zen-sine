# Catppuccin for Sine

An unofficial Sine port of [Catppuccin for Zen Browser](https://github.com/catppuccin/zen-browser).

Choose Latte, Frappé, Macchiato, or Mocha and any of the fourteen upstream accents in Sine's mod settings. Automatic flavor follows browser appearance: Latte in light mode and Mocha in dark mode. The default accent is Mauve. No browser scripts or remote logo requests are needed.

## Install through Sine

1. Open Zen → **Settings → Sine Mods**.
2. Paste this repository URL into Sine's custom repository installation field:

   ```text
   https://github.com/Cole-Abbott/catppuccin-zen-sine
   ```

3. Install **Catppuccin**, then open its preferences to choose a flavor and accent.

Sine handles downloading the styles, enabling/disabling the theme, and checking this repository for updates. Reload open internal pages if necessary. No copying CSS into your profile is required. Sine must already be installed and working in your Zen profile.

If you used the earlier local package, remove that Catppuccin entry through Sine before installing from the repository. If you installed the original theme manually, remove its old CSS imports/rules to avoid conflicting copies.

For explicit Latte, light browser appearance gives the most consistent result; dark appearance suits the other three flavors. The port preserves upstream selectors, including their limitations on newer Zen UI elements.

## Manage or remove

Use Sine's normal enable/disable, preferences, update, and remove controls. The original Catppuccin repository does not contain this port; use the repository URL above.

## Optional offline installation

With Zen completely closed, Python 3 users can run `python3 install.py "/path/to/Zen/profile"` from a downloaded copy of this repository. Find the correct Profile Folder at `about:support` before quitting Zen. The installer checks the profile lock, backs up the Sine registry, and preserves other installed mods. It does not change your existing userChrome.css/userContent.css or Zen.app.

Offline installations disable update checks. To switch to normal repository updates, remove the offline entry through Sine and install using the GitHub URL above.

## Source and modifications

Upstream commit: `c855685442c6040c4dda9c8d3ddc7b708de1cbaa`.

The unmodified upstream theme files are frozen in `vendor/themes/`, with SHA-256 hashes in `PROVENANCE.json`. Run `python3 build.py` to regenerate the styles and preference schema. The generator replaces each theme's outer appearance condition with flavor/accent preference conditions and embeds the matching SVG instead of fetching a remote fallback. Colors, selectors, and nested styling come from upstream. The MIT license and original attribution are preserved. This is an independent adaptation, not an official Catppuccin release.

## Validation

Tested in a separate headless Zen **1.23.4b** profile with Sine **2.3.4.1c**:

- All **56** flavor/accent combinations returned their expected upstream accent color in browser chrome.
- All **56** returned their expected upstream accent color on `about:preferences`.
- The local installer registered the mod; Sine displayed both preference controls.
- Selecting Macchiato/Teal through Sine's controls updated the browser color.
- Unset preferences selected automatic appearance and Mauve.
- Disabling the mod through Sine restored the browser's prior accent color.

`VALIDATION.json` records these results. This checks native style application and Sine integration; it is not a full visual audit of every Zen surface or a guarantee of compatibility with other themes.
