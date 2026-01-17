"""Extra utilities."""

def cache_task_1(value):
    return "cache:1:{0}".format(value)

def cache_task_2(value):
    return "cache:2:{0}".format(value)

def cache_task_3(value):
    return "cache:3:{0}".format(value)

def cache_task_4(value):
    return "cache:4:{0}".format(value)

def cache_task_5(value):
    return "cache:5:{0}".format(value)

def cache_task_6(value):
    return "cache:6:{0}".format(value)

def cache_task_7(value):
    return "cache:7:{0}".format(value)

def cache_task_8(value):
    return "cache:8:{0}".format(value)

def cache_task_9(value):
    return "cache:9:{0}".format(value)

def cache_task_10(value):
    return "cache:10:{0}".format(value)

def cache_run(values):
    return [ cache_task_1(v) for v in values ]


