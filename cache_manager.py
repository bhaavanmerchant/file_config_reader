import disk_reader
import heapq

heap = []
ConfigManager = {}

def __init__(self):
    global heap


def create_as_dict(par,key=None,env=None):
    if env != None and key != None and par != None:
        if env not in ConfigManager[par][key]:
            ConfigManager[par][key][env] = {}
    elif par != None and key != None and env == None:
        if key not in ConfigManager[par]:
            ConfigManager[par][key] = {}
    elif par !=None and key == None:
        ConfigManager[par] = {}

def is_present_in_dict(par,key=None,env=None):
    if env != None and key != None and par != None and env in ConfigManager[par][key]:
        return True
    elif par != None and key != None and env == None and key in ConfigManager[par]:
        return True
    elif par !=None and key == None and par in ConfigManager:
        return True
    else:
        return False

def set_val(par,key,env,val):
    ConfigManager[par][key][env] = val
    heap_node = [1, par, key, env, val]
    if len(heap) + 1 < getMemorySize() :
        heapq.heappush(heap, heap_node)
    else:
        evict_from_cache(par,key,env)
        heapq.heappush(heap, heap_node)

def get_val(par,key,env):
    return ConfigManager[par][key][env]

def get_keys(par):
    return ConfigManager[par].keys()

def return_and_update_cache(par,key,env="_default"):
    #env = os.environ("env")
    val = ConfigManager[par][key][env]
    for heap_node in heap:
        if heap_node[1] == par and heap_node[2] == key and heap_node[3] == env :
            heap_node[0] += 1
    heapq.heapify(heap)
    return val


def check_and_put_cache(par,key,env="_default"):
    #env = os.environ("env")
    diskval = check_in_disk(par,key,env)
    if diskval != "NULL":
        ConfigManager[par][key][env] = diskval
        heap_node = [1, par, key, env, diskval]
        if len(heap) + 1 < getMemorySize() :
            heapq.heappush(heap, heap_node)
        else:
            evict_from_cache(par,key,env)
            heapq.heappush(heap, heap_node)
    return diskval

def getMemorySize():
    return 1000

def evict_from_cache(par,key,env):
    ConfigManager[par][key][env] = None
    heap.pop(0)

def check_in_disk(par,key,env="_default"):
    try:
        return disk_reader.fetch_from_disk(par,key,env)
    except Exception as e:
        return "NULL"
