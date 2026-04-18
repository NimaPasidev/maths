import numpy as np
import pandas as pd

def gauss_seidel_method(A, b, x0, tol=1e-3, max_iter=100):
    """
    Solves the system Ax = b using the Gauss-Seidel iteration method.
    
    Parameters:
    A (list/array): Coefficient matrix
    b (list/array): Constant vector
    x0 (list/array): Initial approximation vector
    tol (float): Tolerance for the stopping criterion
    max_iter (int): Maximum number of iterations
    
    Returns:
    pd.DataFrame: A dataframe containing the values of x at each iteration and the error.
    """
    # Convert inputs to numpy arrays with float type
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    
    n = len(b)
    
    # Check for zeros on the main diagonal
    D = np.diag(A)
    if any(D == 0):
        raise ValueError("Matrix A has zero(s) on its main diagonal. Row interchanges are required.")
    
    # Initialize list for the DataFrame
    iterations_data = []
    
    # Record the initial approximation (Iteration 0)
    iterations_data.append(list(x) + [0.0])
    
    for k in range(1, max_iter + 1):
        # Create a copy to hold the new values for this iteration
        x_new = np.copy(x)
        
        for i in range(n):
            # Sum of the components already updated in the current iteration (j < i)
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            
            # Sum of the components from the previous iteration (j > i)
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            
            # Calculate the new value for x_i
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
            
        # Calculate the l_infinity norm of the relative error
        diff_norm = np.max(np.abs(x_new - x))
        x_new_norm = np.max(np.abs(x_new))
        
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
        x = np.copy(x_new)
        
    # Create the DataFrame
    columns = [f'x_{i+1}' for i in range(n)] + ['Error']
    df = pd.DataFrame(iterations_data, columns=columns)
    
    return df

# ==========================================
# Test Case: Question 3 from the Tutorial
# ==========================================
if __name__ == "__main__":
    # Define the rearranged, diagonally dominant coefficient matrix A
    A = [[3,1,-1],
         [1,4,-1],
         [1,1,5]]
         
    # Define the constant vector b
    b = [4,4,7]
    
    # Initial approximation
    x0 = [0, 0, 0]
    
    # Run the Gauss-Seidel method
    result_df = gauss_seidel_method(A, b, x0, tol=1e-4, max_iter=100)
    
    # Print the resulting DataFrame
    print(result_df.to_string())