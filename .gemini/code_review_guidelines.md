# Code Review Guidelines

## Priority Focus Areas

### 🔴 Critical (Must Address)
- **Security vulnerabilities**: SQL injection, XSS, authentication bypass
- **Data integrity issues**: Race conditions, data loss scenarios
- **Breaking changes**: API compatibility, database migrations
- **Performance bottlenecks**: N+1 queries, inefficient algorithms

### 🟡 Important (Should Address)
- **Error handling**: Missing try-catch, unhandled edge cases
- **Testing**: Missing test coverage for new logic
- **Code duplication**: DRY violations across files
- **Complex logic**: Methods >50 lines, deeply nested conditionals

### 🟢 Nice-to-Have (Suggestions)
- **Naming improvements**: Unclear variable/function names
- **Code organization**: Extract reusable utilities or service, better file structure
- **Documentation**: Missing comments for complex logic
- **Performance optimizations**: Potential caching, batching, multithreading

## Review Structure

For each file reviewed, provide:
1. **Summary**: Brief overview of changes
2. **Issues**: Specific problems with line references. Mark severity: 🔴 Critical, 🟡 Important, 🟢 Nice-to-Have
3. **Positives**: What was well-done (build confidence)
4. **Refactoring**: Structural improvements with examples if needed
5. **Recommendations**: Actionable next steps

## Team Conventions

### Commit Messages
- Follow format: [branch-name] Brief description
- Use imperative mood

### Testing Requirements
- Unit tests for all business logic
- Integration tests for API endpoints
- Minimum 80% code coverage

### Documentation
- README.md updated for new features
- Architecture.md updated with new decisions documented

## Continuous Improvement

This document is living and should evolve based on:
- Feedback from code reviews
- Recurring issues found in production
- New technologies and best practices adopted by the team

**Last Updated**: [Date]
**Recent Improvements**: [Track changes here]