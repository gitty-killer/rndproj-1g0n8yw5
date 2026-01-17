"""Extra utilities."""

def throttle_task_1(value):
    return "throttle:1:{0}".format(value)

def throttle_task_2(value):
    return "throttle:2:{0}".format(value)

def throttle_task_3(value):
    return "throttle:3:{0}".format(value)

def throttle_task_4(value):
    return "throttle:4:{0}".format(value)

def throttle_task_5(value):
    return "throttle:5:{0}".format(value)

def throttle_task_6(value):
    return "throttle:6:{0}".format(value)

def throttle_task_7(value):
    return "throttle:7:{0}".format(value)

def throttle_task_8(value):
    return "throttle:8:{0}".format(value)

def throttle_task_9(value):
    return "throttle:9:{0}".format(value)

def throttle_task_10(value):
    return "throttle:10:{0}".format(value)

def throttle_run(values):
    return [ throttle_task_1(v) for v in values ]


