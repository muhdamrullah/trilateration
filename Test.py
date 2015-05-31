def get_task(task_id):
    hexstr = task_id
    hex = ':'.join([hexstr[i:i+2] for i in range(0, len(hexstr), 2)])
    print hex

get_task('AABBCCDDEEFF')
