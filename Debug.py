import sys

def tracefunc(frame, event, arg):
    if event == "return":
        result = []
        for key in frame.f_locals.keys():
            result.append(key)
        print("function:", frame.f_code.co_name, ", local vars:", result)
    return tracefunc


def foo():
    friends = ["Bob", "Tom"]
    for f in friends:
        print("Hi %s!" % f)
    return len(friends)


sys.settrace(tracefunc)
foo()
