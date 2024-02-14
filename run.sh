# change the port number if required
docker run -it --rm --name key_value_server -p 8123:8123 key_value_server:latest uvicorn main:app --host 0.0.0.0 --port 8123
