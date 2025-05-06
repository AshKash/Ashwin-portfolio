// Contact Form Tests
describe('Contact Form', () => {
  beforeEach(() => {
    document.body.innerHTML = `
      <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/contact-post-success/" class="contact-form">
        <input type="hidden" name="form-name" value="contact" />
        <div hidden>
          <input name="bot-field" />
        </div>
        <div class="form-group">
          <label for="name">Full Name</label>
          <input type="text" name="name" id="name" required>
        </div>
        <div class="form-group">
          <label for="email">Email Address</label>
          <input type="email" name="email" id="email" required>
        </div>
        <div class="form-group">
          <label for="subject">Subject</label>
          <input type="text" name="subject" id="subject" required>
        </div>
        <div class="form-group">
          <label for="message">Message</label>
          <textarea name="message" id="message" rows="5" required></textarea>
        </div>
        <div class="form-group">
          <button type="submit" class="submit-button">Send Message</button>
        </div>
      </form>
    `;
  });

  test('form has required fields', () => {
    const form = document.querySelector('form');
    expect(form).toBeTruthy();
    expect(form.getAttribute('action')).toBe('/contact-post-success/');
    expect(form.getAttribute('data-netlify')).toBe('true');
  });

  test('required fields are marked with asterisk', () => {
    const requiredLabels = document.querySelectorAll('label[for="name"], label[for="email"], label[for="subject"], label[for="message"]');
    requiredLabels.forEach(label => {
      expect(label.textContent).toContain('*');
    });
  });

  test('form has correct input types', () => {
    expect(document.querySelector('#name').type).toBe('text');
    expect(document.querySelector('#email').type).toBe('email');
    expect(document.querySelector('#subject').type).toBe('text');
    expect(document.querySelector('#message').tagName).toBe('TEXTAREA');
  });
}); 