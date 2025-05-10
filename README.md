# Ashwin Kashyap - AI & ML Consulting Portfolio

A professional portfolio website built with Hugo and the PaperMod theme, showcasing AI and Machine Learning consulting services.

## 🚀 Features

- Modern, responsive design with PaperMod theme
- Dark/Light mode support
- Search functionality
- Blog section for articles and updates
- Project showcase
- Service descriptions
- Client testimonials

## 🛠️ Tech Stack

- [Hugo](https://gohugo.io/) - Static site generator
- [PaperMod Theme](https://github.com/adityatelange/hugo-PaperMod) - Clean and modern theme
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
└── themes/           # Theme files
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
- Theme customization: `themes/PaperMod/`

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

# Golf Course Booking CLI

A powerful command-line interface tool that helps golfers find and book tee times at nearby courses. This tool automates the process of searching for golf courses, checking availability, and making reservations, saving golfers time and effort.

## 🎯 Core Features

### Location-Based Course Discovery
- Automatically detect user's location or accept manual input
- Find golf courses within a specified radius
- Sort and filter courses by distance, rating, and price
- Display course details including:
  - Course layout and difficulty
  - Amenities and facilities
  - Current weather conditions
  - Recent reviews and ratings

### Smart Tee Time Search
- Real-time availability checking
- Flexible date and time range selection
- Group size optimization
- Price comparison across different times
- Special rates and promotions detection

### Intelligent Booking System
- Automated form filling and submission
- Multi-step booking flow handling
- Payment processing integration
- Booking confirmation and receipt generation
- Calendar integration for tee time reminders

### Advanced Web Scraping
- Dynamic website parsing and navigation
- JavaScript-rendered content handling
- Anti-bot detection bypass
- Rate limiting and polite crawling
- Error handling and retry mechanisms

## 🛠️ Technical Architecture

### Core Components
- **Location Service**: Handles geolocation and distance calculations
- **Course Database**: Maintains local cache of course information
- **Web Scraper**: Intelligent parsing of various golf course websites
- **Booking Engine**: Handles the reservation process
- **User Interface**: Interactive CLI with progress indicators

### Smart Parsing System
- Pattern recognition for different website layouts
- Dynamic form field detection
- Booking flow analysis
- Error state handling
- Success confirmation verification

### Data Collection
- Course information (name, address, contact)
- Tee time availability
- Pricing and special rates
- Booking requirements
- User preferences and history

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Internet connection
- Valid payment method for bookings

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/golf-booking-cli.git
cd golf-booking-cli

# Install dependencies
pip install -r requirements.txt

# Configure your settings
cp config.example.yaml config.yaml
# Edit config.yaml with your preferences
```

### Basic Usage
```bash
# Find nearby courses
golf-cli find --radius 10

# Check tee time availability
golf-cli check --course "Pine Valley" --date 2024-04-01

# Book a tee time
golf-cli book --course "Pine Valley" --time 09:00 --players 4
```

## 🔧 Configuration

### Location Settings
- Default search radius
- Preferred course types
- Price range preferences
- Group size defaults

### Booking Preferences
- Default number of players
- Preferred tee time ranges
- Payment method settings
- Notification preferences

### Scraping Configuration
- Rate limiting settings
- Retry attempts
- Timeout values
- User agent rotation

## 🤖 Smart Features

### Intelligent Parsing
- Automatically detects booking forms
- Identifies required fields
- Handles different website layouts
- Manages multi-step booking processes

### Booking Flow Analysis
- Maps out booking process steps
- Identifies required information
- Handles dynamic form fields
- Manages session state

### Error Recovery
- Automatic retry on failures
- Alternative booking paths
- Fallback options
- Error reporting and logging

## 🔒 Security & Privacy

- Secure credential storage
- Encrypted payment information
- Privacy-focused data handling
- No personal data sharing

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📞 Support

For support, please:
1. Check the [documentation](docs/)
2. Search [existing issues](https://github.com/yourusername/golf-booking-cli/issues)
3. Create a new issue if needed

## 🎯 Roadmap

- [ ] Course review integration
- [ ] Weather-based recommendations
- [ ] Group booking optimization
- [ ] Mobile app companion
- [ ] API for third-party integration 