docker run -d --network fd-network --name fd-mongo \
    -e MONGO_INITDB_ROOT_USERNAME="find_diapers" \
    -e MONGO_INITDB_ROOT_PASSWORD="find_diapers"  \
    mongo


docker run -it -d \
    --network fd-network \
    --name fd-mongo-express \
    -p 8081:8081 \
    -e ME_CONFIG_OPTIONS_EDITORTHEME="ambiance" \
    -e ME_CONFIG_MONGODB_SERVER="fd-mongo" \
    -e ME_CONFIG_MONGODB_ADMINUSERNAME="find_diapers" \
    -e ME_CONFIG_MONGODB_ADMINPASSWORD="find_diapers" \
    mongo-express
