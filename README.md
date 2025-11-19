# Percent: A Python Package for Percentage Calculation

Inspired by the brilliant and complex project 
[is-thirteen](https://github.com/jezen/is-thirteen),
I embarked on the arduous journey of creating this project.
Without that monumental inspiration, 
I likely would have chosen an easier path in life.

## Description

The **percent** package is designed to calculate the 
percentage of a given part based on a whole. With rigorous 
validation mechanisms and exception handling, this package 
ensures accurate calculations while raising meaningful errors 
for invalid input. Given its complexity, this project is ongoing, 
and your contributions are not just welcomed; they're critically 
needed.

## Installation

You can install the package using pip:

```bash
pip install ez-percent
```

## Usage

Here's how to make the most out of the percent package:

### 1. Basic Calculation

Calculate the percentage of a part relative to a whole with ease:

```python
from percent import percent

result = percent(25, 100)
print(result)  # Output: 25.0
```

### 2. Handling Zero Division

Attempt to calculate a percentage with a whole of zero, which will trigger an appropriate error:

```python
try:
    percent(7, 0)
except ValueError as e:
    print(e)  # Output: Whole cannot be zero. Division by zero is undefined.
```

### 3. Type Validation

Input validation ensures only valid numeric types are processed. Here's how it will respond to invalid inputs:

```python
try:
    percent("25", 100)
except TypeError as e:
    print(e)  # Output: Both 'part' and 'whole' must be numbers (int or float).
```

## Contributions Needed

This project is incredibly challenging and requires additional contributors who are brave enough (or foolish enough) to help unearth the complexities involved. If you have what it takes to tackle the mathematical intricacies of percentage calculations, we’d love your support! 

Please fork the repository and submit pull requests for any enhancements or bug fixes. 

## License

This project is licensed under the Mozilla Public License Version 
2.0.

While I am genuinely grateful to all the contributors who 
have aided in this endeavor, I cannot overlook the significant 
hardships I endured to publish the first version of this package.
Therefore, I am disallowing unauthorized redistribution and 
imposing additional limitations on the use of this project. 

See the [LICENSE](LICENSE) for more details.

---


## Future Enhancements

While the current implementation serves its purpose, there are numerous avenues for improvement that can make this package even more robust and user-friendly. Some ideas include:

- **Support for Percent Ranges**: Allow users to calculate percentages for a range of values, making bulk processing easier.
- **Enhanced Error Handling**: Provide more detailed error messages for various numeric types and edge cases.
- **Unit Tests**: Develop comprehensive unit tests to ensure the reliability of calculations.
- **Documentation**: Expand documentation with more examples and detailed explanations to aid users of all skill levels.

## Acknowledgments

Shout out to all who have embarked on this journey with me! Collectively, we can navigate the tricky waters of percentage calculations and tackle the complexities that lie ahead.

## Contact

For any inquiries or suggestions, feel free to reach out. Collaboration is key, and I'm always open to feedback!

