// Form Validation Tests
describe('Form Validation', () => {
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

  test('required fields cannot be empty', () => {
    const form = document.querySelector('form');
    const nameInput = document.querySelector('#name');
    const emailInput = document.querySelector('#email');
    const subjectInput = document.querySelector('#subject');
    const messageInput = document.querySelector('#message');

    // Test empty form submission
    expect(form.checkValidity()).toBe(false);

    // Fill in required fields
    nameInput.value = 'John Doe';
    emailInput.value = 'john@example.com';
    subjectInput.value = 'Test Subject';
    messageInput.value = 'Test Message';

    // Test form with all required fields filled
    expect(form.checkValidity()).toBe(true);
  });

  test('email field validates email format', () => {
    const emailInput = document.querySelector('#email');
    
    // Test invalid email
    emailInput.value = 'invalid-email';
    expect(emailInput.checkValidity()).toBe(false);

    // Test valid email
    emailInput.value = 'valid@example.com';
    expect(emailInput.checkValidity()).toBe(true);
  });
}); 