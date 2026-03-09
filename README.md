# Curriculum Vitae

A modern, responsive CV/resume website generated from YAML data. This project makes it easy to maintain your professional CV as structured data and generate a beautiful HTML website.

## Features

- **YAML-based data**: Easy to update and version control your CV content
- **Responsive design**: Looks great on desktop, tablet, and mobile
- **Print-friendly**: Optimized CSS for printing to PDF
- **Modern styling**: Clean, professional design with smooth animations
- **Easy to customize**: Simple template and CSS structure

## Quick Start

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```bash
   cd curriculum-vitae
   ```

2. Install dependencies (this creates a virtual environment):
   ```bash
   make install
   ```

   Or manually:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   ```

3. Update your information in `input/cv.yaml`

4. Generate your CV:
   ```bash
   make build
   ```

5. View your CV:
   ```bash
   make serve
   ```
   Then open http://localhost:8000 in your browser

## Project Structure

```
curriculum-vitae/
├── input/
│   ├── cv.yaml           # Your CV data (edit this!)
│   └── template.html     # HTML template
├── css/
│   └── style.css         # Styling
├── js/
│   └── main.js           # JavaScript functionality
├── out/                  # Generated output
├── generate.py           # Python script to generate HTML
├── requirements.txt      # Python dependencies
├── Makefile             # Build commands
└── README.md            # This file
```

## Updating Your CV

1. Edit `input/cv.yaml` with your information
2. Run `make build`
3. Open `index.html` in your browser

### YAML Structure

The `cv.yaml` file is organized into sections:

- **personal**: Name, title, location, contact info
- **summary**: Brief professional summary
- **experience**: Work history
- **volunteer**: Volunteer work
- **education**: Academic background
- **certifications**: Professional certifications
- **skills**: Technical and soft skills

See `input/cv.yaml` for the full structure with examples.

## Customization

### Styling

Edit `css/style.css` to customize colors, fonts, and layout. CSS variables at the top make it easy to change the color scheme:

```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    /* ... */
}
```

### Template

Modify `input/template.html` to change the structure and layout. The template uses Jinja2 syntax for dynamic content.

## Deployment

### GitHub Pages

1. Generate your CV: `make build`
2. Commit the generated `index.html`
3. Push to GitHub
4. Enable GitHub Pages in your repository settings
5. Your CV will be available at `https://yourusername.github.io/curriculum-vitae/`

### Custom Domain

Add a `CNAME` file with your domain name and configure your DNS settings to point to GitHub Pages.

## Make Commands

- `make install` - Create virtual environment and install Python dependencies
- `make build` - Generate CV from YAML data
- `make clean` - Remove generated files
- `make clean-all` - Remove generated files and virtual environment
- `make serve` - Build and serve CV locally
- `make help` - Show available commands

## Technologies Used

- **Python**: Build script
- **Jinja2**: HTML templating
- **PyYAML**: YAML parsing
- **CSS3**: Modern styling with variables and flexbox
- **JavaScript**: Interactive features and animations

## License

MIT License - Feel free to use this template for your own CV!
