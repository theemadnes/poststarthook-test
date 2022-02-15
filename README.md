# poststarthook-test
Testing out running a background process in a K8s pod within the same container as the app process

#### notes

https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/

`Hook handler calls are synchronous within the context of the Pod containing the Container. This means that for a PostStart hook, the Container ENTRYPOINT and hook fire asynchronously. However, if the hook takes too long to run or hangs, the Container cannot reach a running state.`

`If either a PostStart or PreStop hook fails, it kills the Container.`

`The logs for a Hook handler are not exposed in Pod events. If a handler fails for some reason, it broadcasts an event. For PostStart, this is the FailedPostStartHook event, and for PreStop, this is the FailedPreStopHook event.`


#### build container image

gcloud artifacts repositories create quickstart-docker-repo --repository-format=docker \
--location=us-central1 --description="Docker repository"
gcloud auth configure-docker us-central1-docker.pkg.dev

(src)& docker build -t us-central1-docker.pkg.dev/mci-asm-mcp/quickstart-docker-repo/quickstart-image:run5-v1 .
(src)& docker push us-central1-docker.pkg.dev/mci-asm-mcp/quickstart-docker-repo/quickstart-image:run5-v1

kubectl exec --stdin --tty flask-hello-world-594d77c779-5gjx2 -- /bin/sh

docker build -t us-central1-docker.pkg.dev/mci-asm-mcp/quickstart-docker-repo/quickstart-image:run5-v1-fat .
docker push us-central1-docker.pkg.dev/mci-asm-mcp/quickstart-docker-repo/quickstart-image:run5-v1-fat

docker build -t us-central1-docker.pkg.dev/mci-asm-mcp/quickstart-docker-repo/quickstart-image:run5-v1-alpine .
docker push us-central1-docker.pkg.dev/mci-asm-mcp/quickstart-docker-repo/quickstart-image:run5-v1-alpine

docker build -t us-central1-docker.pkg.dev/mci-asm-mcp/quickstart-docker-repo/quickstart-image:run5-v1-fat-forever .
docker push us-central1-docker.pkg.dev/mci-asm-mcp/quickstart-docker-repo/quickstart-image:run5-v1-fat-forever