
# pubsub keys
ERU_TASK_PUBKEY = 'eru:task:pub:%s'
ERU_TASK_LOGKEY = 'eru:task:log:%s'
ERU_TASK_RESULTKEY = 'eru:task:result:%s'

ERU_AGENT_CONTAINERSKEY = 'eru:agent:%s:containers'
ERU_AGENT_WATCHERKEY = 'eru:agent:%s:watcher'

PUB_END_MESSAGE = 'ERU_END_PUB'

# HTTP code
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_NOT_FOUND = 404
HTTP_BAD_REQUEST = 400
HTTP_CONFLICT = 409

OK = 'ok'

# task
TASK_CREATE = 1
TASK_BUILD = 2
TASK_REMOVE = 3

TASK_SUCCESS = 1
TASK_FAILED = 2

TASK_ACTIONS = {
    TASK_CREATE: 'create',
    TASK_BUILD: 'build',
    TASK_REMOVE: 'remove',
}

TASK_RESULT_SUCCESS = 'SUCCESS'
TASK_RESULT_FAILED = 'FAILED'

# raw version
RAW_VERSION_PLACEHOLDER = 'this_is_just_a_default_version'
