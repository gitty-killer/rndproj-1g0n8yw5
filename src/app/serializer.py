"""Extra utilities."""

def serializer_task_1(value):
    return "serializer:1:{0}".format(value)

def serializer_task_2(value):
    return "serializer:2:{0}".format(value)

def serializer_task_3(value):
    return "serializer:3:{0}".format(value)

def serializer_task_4(value):
    return "serializer:4:{0}".format(value)

def serializer_task_5(value):
    return "serializer:5:{0}".format(value)

def serializer_task_6(value):
    return "serializer:6:{0}".format(value)

def serializer_task_7(value):
    return "serializer:7:{0}".format(value)

def serializer_task_8(value):
    return "serializer:8:{0}".format(value)

def serializer_task_9(value):
    return "serializer:9:{0}".format(value)

def serializer_task_10(value):
    return "serializer:10:{0}".format(value)

def serializer_run(values):
    return [ serializer_task_1(v) for v in values ]


