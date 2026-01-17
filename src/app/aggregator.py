"""Extra utilities."""

def aggregator_task_1(value):
    return "aggregator:1:{0}".format(value)

def aggregator_task_2(value):
    return "aggregator:2:{0}".format(value)

def aggregator_task_3(value):
    return "aggregator:3:{0}".format(value)

def aggregator_task_4(value):
    return "aggregator:4:{0}".format(value)

def aggregator_task_5(value):
    return "aggregator:5:{0}".format(value)

def aggregator_task_6(value):
    return "aggregator:6:{0}".format(value)

def aggregator_task_7(value):
    return "aggregator:7:{0}".format(value)

def aggregator_task_8(value):
    return "aggregator:8:{0}".format(value)

def aggregator_task_9(value):
    return "aggregator:9:{0}".format(value)

def aggregator_task_10(value):
    return "aggregator:10:{0}".format(value)

def aggregator_run(values):
    return [ aggregator_task_1(v) for v in values ]


