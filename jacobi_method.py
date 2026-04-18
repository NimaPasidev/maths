import numpy as np
import pandas as pd

def jacobi_method(A, b, x0, tol=1e-3, max_iter=100):
    """
    Solves the system Ax = b using the Jacobi iteration method.
    
    Parameters:
    A (list/array): Coefficient matrix
    b (list/array): Constant vector
    x0 (list/array): Initial approximation vector
    tol (float): Tolerance for the stopping criterion
    max_iter (int): Maximum number of iterations
    
    Returns:
    pd.DataFrame: A dataframe containing the values of x at each iteration and the error.
    """
    # Convert inputs to numpy arrays with float type to prevent integer division issues
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    
    n = len(b)
    
    # Extract the diagonal elements (D) and the remainder of the matrix (R = L + U)
    D = np.diag(A)
    R = A - np.diagflat(D)
    
    # Check for zeros on the diagonal to avoid division by zero
    if any(D == 0):
        raise ValueError("Matrix A has zero(s) on its main diagonal. Row interchanges are required.")
    
    # Initialize a list to store iteration data for the DataFrame
    iterations_data = []
    
    # Record the initial approximation (Iteration 0)
    # The initial error is marked as 0.0
    initial_record = list(x) + [0.0]
    iterations_data.append(initial_record)
    
    for k in range(1, max_iter + 1):
        # Jacobi formula in matrix form: x_new = (b - R*x) / D
        x_new = (b - np.dot(R, x)) / D
        
        # Calculate the l_infinity norm of the relative error
        diff_norm = np.max(np.abs(x_new - x))
        x_new_norm = np.max(np.abs(x_new))
        
        # Avoid division by zero if the solution vector is exactly zero
        if x_new_norm == 0:
            error = diff_norm
        else:
            error = diff_norm / x_new_norm
            
        # Store the current iteration's data
        iterations_data.append(list(x_new) + [error])
        
        # Check if the stopping criterion is met
        if error < tol:
            break
            
        # Update x for the next iteration
        x = x_new
        
    # Create the DataFrame
    columns = [f'x_{i+1}' for i in range(n)] + ['Error']
    df = pd.DataFrame(iterations_data, columns=columns)
    
    return df

# ==========================================
# Test Case: Question 2 from the Tutorial
# ==========================================
if __name__ == "__main__":
    # Define the system
    A = [[4, 1, 1],
         [1, 3, 1],
         [2, -1, 4]]
         
    b = [5, 3, 7]
    
    # Initial approximation
    x0 = [1, 1, 1]
    
    # Run the Jacobi method
    # Tolerance is 10^-3 as specified in Q2
    result_df = jacobi_method(A, b, x0, tol=1e-3, max_iter=100)
    
    # Print the resulting DataFrame
    print(result_df.to_string())