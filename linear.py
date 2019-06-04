# -*- coding: utf-8 -*-
"""
"""
import math

def y_estimate(m,x,b):
    return m*x + b

def slope(x_values, y_values):
    new_list = sorted_points(x_values, y_values)
    new_x = new_list[-1][0] - new_list[0][0]
    new_y = new_list[-1][1] - new_list[0][1]
    return new_y / new_x

def sorted_points(x_values, y_values):
    values = list(zip(x_values, y_values))
    sorted_values = sorted(values, key=lambda value: value[0])
    return sorted_values

def y_intercept(x_values, y_values, m = None):    
    m = slope(x_values, y_values)
    mx = x_values[-1] * m
    return y_values[-1] - mx    

def y_inter(x_values, y_values, m = None):
    sorted_values = sorted_points(x_values, y_values)
    highest = sorted_values[-1]
    if m == None:
        m = slope(x_values, y_values)
    offset = highest[1] - m*highest[0]
    return offset

def build_line(x_values, y_values):
    m = slope(x_values, y_values)
    b = y_intercept(x_values, y_values, m)
    return {'m':m, 'b':b}

def y_actual(x, x_values, y_values):
    combined_values = list(zip(x_values, y_values))
    point_at_x = list(filter(lambda point: point[0] == x,combined_values))[0]
    return point_at_x[1]

def error(x_values, y_values, m, b, x):
    y_est = (m*x)+b
    y_act = y_actual(x, x_values, y_values)
    return y_act - y_est

def error_line_trace(x_values, y_values, m, b, x):
    new_dict = {}
    new_dict['marker'] = {'color':'red'}
    new_dict['mode'] = 'lines'
    new_dict['name'] = "error at " + str(x)
    new_dict['x'] = [x, x]
    new_dict['y'] = [y_actual(x, x_values, y_values), y_estimate(m,x,b)]
    return new_dict

def error_line_traces(x_values, y_values, m, b):
    new_list = []
    for x in x_values:
        new_list.append(error_line_trace(x_values, y_values, m, b, x))
    return new_list

def squared_error(x_values, y_values, m, b, x):
    return error(x_values, y_values, m, b, x) ** 2

def squared_errors(x_values, y_values, m, b):
    return list(map(lambda x: squared_error(x_values, y_values, m, b, x), x_values))

def residual_sum_squares(x_values, y_values, m, b):
    return sum(squared_errors(x_values, y_values, m, b))

def root_mean_squared_error(x_values, y_values, m, b):
    return (math.sqrt(residual_sum_squares(x_values, y_values, m, b)))/len(x_values)

def root_mean_squared_errors(x_values, y_values, regression_lines):
    errors = []
    for regression_line in regression_lines:
        error = root_mean_squared_error(x_values, y_values, regression_line[0], regression_line[1])
        errors.append([regression_line[0], regression_line[1], round(error, 0)])
    return errors


    