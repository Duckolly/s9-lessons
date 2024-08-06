create schema if not exists cdm;

-- yc vpc network create --name my-yc-network  --labels my-label=my-value --description "my first network via yc"
-- yc vpc subnet create --name my-yc-subnet-a --zone ru-central1-a --range 10.1.2.0/24 --network-name my-yc-network --description "my first subnet via yc"
-- yc compute instance create --name my-yc-instance --network-interface subnet-name=my-yc-subnet-a,nat-ip-version=ipv4 --zone ru-central1-a --ssh-key ~/.ssh/id_ed25519.pub

