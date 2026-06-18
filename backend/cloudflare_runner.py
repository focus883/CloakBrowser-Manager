import os
import subprocess

CLOUDFLARED_BIN = "/app/cloudflared"

def ensure_cloudflared():
    """下载 cloudflared 二进制文件"""
    if not os.path.exists(CLOUDFLARED_BIN):
        subprocess.run([
            "wget",
            "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64",
            "-O", CLOUDFLARED_BIN
        ])
        subprocess.run(["chmod", "+x", CLOUDFLARED_BIN])


def start_cloudflare_tunnel():
    """使用环境变量中的 token 自动连接 Cloudflare Tunnel"""
    token = os.getenv("CLOUDFLARE_TUNNEL_TOKEN")
    if not token:
        print("⚠️ 未设置 CLOUDFLARE_TUNNEL_TOKEN 环境变量，跳过 cloudflared 启动")
        return

    subprocess.Popen(
        [CLOUDFLARED_BIN, "tunnel", "run", "--token", token],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
