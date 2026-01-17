"""Extra utilities."""

def policy_task_1(value):
    return "policy:1:{0}".format(value)

def policy_task_2(value):
    return "policy:2:{0}".format(value)

def policy_task_3(value):
    return "policy:3:{0}".format(value)

def policy_task_4(value):
    return "policy:4:{0}".format(value)

def policy_task_5(value):
    return "policy:5:{0}".format(value)

def policy_task_6(value):
    return "policy:6:{0}".format(value)

def policy_task_7(value):
    return "policy:7:{0}".format(value)

def policy_task_8(value):
    return "policy:8:{0}".format(value)

def policy_task_9(value):
    return "policy:9:{0}".format(value)

def policy_task_10(value):
    return "policy:10:{0}".format(value)

def policy_run(values):
    return [ policy_task_1(v) for v in values ]


