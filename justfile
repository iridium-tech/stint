set dotenv-load := false

default:
    @just --list

setup-engine:
    cd engine && uv sync

setup-frontend:
    cd frontend && bun install

setup-root:
    bun install

setup: setup-root setup-engine setup-frontend
    @echo "ready"


install-hooks:
    bunx prek install

gen:
    buf generate
    find engine/src/api -type d -exec touch {}/__init__.py \;

clean-gen:
    rm -rf engine/src/api frontend/src/api

regen: clean-gen gen

dev-engine:
    cd engine && uv run uvicorn server:app --reload

dev-frontend:
    cd frontend && bun dev

dev:
    #!/usr/bin/env bash
    trap 'kill 0' EXIT
    just dev-engine &
    just dev-frontend &
    wait

check-engine:
    cd engine && uv run ty check

check-frontend:
    cd frontend && bun run biome check src

check: check-engine check-frontend

build-frontend:
    cd frontend && bun run build && bun run .output/server/index.mjs
