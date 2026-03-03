#!/usr/bin/env bash

SERVICE_NAME="bucket"
NETWORK_NAME="eveler_point_dev"
MC_CONFIG_VOL="mc_config_data"

docker volume create $MC_CONFIG_VOL > /dev/null

docker run --rm \
    --network=$NETWORK_NAME \
    -v $MC_CONFIG_VOL:/root/.mc \
    minio/mc \
    alias set myminio http://$SERVICE_NAME:9000 minioadmin minioadmin

docker run --rm \
    --network=$NETWORK_NAME \
    -v $MC_CONFIG_VOL:/root/.mc \
    minio/mc \
    mb myminio/images-brutes

docker run --rm \
    --network=$NETWORK_NAME \
    -v $MC_CONFIG_VOL:/root/.mc \
    minio/mc \
    mb myminio/images-web


