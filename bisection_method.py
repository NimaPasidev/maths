import math

def get_sign(value):
    """Returns '+' or '-' based on the value."""
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

def bisection_table():
    print("=== Bisection Method Table Generator ===")
    
    # 1. Get user inputs
    func_str = input("Enter the equation f(x) (e.g., x**3 - x - 2 or math.cos(x) - x): ")
    a = float(input("Enter the left endpoint (a): "))
    b = float(input("Enter the right endpoint (b): "))
    max_iter = int(input("Enter the number of iterations: "))

    # Safely evaluate the mathematical function
    def f(x):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names['x'] = x
        return eval(func_str, {"__builtins__": None}, allowed_names)

    # Check if the initial interval is valid
    if f(a) * f(b) >= 0:
        print("\nError: f(a) and f(b) must have opposite signs. The interval may not contain a root.")
        return

    # 2. Print Table Header
    print("\n" + "=" * 85)
    print(f"{'i':^5} | {'a':^8} | {'f(a)':^4} | {'b':^8} | {'f(b)':^4} | {'p':^8} | {'f(p)':^9} | {'Rel. Error':^10}")
    print("-" * 85)

    p_prev = 0

    # 3. Iterate and calculate
    for i in range(1, max_iter + 1):
        # Calculate midpoint p
        p = (a + b) / 2
        
        # Calculate function values
        fa = f(a)
        fb = f(b)
        fp = f(p)
        
        # Calculate relative error
        if i == 1:
            rel_error_str = "---"
        else:
            rel_error = abs((p_prev - p) / p)
            rel_error_str = f"{rel_error:.4f}"

        # Print the current row
        print(f"{i:^5} | {a:<8.4g} | {get_sign(fa):^4} | {b:<8.4g} | {get_sign(fb):^4} | {p:<8.4g} | {fp:>8.4f} | {rel_error_str:^10}")

        # 4. Update bounds for the next iteration
        if fa * fp < 0:
            b = p
        elif fb * fp < 0:
            a = p
        else:
            print("\nExact root found!")
            break
            
        p_prev = p
        
    print("=" * 85)

# Run the program
if __name__ == "__main__":
    bisection_table()


#pasindu nimsara