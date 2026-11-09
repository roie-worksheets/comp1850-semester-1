
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name:
"""

def currency_converter(amount, from_currency, to_currency):
    """
    Converts an amount from "from_currency" to "to_currency", where
    each is a 3 character string within ["GBP, "CNY", "PHP", "INR"]
    """
    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # your code here
    return amount * conversion_rate[from_currency][to_currency] if amount > 0 else 0;

# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
