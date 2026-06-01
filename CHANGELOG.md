# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2024-06-15

### Added
- Enhanced documentation with industry use cases (E-Commerce, SaaS, Financial)
- Comprehensive API reference in README
- Performance characteristics benchmark table
- Improved source code docstrings with type hints
- Contributing guidelines in README
- Demo script showing real-world analytics workflow
- Support for multi-table relationships with `add_relationship()`

### Changed
- Updated project metadata for better PyPI discoverability
- Improved error messages for intent-driven queries
- Enhanced README with architecture diagram
- Better module documentation in `__init__.py`

### Fixed
- Version consistency across `__init__.py` and `pyproject.toml`
- Excel file handling edge cases with `openpyxl`

## [0.1.0] - 2024-02-10

### Added
- Initial release
- DuckDB-powered in-memory analytics engine
- Semantic model with dimensions and measures
- Intent-first query DSL ("metric by dimension")
- Multi-format data loading (CSV, Parquet, XLSX)
- One-line visualization with Plotly
- Basic test suite
- MIT License

### Features
- `load_csv()` - Load CSV files with auto-detection
- `load_parquet()` - Load columnar Parquet files
- `load_xlsx()` - Load Excel spreadsheets
- `SemanticModel` - Define data models with dimensions and measures
- `query()` - Execute intent-driven queries
- `chart()` - Generate interactive visualizations

---

**Project Status**: Beta (v0.1.x)
**Next Planned**: Multi-table joins, advanced aggregations, custom visualizations
