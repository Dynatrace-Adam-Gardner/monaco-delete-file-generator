# monaco-delete-file-generator

Utility to create a delete.yaml file for you, given a correct monaco folder structure.

Run the following docker command from within the monaco root directory. A `delete.yaml` file will be generated for you:

**Windows**
```
docker run --rm ^
-v="%CD%:/app" ^
adamgardnerdt/monaco-generate-delete-file:v0.1
```

**Linux**
```
docker run --rm \
-v="$(PWD):/app"
adamgardnerdt/monaco-generate-delete-file:v0.1
```
