import time


def time_count(function_to_decorate):
    def the_wrapper_around_the_original_function(arg):
        print(arg)
        start = time.time()
        func_result = function_to_decorate(arg)
        end = time.time()
        period = end - start
        print(period)
        return {"func_result": func_result, "period": period}

    return the_wrapper_around_the_original_function
