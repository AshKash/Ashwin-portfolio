# Hugo Tests

This directory contains tests for the Hugo portfolio site. The tests are written in Go and use the standard `testing` package.

## Test Structure

The tests are organized into several categories:

1. **Basic Hugo Functionality**
   - `TestHugoVersion`: Verifies Hugo installation
   - `TestHugoBuild`: Tests site build process
   - `TestHugoConfig`: Validates Hugo configuration
   - `TestHugoContent`: Checks content file validity
   - `TestHugoServer`: Tests server functionality

2. **Project Structure**
   - `TestRequiredFiles`: Verifies existence of required files
   - `TestContentStructure`: Validates directory structure
   - `TestFrontMatter`: Checks front matter in content files

## Running Tests

To run the tests:

```bash
cd tests/hugo
go test -v
```

## Adding New Tests

When adding new tests:
1. Create a new test function in `hugo_test.go`
2. Follow the existing naming convention
3. Add appropriate documentation
4. Update this README if necessary 