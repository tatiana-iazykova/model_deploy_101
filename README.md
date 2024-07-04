# model_deploy_101
How to deploy your AI models

step one
```bash
docker build . -t test 
```

step two
```bash
docker run --rm -d -p 8000:8000 test
```

watch logs
```bash
docker logs -f <image_name>
```