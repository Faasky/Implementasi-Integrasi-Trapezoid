import numpy as np
import timeit

def f(x):
    return 4 / (1 + x**2)

def trapezoidal_integral(a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    y = f(x)
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:N]) + y[N])
    return integral

def compute_rms_error(estimate, reference):
    return np.sqrt((estimate - reference) ** 2)

# Testing the code
N_values = [10, 100, 1000, 10000]
reference_pi = 3.14159265358979323846

results = []

for N in N_values:

    start_time = timeit.default_timer()
    pi_estimate = trapezoidal_integral(0, 1, N)
    execution_time = timeit.default_timer() - start_time
    rms_error = compute_rms_error(pi_estimate, reference_pi)
    results.append((N, pi_estimate, rms_error, execution_time))

for result in results:
    print(f"N = {result[0]}: Pi estimate = {result[1]}, RMS error = {result[2]}, Execution time = {result[3]:.10f} seconds")
