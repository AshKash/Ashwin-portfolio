package hugo

import (
	"os"
	"path/filepath"
	"strings"
	"testing"
)

var projectRoot string

func init() {
	// Get the absolute path to the project root
	wd, err := os.Getwd()
	if err != nil {
		panic(err)
	}
	projectRoot = filepath.Dir(filepath.Dir(wd))
}

// TestFormSubmission verifies that the contact form is properly configured
func TestFormSubmission(t *testing.T) {
	// Check if contact form shortcode exists
	formPath := filepath.Join(projectRoot, "layouts", "shortcodes", "contact-form.html")
	if _, err := os.Stat(formPath); os.IsNotExist(err) {
		t.Errorf("Contact form shortcode not found at %s", formPath)
	}

	// Check if success page exists
	successPath := filepath.Join(projectRoot, "content", "contact-post-success.md")
	if _, err := os.Stat(successPath); os.IsNotExist(err) {
		t.Errorf("Contact form success page not found at %s", successPath)
	}

	// Check if Netlify configuration exists
	netlifyPath := filepath.Join(projectRoot, "netlify.toml")
	if _, err := os.Stat(netlifyPath); os.IsNotExist(err) {
		t.Errorf("Netlify configuration not found at %s", netlifyPath)
	}
}

// TestFormFields verifies that the contact form has all required fields and proper structure
func TestFormFields(t *testing.T) {
	formPath := filepath.Join(projectRoot, "layouts", "shortcodes", "contact-form.html")
	content, err := os.ReadFile(formPath)
	if err != nil {
		t.Fatalf("Failed to read contact form: %v", err)
	}

	formContent := string(content)

	// Check for required fields
	requiredFields := []string{
		`name="name"`,
		`name="email"`,
		`name="subject"`,
		`name="message"`,
	}

	for _, field := range requiredFields {
		if !strings.Contains(formContent, field) {
			t.Errorf("Required field %s not found in contact form", field)
		}
	}

	// Check for Netlify form attributes
	netlifyAttrs := []string{
		`data-netlify="true"`,
		`netlify-honeypot="bot-field"`,
		`name="contact"`,
	}

	for _, attr := range netlifyAttrs {
		if !strings.Contains(formContent, attr) {
			t.Errorf("Required Netlify attribute %s not found in contact form", attr)
		}
	}

	// Check for honeypot field
	if !strings.Contains(formContent, `name="bot-field"`) {
		t.Error("Honeypot field not found in contact form")
	}

	// Check for form action
	if !strings.Contains(formContent, `action="/contact-post-success/"`) {
		t.Error("Form action not set to success page")
	}
}

// TestSuccessPage verifies that the success page has the required content
func TestSuccessPage(t *testing.T) {
	successPath := filepath.Join(projectRoot, "content", "contact-post-success.md")
	content, err := os.ReadFile(successPath)
	if err != nil {
		t.Fatalf("Failed to read success page: %v", err)
	}

	successContent := string(content)

	// Check for required frontmatter
	requiredFrontmatter := []string{
		"title:",
		"description:",
		"layout:",
	}

	for _, field := range requiredFrontmatter {
		if !strings.Contains(successContent, field) {
			t.Errorf("Required frontmatter field %s not found in success page", field)
		}
	}

	// Check for required content
	requiredContent := []string{
		"Thank You for Your Message",
		"What's Next",
		"Return to Home Page",
	}

	for _, text := range requiredContent {
		if !strings.Contains(successContent, text) {
			t.Errorf("Required content '%s' not found in success page", text)
		}
	}
} 