def validate_parameter_with_type(parameter, parameter_type):
    if not isinstance(parameter, parameter_type):
        raise TypeError(f"Parameter {parameter} must be a {parameter_type}")

    return parameter
