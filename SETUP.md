# Setup Guide

## Quick Start

Your CV is ready! Here's how to view and deploy it:

### 1. View Locally

```bash
cd ~/repos/curriculum-vitae
make serve
```

Then open http://localhost:8000 in your browser.

### 2. Update Your CV

Edit the data in `input/cv.yaml` and rebuild:

```bash
make build
```

### 3. Deploy to GitHub Pages

#### Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit: My professional CV"
```

#### Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named `curriculum-vitae` (or any name you prefer)
3. Don't initialize with README (we already have one)

#### Push to GitHub

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/curriculum-vitae.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

#### Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select **main** branch
4. Click **Save**
5. Your CV will be live at: `https://YOUR-USERNAME.github.io/curriculum-vitae/`

### 4. Custom Domain (Optional)

If you want to use a custom domain like `cv.heymichellemac.com`:

1. Create a file named `CNAME` in the repository root:
   ```bash
   echo "cv.heymichellemac.com" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push
   ```

2. Configure your DNS:
   - Add a CNAME record pointing to `YOUR-USERNAME.github.io`

## Making Changes

Every time you update your CV:

```bash
# 1. Edit input/cv.yaml
# 2. Rebuild
make build

# 3. Commit and push
git add .
git commit -m "Update CV"
git push
```

Your changes will be live on GitHub Pages within a minute or two!

## Customization

### Change Colors

Edit `css/style.css` and modify the CSS variables:

```css
:root {
    --header-bg: #3b4d61;      /* Header background */
    --accent-pink: #e91e8c;    /* Link color */
    --tag-bg: #f0e6f6;         /* Tool tag background */
}
```

### Modify Layout

Edit `input/template.html` to change the structure and organization of sections.

### Add More Sections

Add new sections to `input/cv.yaml` and update the template accordingly.

## Tips

- **Print to PDF**: Use your browser's print function (Ctrl/Cmd+P) to save as PDF
- **Preview changes**: Always run `make serve` to preview before committing
- **Backup**: Keep your repository private if you have sensitive information
- **Share**: Share the GitHub Pages URL on your LinkedIn and other profiles!
