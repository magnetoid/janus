# nix/packages.nix — Janus Agent package built with uv2nix
{ inputs, ... }:
{
  perSystem =
    { pkgs, lib, inputs', ... }:
    let
      janusAgent = pkgs.callPackage ./janus-agent.nix {
        inherit (inputs) uv2nix pyproject-nix pyproject-build-systems;
        npm-lockfile-fix = inputs'.npm-lockfile-fix.packages.default;
        # Only embed clean revs — dirtyRev doesn't represent any upstream
        # commit, so comparing it would always claim "update available".
        rev = inputs.self.rev or null;
      };
    in
    {
      packages = {
        default = janusAgent;

        # Ships discord.py + python-telegram-bot + slack-sdk so a plain
        # `nix profile install .#messaging` connects to Discord/Telegram/Slack
        # on first run — lazy-install can't write to the read-only /nix/store.
        messaging = janusAgent.override {
          extraDependencyGroups = [ "messaging" ];
        };

        # All platform-portable optional integrations pre-built.
        # matrix is Linux-only (oqs/liboqs lacks aarch64-darwin wheels).
        full = janusAgent.override {
          extraDependencyGroups = [
            "anthropic"
            "azure-identity"
            "bedrock"
            "daytona"
            "dingtalk"
            "edge-tts"
            "exa"
            "fal"
            "feishu"
            "firecrawl"
            "hindsight"
            "honcho"
            "messaging"
            "modal"
            "parallel-web"
            "tts-premium"
            "voice"
          ] ++ lib.optionals pkgs.stdenv.isLinux [ "matrix" ];
        };

        tui = janusAgent.janusTui;
        web = janusAgent.janusWeb;
        desktop = janusAgent.janusDesktop;

        fix-lockfiles = janusAgent.janusNpmLib.mkFixLockfiles { attr = "tui"; };
      };
    };
}
