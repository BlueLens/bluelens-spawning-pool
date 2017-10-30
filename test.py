from __future__ import print_function
from bluelens_spawning_pool import spawning_pool

pool = spawning_pool.SpawningPool()

project_name = 'bl-cropper'

pool.setServerUrl('35.187.244.252')
pool.setApiVersion('v1')
pool.setKind('pod')
pool.setMetadataName(project_name)
pool.setMetadataNamespace('index')
pool.addMetadataLabel('name', project_name)
container = pool.createContainer()
pool.setContainerName(container, project_name)
pool.addContainerEnv(container, 'key1', 'xxxxx')
pool.addContainerEnv(container, 'key2', 'yyyyy')
pool.setContainerImage(container, 'bluelens/bl-cropper:latest')
pool.addContainer(container)
pool.setRestartPolicy('Never')
pool.spawn()