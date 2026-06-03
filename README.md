# Wenzel.no Web Project

<!-- Status badges -->
[![CI](https://img.shields.io/github/actions/workflow/status/xvenca/wenzl/.github/workflows/ci.yml?branch=main)](https://github.com/xvenca/wenzl/actions/workflows/ci.yml)
[![Deploy](https://img.shields.io/github/actions/workflow/status/xvenca/wenzl/.github/workflows/deploy.yml?branch=main)](https://github.com/xvenca/wenzl/actions/workflows/deploy.yml)
[![Pages Status](https://img.shields.io/website?down_color=red&down_message=down&up_color=green&up_message=up&url=https://xvenca.github.io/wenzl/)](https://xvenca.github.io/wenzl/)
[![Last Commit](https://img.shields.io/github/last-commit/xvenca/wenzl)](https://github.com/xvenca/wenzl/commits/main)
[![Dependabot](https://img.shields.io/badge/dependabot-enabled-brightgreen)](https://github.com/xvenca/wenzl/security/dependabot)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)

![Implemented](https://img.shields.io/badge/implemented-5%2F18-blue)
![Remaining](https://img.shields.io/badge/remaining-13-orange)
![Project Status](https://img.shields.io/badge/status-Early-red)

[Plan details](doc/implementation-plan.md)


## Overview
This project is for the website **wenzel.no**, a personal showcase of local craftsmanship and farming activities based in Bergen, Norway. The site will serve as a digital portfolio, similar to an Instagram feed, highlighting unique products and services without any pricing or sales focus. The website must be available in **Norwegian (Bokmål)** and **English**, with a simple, minimalist design emphasizing visuals and authenticity.

The site reflects the owner's hobbies and potential future business ventures, including beekeeping, crafting wooden beehives, creating laser-cut tourism items, farming with chickens, and growing oyster mushrooms. It should feel local, approachable, and community-driven, avoiding any corporate or overly commercial vibe. The site will be built using **Hugo**, a static site generator, with content written in markdown for simplicity and speed.

## Objectives
- Showcase the owner's skills and projects in a clean, visual format.
- Provide a contact point for interested visitors (email and phone number).
- Support bilingual content (Norwegian Bokmål and English).
- Use Hugo for a static, lightweight, and fast website with no backend.
- Host independently, avoiding "American servers" (e.g., no AWS or Google Cloud).
- Avoid any mention of prices or direct sales.
- Optimize for speed and minimal resource usage.

## Website Structure
The website will consist of the following sections, each with a focus on visuals (photos) and brief descriptions in markdown files. No pricing or sales pitches are included. Content will be organized in Hugo's content directory with separate folders for Norwegian and English.

### 1. Homepage
- **File**: `content/no/_index.md` (Norwegian), `content/en/_index.md` (English)
- **Title**: Wenzel.no
- **Content**: A brief welcome message introducing the owner as a local craftsman and farmer in Bergen, passionate about unique projects.
- **Call-to-action**: "See what I do" (links to sections below) and "Contact me" (email: info@wenzel.no, phone: +47 926 20569).
- **Visuals**: A hero image of Bergen landscape or a crafted product (e.g., wooden beehive or oyster mushroom).
- **Frontmatter**:
  ```yaml
  title: "Wenzel.no"
  description: "Local crafts and farming from Bergen"
  image: "/images/hero.svg"
  ```

### 2. Beekeeping (Včelařství / Birøkt)
- **File**: `content/no/birokt.md`, `content/en/beekeeping.md`
- **Content**:
  - Free bee swarm collection in Bergen: "Got a swarm? I’ll come and take it away for free."
  - Pollination services: "Need bees for your farm? I can bring them for pollination."
  - Handcrafted wooden beehives: "I make sturdy beehives from solid wood."
  - Special heart-shaped frames: "Unique frames for love-shaped honeycombs, perfect for beekeepers."
- **Visuals**: Photos of beehives, heart-shaped honeycombs, bees in action.
- **Note**: Emphasize "Med z lásky" (Honey from Love) for heart-shaped frames, but no mention of selling honey.
- **Frontmatter**:
  ```yaml
  title: "Birøkt / Beekeeping"
  description: "Free swarm collection, pollination, and handcrafted beehives"
  image: "/images/beekeeping.svg"
  ```

### 3. Tourism Items (Turistické předměty / Turistartikler)
- **File**: `content/no/turistartikler.md`, `content/en/tourism-items.md`
- **Content**:
  - Handcrafted laser-cut items: "I create unique souvenirs like plant stands, decorative maps, and custom designs."
  - Focus on local Bergen-inspired designs: "Made with love for tourists and locals."
- **Visuals**: Photos of laser-cut plant stands, maps, or other prototypes (e.g., "brigišky", "gunlehalte").
- **Note**: Keep it visual, like a portfolio. No technical details about laser cutting.
- **Frontmatter**:
  ```yaml
  title: "Turistartikler / Tourism Items"
  description: "Handcrafted souvenirs with a Bergen touch"
  image: "/images/tourism.svg"
  ```

### 4. Farm (Farma / Gård)
- **File**: `content/no/gard.md`, `content/en/farm.md`
- **Content**:
  - Chicken farming: "I raise happy chickens and share their eggs with the community."
  - Egg hatching: "Got a coop? I can provide eggs for hatching and help you start."
  - Collaboration: "Let’s work together – you raise chickens, I’ll supply eggs."
- **Visuals**: Photos of chickens, coops, or eggs (no sales, just a cozy farm vibe).
- **Note**: Keep it light, like a diary. Avoid any commercial tone.
- **Frontmatter**:
  ```yaml
  title: "Gård / Farm"
  description: "Chickens, eggs, and community farming"
  image: "/images/farm.svg"
  ```

### 5. Oyster Mushrooms (Hlíva ústřičná / Østerssopp)
- **File**: `content/no/osterssopp.md`, `content/en/oyster-mushrooms.md`
- **Content**:
  - Growing oyster mushrooms: "I cultivate oyster mushrooms with care."
  - Forest integration: "Find my wooden stump in the woods with a QR code linking here."
  - Community idea: "Picked some mushrooms? Support my work if you like."
- **Visuals**: Photos of mushrooms, wooden stumps with QR codes in a forest setting.
- **Note**: Highlight the quirky stump idea as a unique, local touch.
- **Frontmatter**:
  ```yaml
  title: "Østerssopp / Oyster Mushrooms"
  description: "Locally grown mushrooms with a unique twist"
  image: "/images/mushrooms.svg"
  ```

### 6. Beekeeping App (Aplikace pro včelaře / App for birøktere)
- **File**: `content/no/app.md`, `content/en/app.md`
- **Content**:
  - Upcoming app for beekeepers: "Track your bees, make notes, and manage your hives locally."
  - Free for Norwegian beekeepers: "Coming soon to Google Play and App Store."
- **Visuals**: Mockup of the app interface (if available) or a placeholder image of a beehive.
- **Note**: Keep it vague, as the app is not yet developed.
- **Frontmatter**:
  ```yaml
  title: "App for birøktere / Beekeeping App"
  description: "Coming soon: a free app for Norwegian beekeepers"
  image: "/images/app.svg"
  ```

### 7. Contact
- **File**: `content/no/kontakt.md`, `content/en/contact.md`
- **Content**:
  - "Want to collaborate or learn more? Reach out!"
  - Email: info@wenzel.no
  - Phone: +47 926 20569
- **Visuals**: Simple icon or photo of Bergen to tie it to the location.
- **Note**: No social media links, emphasizing independence from "American servers."
- **Frontmatter**:
  ```yaml
  title: "Kontakt / Contact"
  description: "Get in touch for collaborations or inquiries"
  image: "/images/contact.svg"
  ```

## Technical Requirements
- **Framework**: Hugo (static site generator) for fast, lightweight deployment.
- **Content Format**: All content in markdown files, organized in `content/no/` and `content/en/` directories for bilingual support.
- **Languages**: Norwegian (Bokmål) and English, with a language toggle (e.g., NO/EN) in the navigation.
- **Design**: Minimalist, mobile-friendly, image-heavy (Instagram-like). Use Tailwind CSS for styling.
- **Assets**: Store images in `static/images/` (e.g., hero.svg, beekeeping.svg). Use placeholders until real photos are provided.
- **QR Code**: Generate a QR code linking to the homepage for the Oyster Mushroom section (e.g., using a Hugo shortcode or static image).
- **No Backend**: Fully static, no database or server-side processing.
- **Hosting**: Deploy on an independent European server (e.g., Netlify with a European provider or a local Norwegian host).
- **SEO**: Optimize for Bergen-related keywords (e.g., "Bergen beekeeping," "local crafts Bergen"). Include meta descriptions in frontmatter.
- **Accessibility**: Ensure alt tags for images and readable text (minimum 16px font size).
- **Performance**: Optimize images (compress to <200KB), minify CSS/JS, and use Hugo’s built-in minification.
- **Navigation**: Simple menu with links to all sections and a language toggle.

## Hugo Setup
1. **Directory Structure**:
   ```
   wenzel.no/
   ├── content/
   │   ├── no/
   │   │   ├── _index.md
   │   │   ├── birokt.md
   │   │   ├── turistartikler.md
   │   │   ├── gard.md
   │   │   ├── osterssopp.md
   │   │   ├── app.md
   │   │   ├── kontakt.md
   │   ├── en/
   │   │   ├── _index.md
   │   │   ├── beekeeping.md
   │   │   ├── tourism-items.md
   │   │   ├── farm.md
   │   │   ├── oyster-mushrooms.md
   │   │   ├── app.md
   │   │   ├── contact.md
   ├── static/
   │   ├── images/
   │   │   ├── hero.jpg
   │   │   ├── beekeeping.jpg
   │   │   ├── tourism.jpg
   │   │   ├── farm.jpg
   │   │   ├── mushrooms.jpg
   │   │   ├── app.jpg
   │   │   ├── contact.jpg
  ├── static/
  │   ├── images/
  │   │   ├── hero.svg
  │   │   ├── beekeeping.svg
  │   │   ├── tourism.svg
  │   │   ├── farm.svg
  │   │   ├── mushrooms.svg
  │   │   ├── app.svg
  │   │   ├── contact.svg
   ├── themes/
   │   ├── [your-theme]/
   ├── config.toml
   ```

2. **Config Example** (`config.toml`):
   ```toml
   baseURL = "https://wenzel.no/"
   defaultContentLanguage = "no"
   [languages]
     [languages.no]
       languageName = "Norsk"
       contentDir = "content/no"
     [languages.en]
       languageName = "English"
       contentDir = "content/en"
   [params]
     title = "Wenzel.no"
     description = "Local crafts and farming from Bergen, Norway"
  images = ["/images/hero.svg"]
   [menu]
     [[menu.main]]
       name = "Hjem"
       url = "/"
       weight = 1
     [[menu.main]]
       name = "Birøkt"
       url = "/birokt/"
       weight = 2
     # Add other menu items similarly
   ```

3. **Theme**: Use a lightweight Hugo theme (e.g., `hugo-theme-ananke` or a custom Tailwind-based theme).
4. **Build Command**: `hugo --minify` to generate a compressed static site in the `public/` folder.

## Development Notes
- Write all content in markdown for easy updates.
- Use Hugo’s i18n for bilingual support (e.g., separate `i18n/no.yaml` and `i18n/en.yaml` for translations).
- Compress images to ensure fast loading (aim for <200KB per image).
- Implement a QR code shortcode in Hugo for the Oyster Mushroom section (e.g., `{{</ qrcode url="https://wenzel.no" >}}`).
- Test language toggle functionality on desktop and mobile.
- Ensure no external dependencies (e.g., no Google Fonts, use system fonts or locally hosted ones).
- Use Tailwind CSS for styling, included via CDN or locally compiled for speed.
- Test the site with `hugo server` locally before deployment.

## Next Steps
1. Initialize a Hugo project: `hugo new site wenzel.no`.
2. Create markdown files for each section in `content/no/` and `content/en/`.
3. Add placeholder images to `static/images/`.
4. Choose or create a Hugo theme with Tailwind CSS integration.
5. Implement a language toggle in the navigation.
6. Generate a QR code for the Oyster Mushroom section.
7. Test responsiveness and performance (aim for <2s load time).
8. Deploy on an independent European server (e.g., Netlify with a European provider or a local Norwegian host).

## Try it locally

Run the development server and open http://localhost:1313/:

```powershell
hugo server -D
```

Build the production site into `public/`:

```powershell
hugo --minify
```
