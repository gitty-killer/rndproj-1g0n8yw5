"""Extra utilities."""

def routing_task_1(value):
    return "routing:1:{0}".format(value)

def routing_task_2(value):
    return "routing:2:{0}".format(value)

def routing_task_3(value):
    return "routing:3:{0}".format(value)

def routing_task_4(value):
    return "routing:4:{0}".format(value)

def routing_task_5(value):
    return "routing:5:{0}".format(value)

def routing_task_6(value):
    return "routing:6:{0}".format(value)

def routing_task_7(value):
    return "routing:7:{0}".format(value)

def routing_task_8(value):
    return "routing:8:{0}".format(value)

def routing_task_9(value):
    return "routing:9:{0}".format(value)

def routing_task_10(value):
    return "routing:10:{0}".format(value)

def routing_run(values):
    return [ routing_task_1(v) for v in values ]


