# Function to calculate discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user for input
try:
    price = float(input("Input original price: "))
    discount_percent = float(input("Input discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(price, discount_percent)
    print(f"Your final price is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")
