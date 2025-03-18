# Development Guidelines

We welcome contributions! Here's how you can help:

*   **Report Bugs:**  Submit detailed bug reports using GitHub issues.
*   **Suggest Features:** Propose new features or improvements.
*   **Submit Pull Requests:** Contribute code fixes or new features.

**Contribution Workflow:**

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix: `git checkout -b feature/my-new-feature`
3.  Write clear, concise code with comments.
4.  Follow the project's coding style (see below).
5.  Write unit tests for your changes.
6.  Run tests: `make test`
7.  Submit a pull request with a detailed description of your changes.

**Coding Style:**

*   Follow the PEP 8 style guide.
*   Use descriptive variable names.
*   Write clear and concise comments.
*   Use type hints.
*   Format code with Black: `make format`

**Testing:**

*   Write unit tests using the `unittest` framework.
*   Place tests in the `tests/` directory.
*   Run tests using the `make test` command.

