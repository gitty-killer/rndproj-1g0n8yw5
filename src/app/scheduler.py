"""Extra utilities."""

def scheduler_task_1(value):
    return "scheduler:1:{0}".format(value)

def scheduler_task_2(value):
    return "scheduler:2:{0}".format(value)

def scheduler_task_3(value):
    return "scheduler:3:{0}".format(value)

def scheduler_task_4(value):
    return "scheduler:4:{0}".format(value)

def scheduler_task_5(value):
    return "scheduler:5:{0}".format(value)

def scheduler_task_6(value):
    return "scheduler:6:{0}".format(value)

def scheduler_task_7(value):
    return "scheduler:7:{0}".format(value)

def scheduler_task_8(value):
    return "scheduler:8:{0}".format(value)

def scheduler_task_9(value):
    return "scheduler:9:{0}".format(value)

def scheduler_task_10(value):
    return "scheduler:10:{0}".format(value)

def scheduler_run(values):
    return [ scheduler_task_1(v) for v in values ]


