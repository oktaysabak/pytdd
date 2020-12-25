# Notes

- Traditional unit testing and developer testing are all about writing tests to verify that the code works as it is supposed to.

- **TDD** does not focus about testing. The simple act of writing a test before the implementation changes the way we think when we implement the corresponding functionality.

- The tests tha are written in TDD are those that drive the development forward, and not necessarily those that cover all imaginable scenarios.

- for running tests use this command:
```bash
python -m unittest
(or)
python -m unittest discover
```

- `assertAlmostEqual` method is often used when checking equality with floating numbers. The reason is that due to the way floating points are stored, the result may not be exactly the number you expect.