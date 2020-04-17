#!/bin/bash -eux

CURRENT_MODULE=$(basename "$(pwd)")
printf "\033[0;32mUpdate sub module ${CURRENT_MODULE}...\033[0m\n"
msg="Commit in $(date)"

if [ -n "$*" ]; then
    msg="$*"
fi

git add .
git commit -m "${msg}"
git push -u origin master

cd ../..
MASTER_MODULE=$(basename "$(pwd)")
printf "\033[0;32mUpdate master module ${MASTER_MODULE}...\033[0m\n"
if [[ -f "deploy.sh" ]]; then
    ./deploy.sh "${msg}"
fi