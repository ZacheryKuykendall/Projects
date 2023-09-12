#!/bin/bash

# File name
DOCKERFILE="Dockerfile"

# Ask if the user wants to overwrite an existing Dockerfile
if [ -f "$DOCKERFILE" ]; then
    read -p "$DOCKERFILE already exists. Overwrite? (y/n) " overwrite
    if [[ $overwrite != "y" ]]; then
        echo "Exiting without overwriting."
        exit 1
    fi
fi

# Create or overwrite Dockerfile
touch $DOCKERFILE
echo "# Generated Dockerfile" > $DOCKERFILE

# Base image
read -p "Enter the base image (e.g., ubuntu:latest): " base_image
echo "FROM $base_image" >> $DOCKERFILE
echo "" >> $DOCKERFILE

# Labels (metadata)
while true; do
    read -p "Do you want to add a label? (y/n) " add_label
    if [[ $add_label != "y" ]]; then
        break
    fi
    read -p "Enter label key (e.g., version): " label_key
    read -p "Enter label value: " label_value
    echo "LABEL $label_key=\"$label_value\"" >> $DOCKERFILE
done
echo "" >> $DOCKERFILE

# RUN commands
while true; do
    read -p "Do you want to add a RUN command? (y/n) " add_run
    if [[ $add_run != "y" ]]; then
        break
    fi
    read -p "Enter the RUN command (e.g., apt-get update): " run_cmd
    echo "RUN $run_cmd" >> $DOCKERFILE
done
echo "" >> $DOCKERFILE

# COPY/ADD commands
while true; do
    read -p "Do you want to add a COPY or ADD command? (y/n) " add_copy_or_add
    if [[ $add_copy_or_add != "y" ]]; then
        break
    fi
    read -p "Choose COPY or ADD: " copy_or_add
    read -p "Enter source path: " source_path
    read -p "Enter destination path: " dest_path
    echo "$copy_or_add $source_path $dest_path" >> $DOCKERFILE
done
echo "" >> $DOCKERFILE

# Expose ports
while true; do
    read -p "Do you want to expose a port? (y/n) " expose_port
    if [[ $expose_port != "y" ]]; then
        break
    fi
    read -p "Enter the port number: " port_number
    echo "EXPOSE $port_number" >> $DOCKERFILE
done
echo "" >> $DOCKERFILE

# CMD or ENTRYPOINT
read -p "Do you want to set CMD or ENTRYPOINT? (cmd/entrypoint/none): " cmd_or_entrypoint
if [[ $cmd_or_entrypoint == "cmd" ]]; then
    read -p "Enter CMD command (e.g., /bin/bash): " cmd_command
    echo "CMD [\"$cmd_command\"]" >> $DOCKERFILE
elif [[ $cmd_or_entrypoint == "entrypoint" ]]; then
    read -p "Enter ENTRYPOINT command (e.g., /app/start.sh): " entry_command
    echo "ENTRYPOINT [\"$entry_command\"]" >> $DOCKERFILE
fi

echo "Dockerfile created!"
