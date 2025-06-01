# Ashwin Kashyap - AI & ML Consulting Portfolio

A professional portfolio website built with Hugo, showcasing AI and Machine Learning consulting services.

## 🚀 Features

- Modern, responsive design
- Dark/Light mode support
- Search functionality
- Blog section for articles and updates
- Project showcase
- Service descriptions
- Client testimonials

## 🛠️ Tech Stack

- [Hugo](https://gohugo.io/) - Static site generator
- [Netlify](https://www.netlify.com/) - Hosting and deployment

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AshKash/Ashwin-portfolio.git
   cd Ashwin-portfolio
   ```

2. Install Hugo (version 0.123.0 or later):
   ```bash
   brew install hugo  # macOS
   # or
   choco install hugo -confirm  # Windows
   ```

3. Start the development server:
   ```bash
   hugo server -D
   ```

## 🏗️ Project Structure

```
.
├── content/           # Content files
│   ├── pages/        # Static pages
│   ├── posts/        # Blog posts
│   └── services/     # Service descriptions
├── layouts/          # Custom layouts
├── static/           # Static assets
└── tests/           # Test files
```

## 🚀 Deployment

The site is automatically deployed to Netlify when changes are pushed to the main branch.

### Manual Deployment

1. Build the site:
   ```bash
   hugo --gc --minify
   ```

2. The built site will be in the `public/` directory

## 🔧 Configuration

- Site configuration: `hugo.toml`
- Netlify configuration: `netlify.toml`

## 📝 Content Management

- Blog posts: `content/posts/`
- Static pages: `content/pages/`
- Projects: `content/projects/`
- Services: `content/services/`

## 📄 License

All Rights Reserved © 2024 Ashwin Kashyap

## 👨‍💻 Author

**Ashwin Kashyap** - AI & ML Consultant
- Website: [ashwinkashyap.ai](https://ashwinkashyap.ai)
- GitHub: [@AshKash](https://github.com/AshKash) 