# Boar's Head SCADA Wiki server (docker compose up -d --build wiki -> http://localhost:3030).
# The compose service bind-mounts ./wiki to /app and keeps node_modules in the named volume bh-wiki-node-modules.
# On start it reinstalls when package-lock.json changed, builds the static site (the offline search index only
# exists in a production build) and serves it. A failed build is retried every 5 minutes (pages being edited).
# Rebuild after doc edits: docker restart bh-wiki
FROM node:22-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund && cp package-lock.json node_modules/.bh-lock
COPY . .
# Own generated-files dir so a container build never collides with a host build in the same bind mount.
ENV DOCUSAURUS_GENERATED_FILES_DIR_NAME=.docusaurus-container
EXPOSE 3000
CMD ["sh", "-c", "cmp -s package-lock.json node_modules/.bh-lock || { npm ci --no-audit --no-fund && cp package-lock.json node_modules/.bh-lock; }; until npx docusaurus build --out-dir /tmp/wiki-build; do echo '[wiki] build failed, retrying in 5 min'; sleep 300; done; exec npx docusaurus serve --dir /tmp/wiki-build --host 0.0.0.0 --port 3000 --no-open"]
