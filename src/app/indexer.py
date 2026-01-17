"""Extra utilities."""

def indexer_task_1(value):
    return "indexer:1:{0}".format(value)

def indexer_task_2(value):
    return "indexer:2:{0}".format(value)

def indexer_task_3(value):
    return "indexer:3:{0}".format(value)

def indexer_task_4(value):
    return "indexer:4:{0}".format(value)

def indexer_task_5(value):
    return "indexer:5:{0}".format(value)

def indexer_task_6(value):
    return "indexer:6:{0}".format(value)

def indexer_task_7(value):
    return "indexer:7:{0}".format(value)

def indexer_task_8(value):
    return "indexer:8:{0}".format(value)

def indexer_task_9(value):
    return "indexer:9:{0}".format(value)

def indexer_task_10(value):
    return "indexer:10:{0}".format(value)

def indexer_run(values):
    return [ indexer_task_1(v) for v in values ]


