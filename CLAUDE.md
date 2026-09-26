# OpenSEO setup for this repository

This repository carries the OpenSEO Agent Skills so every Claude Code cloud
session on it can run OpenSEO workflows.

## Skills

The ten public OpenSEO skills live in `.claude/skills/` (copied from
`plugins/openseo/skills` in <https://github.com/every-app/open-seo>). Invoke one
with its name, for example `/seo-audit`, `/seo-project-setup`,
`/keyword-research`, or `/local-seo`. Update them with `npx skills update`.

## OpenSEO MCP (live data)

The skills need the OpenSEO MCP server (`https://app.openseo.so/mcp`). Cloud
sessions cannot complete a browser OAuth login inside the VM, so the server is
connected in one of two ways:

1. **Preferred (OAuth):** add OpenSEO as a custom connector on claude.ai
   (Customize -> Connectors -> Add custom connector, URL above), approve the
   OpenSEO login, then enable the connector on new sessions. Connector traffic
   goes through Anthropic's servers, so no network allowlist change is needed.
2. **Fallback (API key):** create a key at <https://app.openseo.so/settings>
   (Settings -> API keys), store it in the cloud environment as the
   `OPENSEO_API_KEY` environment variable or API credential, add
   `app.openseo.so` to the environment's allowed domains, and commit a
   project-scope `.mcp.json`:

   ```json
   {
     "mcpServers": {
       "openseo": {
         "type": "http",
         "url": "https://app.openseo.so/mcp",
         "headers": { "Authorization": "Bearer ${OPENSEO_API_KEY}" }
       }
     }
   }
   ```

Use only one of the two so the tools are not duplicated. Verify with the free
`whoami` and `list_projects` tools before running paid research.

The official Claude Code plugin (`openseo@openseo` from the `every-app/open-seo`
marketplace) is the preferred install on a local machine, but cloud sessions do
not load plugins from user or repository settings, which is why the skills are
committed here instead.
