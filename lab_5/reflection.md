# Reflection

The supplied handout lists reflection as a deliverable but does not include the four reflection prompts. These responses address four central questions from the lab objectives.

## 1. What is the purpose of static code analysis?

Static analysis checks source code without running it. It catches likely bugs, unsafe patterns, and style problems early, when they are cheaper to fix. It complements execution-based checks because it can identify risks on code paths the demo does not exercise.

## 2. What did Pylint, Bandit, and Flake8 each contribute?

Pylint highlighted code quality issues such as the shared mutable default, broad exception handling, missing documentation, and nonstandard naming. Bandit focused on security risks, including shell execution, insecure temporary-file naming, and an unsuitable random number generator for an OTP. Flake8 caught whitespace and layout violations. Their checks overlap in places, but each tool emphasizes different concerns.

## 3. Which finding mattered most, and how was it addressed?

The `shell=True` ping helper was the highest severity finding because untrusted input could become part of a shell command. The helper was unused by the program, so it and its subprocess dependency were removed. The unused insecure temporary-file helper was removed as well. The booking function now creates a fresh history list per call, unknown IDs are handled directly, and OTPs use Python's `secrets` module.

## 4. How will static analysis be used in future work?

I would run these checks before committing and in continuous integration. The reports should be reviewed rather than blindly followed: a tool identifies a possible issue, and the developer still needs to understand the code and choose a fix that preserves behavior. Static analysis is one part of quality assurance, alongside code review and tests.
