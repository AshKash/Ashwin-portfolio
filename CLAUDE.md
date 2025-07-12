# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a professional portfolio website for Ashwin Kashyap, an AI & ML consultant, built with Hugo static site generator and hosted on Netlify. The site showcases consulting services, blog posts, testimonials, and includes AI/ML model training capabilities.

## Development Commands

### Hugo Development
```bash
# Start development server with drafts
hugo server -D

# Start development server (production-like)
hugo server

# Build for production
hugo --gc --minify

# Build with specific base URL
hugo --gc --minify --baseURL <url>
```

### Testing
```bash
# Run JavaScript tests
npm test

# Individual test files
npx jest tests/contact-form.test.js
npx jest tests/form-validation.test.js
npx jest tests/success-page.test.js
```

### AI Model Training
```bash
# Set up Python environment for AI scripts
cd scripts/ai
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run model fine-tuning
python models/fine_tune.py

# Test model functionality
python utils/test_ft.py
```

## Architecture Overview

### Hugo Structure
- **Content Organization**: Uses Hugo's content system with separate directories for pages, posts, and testimonials
- **Theme**: Built on the Ananke theme with custom layouts and shortcodes
- **Templates**: Custom layouts in `/layouts/` with partials for reusable components
- **Static Assets**: Images, CSS, and JS in `/static/` directory

### Key Directories
- `content/pages/`: Static pages (about, services, contact)
- `content/posts/`: Blog posts and articles  
- `content/testimonials/`: Client testimonials
- `layouts/`: Custom Hugo templates and partials
- `static/`: Static assets (CSS, images, JS)
- `scripts/ai/`: Python scripts for AI model training and processing
- `tests/`: Jest tests for JavaScript functionality

### AI Integration
- Fine-tuned Phi model training capability
- Document processing and embeddings
- Model artifacts stored in `/models/` and `/static/models/`
- Training data processing in `/data/processed/`

### Deployment
- **Netlify**: Automatic deployment on main branch push
- **Build Command**: `git submodule update --init --recursive && hugo --gc --minify`
- **Hugo Version**: 0.146.0
- **Environment Variables**: HUGO_ENV, HUGO_BASEURL set in netlify.toml

## Configuration Files

### Main Configuration
- `hugo.toml`: Hugo site configuration, menus, parameters
- `netlify.toml`: Netlify build settings and redirects
- `package.json`: Node.js dependencies for testing

### Content Guidelines
- Use YAML frontmatter with title, description, date (for posts), draft status
- Follow kebab-case naming for content files
- Blog posts in `/content/posts/` with proper categorization and tags
- Static pages use custom layouts when specified

### Testing Setup
- Jest configuration in package.json
- Test environment: jsdom
- Setup file: `tests/setup.js`
- Test files follow `*.test.js` pattern

## Development Workflow

### Adding Blog Posts
1. Create new file in `content/posts/`
2. Include proper frontmatter with title, description, date, categories, tags
3. Use markdown format for content
4. Test locally with `hugo server -D`

### Modifying Templates
1. Custom templates go in `layouts/` directory
2. Follow existing partial structure
3. Test changes with development server
4. Ensure responsive design and accessibility

### AI Model Development
1. Work in `scripts/ai/` directory with virtual environment
2. Process training data through data loaders
3. Fine-tune models using provided scripts
4. Test model outputs before deployment

### Form Handling
- Contact forms processed through Netlify Forms
- Success redirects configured in netlify.toml
- Form validation tested with Jest

## Content Strategy
The site focuses on AI/ML consulting services with technical blog content covering:
- RAG systems and query expansion
- LLM optimization and edge deployment
- Web scraping and data extraction
- AI product development
- Machine learning workflows