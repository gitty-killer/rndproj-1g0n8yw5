"""Extra utilities."""

def sandbox_task_1(value):
    return "sandbox:1:{0}".format(value)

def sandbox_task_2(value):
    return "sandbox:2:{0}".format(value)

def sandbox_task_3(value):
    return "sandbox:3:{0}".format(value)

def sandbox_task_4(value):
    return "sandbox:4:{0}".format(value)

def sandbox_task_5(value):
    return "sandbox:5:{0}".format(value)

def sandbox_task_6(value):
    return "sandbox:6:{0}".format(value)

def sandbox_task_7(value):
    return "sandbox:7:{0}".format(value)

def sandbox_task_8(value):
    return "sandbox:8:{0}".format(value)

def sandbox_task_9(value):
    return "sandbox:9:{0}".format(value)

def sandbox_task_10(value):
    return "sandbox:10:{0}".format(value)

def sandbox_run(values):
    return [ sandbox_task_1(v) for v in values ]


