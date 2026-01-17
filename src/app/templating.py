"""Extra utilities."""

def templating_task_1(value):
    return "templating:1:{0}".format(value)

def templating_task_2(value):
    return "templating:2:{0}".format(value)

def templating_task_3(value):
    return "templating:3:{0}".format(value)

def templating_task_4(value):
    return "templating:4:{0}".format(value)

def templating_task_5(value):
    return "templating:5:{0}".format(value)

def templating_task_6(value):
    return "templating:6:{0}".format(value)

def templating_task_7(value):
    return "templating:7:{0}".format(value)

def templating_task_8(value):
    return "templating:8:{0}".format(value)

def templating_task_9(value):
    return "templating:9:{0}".format(value)

def templating_task_10(value):
    return "templating:10:{0}".format(value)

def templating_run(values):
    return [ templating_task_1(v) for v in values ]


