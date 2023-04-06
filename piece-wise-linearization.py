# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 07:10:20 2023

@author: sabbas
"""

import numpy as np
import matplotlib.pyplot as plt

def nonlinear_function(x):
    """Nonlinear function to be approximated."""
    return np.sin(x) + np.abs(x)

def piecewise_linearization(x, segments):
    """
    Piecewise linearization of a nonlinear function.

    Parameters:
        x (float): Input value for the nonlinear function.
        segments (list): List of tuples representing the segments.
                         Each tuple contains two values: (x_start, x_end).
                         The function will be linearly approximated within each segment.

    Returns:
        y (float): Piecewise linear approximation of the nonlinear function at x.
    """
    # Sort the segments based on x_start
    segments = sorted(segments, key=lambda segment: segment[0])
    y = 0.0  # Initialize the approximation

    # Loop through each segment
    for i in range(len(segments)):
        x_start, x_end = segments[i]
        # Check if x is within the current segment
        if x >= x_start and x <= x_end:
            # Compute the slope of the linear function within the current segment
            slope = (nonlinear_function(x_end) - nonlinear_function(x_start)) / (x_end - x_start)
            # Compute the y-value of the linear approximation using point-slope form
            y = slope * (x - x_start) + nonlinear_function(x_start)
            break  # No need to check remaining segments, we found the current segment

    return y

# Example usage
segments = [(-5, -3), (-3, 0), (0, 2), (2, 5)]  # Define segments
x = np.linspace(-5, 5, 500)  # Generate x values for plotting
y_nonlinear = nonlinear_function(x)  # Compute y values of the nonlinear function
y_piecewise_linear = np.array([piecewise_linearization(xi, segments) for xi in x])  # Compute piecewise linear approximation

# Plot the nonlinear function and its piecewise linear approximation
plt.figure(figsize=(8, 6))
plt.plot(x, y_nonlinear, label='Nonlinear Function')
plt.plot(x, y_piecewise_linear, label='Piecewise Linear Approximation')
plt.scatter([seg[0] for seg in segments], [nonlinear_function(seg[0]) for seg in segments], color='r', marker='o', label='Segment Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Piecewise Linear Approximation of Nonlinear Function')
plt.legend()
plt.grid(True)
plt.show()
