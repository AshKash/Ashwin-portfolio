// Test setup file
require('@testing-library/jest-dom');

// Mock window.location
Object.defineProperty(window, 'location', {
  value: {
    href: '',
    pathname: '',
    search: '',
    hash: '',
    assign: jest.fn(),
    replace: jest.fn(),
    reload: jest.fn()
  },
  writable: true
});

// Mock fetch
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve({}),
    text: () => Promise.resolve('')
  })
); 