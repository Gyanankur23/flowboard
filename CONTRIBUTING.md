# Contributing to Flowboard

Thank you for your interest in contributing to Flowboard! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Be respectful, inclusive, and professional. We're building a welcoming community for data engineers and analysts.

## Getting Started

### Development Setup

```bash
git clone https://github.com/gyanankur23/flowboard.git
cd flowboard
pip install -e .[dev]
```

### Running Tests

```bash
pytest
pytest --cov=src/flowboard  # With coverage
```

### Code Style

- Follow PEP 8
- Use type hints for function arguments and return values
- Write docstrings for all public functions (Google style)
- Keep line length ≤ 88 characters

### Example Docstring

```python
def my_function(param1: str, param2: int) -> Dict[str, Any]:
    """
    Brief description of what the function does.
    
    Longer description explaining the purpose and behavior.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When validation fails
        
    Example:
        >>> result = my_function('test', 42)
    """
    pass
```

## Pull Request Process

1. **Create a branch**: `git checkout -b feature/your-feature-name`
2. **Make changes**: Implement your feature with tests
3. **Write tests**: Ensure new code has test coverage
4. **Run tests**: `pytest` must pass
5. **Update docs**: Update README/docstrings if behavior changes
6. **Create PR**: Include clear description of changes and motivation

## Types of Contributions

### Bug Fixes
- Open an issue describing the bug
- Include minimal reproduction example
- Submit PR with fix and test case

### Features
- Discuss feature idea in an issue first
- Keep scope focused and testable
- Add tests for new functionality
- Update documentation

### Documentation
- Fix typos and unclear explanations
- Add examples and use cases
- Improve docstrings
- Create tutorials or guides

## Areas for Contribution

### High Priority
- Performance optimizations for large datasets
- Better error messages and validation
- Multi-table join support
- Advanced visualization options

### Medium Priority
- Additional data format support (JSON, Avro)
- Query result caching
- Metric templates and library
- Integration with BI tools

### Community
- Write blog posts or tutorials
- Share example notebooks
- Help answer questions
- Provide feedback on design

## Testing Standards

- All public functions must have tests
- Tests should cover happy path and error cases
- Use meaningful test names: `test_<function>_<scenario>`
- Aim for >80% code coverage

```python
def test_query_valid_intent():
    """Test that valid intent formats are parsed correctly."""
    model = SemanticModel()
    model.add_table('test', dimensions=['date'], measures={'revenue': 'SUM(amount)'})
    result = query('revenue by date', model)
    assert isinstance(result, list)

def test_query_invalid_intent_format():
    """Test that invalid intent format raises ValueError."""
    model = SemanticModel()
    with pytest.raises(ValueError):
        query('revenue', model)
```

## Documentation Standards

- Keep README focused on getting started
- Use clear, concise language
- Provide real-world examples
- Include architecture diagrams for complex features

## Commit Messages

Use clear, descriptive commit messages:

```
Add multi-table join support

- Implement JOIN clauses in query engine
- Add test cases for various join types
- Update documentation with examples
- Fixes #42
```

## Questions or Suggestions?

- Open an issue on GitHub
- Email: gyanankur9@gmail.com
- Discussions welcome on any aspect of the project

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for helping make Flowboard better!** 🚀
