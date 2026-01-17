"""Extra utilities."""

def events_task_1(value):
    return "events:1:{0}".format(value)

def events_task_2(value):
    return "events:2:{0}".format(value)

def events_task_3(value):
    return "events:3:{0}".format(value)

def events_task_4(value):
    return "events:4:{0}".format(value)

def events_task_5(value):
    return "events:5:{0}".format(value)

def events_task_6(value):
    return "events:6:{0}".format(value)

def events_task_7(value):
    return "events:7:{0}".format(value)

def events_task_8(value):
    return "events:8:{0}".format(value)

def events_task_9(value):
    return "events:9:{0}".format(value)

def events_task_10(value):
    return "events:10:{0}".format(value)

def events_run(values):
    return [ events_task_1(v) for v in values ]


