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
    mb myminio/eveler-point-dev

# Création bucket public
docker run --rm \
    --network=$NETWORK_NAME \
    -v $MC_CONFIG_VOL:/root/.mc \
    minio/mc \
    mb myminio/eveler-point-dev-public

docker run --rm \
    --network=$NETWORK_NAME \
    -v $MC_CONFIG_VOL:/root/.mc \
    minio/mc \
    anonymous set download myminio/eveler-point-dev-public

# Création utilisateur
docker run --rm \
    -v mc_config_data:/root/.mc \
    --network=eveler_point_dev \
    minio/mc admin user add myminio eveler_user eveler_password123
